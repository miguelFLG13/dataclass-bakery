import random
from dataclasses import is_dataclass
from enum import Enum
from typing import Any, Literal, Union, get_args, get_origin, is_typeddict

from dataclass_bakery.generators import defaults


def is_named_tuple(cls: Any) -> bool:
    return isinstance(cls, type) and issubclass(cls, tuple) and hasattr(cls, "_fields")


def is_annotated_record(cls: Any) -> bool:
    """
    True for any class whose random instance can be built the same way as a
    dataclass: iterate its annotated fields, generate each one, and call the
    class with those fields as keyword arguments. Covers dataclasses,
    typing.NamedTuple classes and typing.TypedDict classes.
    """
    return is_dataclass(cls) or is_named_tuple(cls) or is_typeddict(cls)


def resolve_field_type(field_type: Any, arguments: dict, field_name: str = "value"):
    """
    Resolves a raw type annotation into a concrete type ready to be looked
    up in defaults.TYPING_GENERATORS (or checked with is_annotated_record),
    mutating and returning `arguments` with whatever extra generator kwargs
    the resolution produces (_key_type_, _value_type_, _options_, _enum_class_).

    Uses typing.get_origin/get_args (the public, stable API) instead of
    poking at private _GenericAlias internals: it is the only approach that
    behaves consistently for typing.Union[...], Optional[...], the PEP 604
    `X | Y` syntax and the PEP 585 builtin generics (`list[int]`,
    `dict[str, int]`, ...) across Python 3.12, 3.13 and 3.14, where Union
    stopped being a _GenericAlias instance.
    """
    while get_origin(field_type) == Union:
        options = [argument for argument in get_args(field_type) if argument != type(None)]
        if not options:
            raise TypeError(f"Union without Typing in dataclass {field_name}")
        field_type = random.choice(options)

    field_origin = get_origin(field_type)
    if field_origin is not None and field_origin != Literal:  # Is a Dict, List, Set...
        field_args = get_args(field_type)
        arguments_lenght = len(field_args)
        if arguments_lenght > 1:  # Is a Dict
            arguments[defaults.KEY_TYPE_ARG] = field_args[0]
            arguments[defaults.VALUE_TYPE_ARG] = field_args[1]
        elif arguments_lenght > 0:  # Is a List, Tuple, Set, Type...
            arguments[defaults.VALUE_TYPE_ARG] = field_args[0]

        field_type = field_origin

    elif field_origin is not None and field_origin == Literal:
        arguments[defaults.OPTIONS_ARG] = get_args(field_type)
        field_type = field_origin

    if isinstance(field_type, type) and issubclass(field_type, Enum):
        arguments[defaults.ENUM_CLASS_ARG] = field_type
        field_type = Enum

    return field_type, arguments


def generate_value(field_type: Any, arguments: dict = None, field_name: str = "value") -> Any:
    """
    Generates a random value for an arbitrary type annotation: a scalar
    type, a generic container (possibly nested, e.g. List[List[int]] or
    Dict[str, List[int]]), a Literal, an Enum, a Union/Optional, or a
    dataclass/NamedTuple/TypedDict. This is the single place that knows how
    to turn "a typing annotation" into "a random value", used both for
    dataclass fields and for the items of any container generator.
    """
    field_type, arguments = resolve_field_type(field_type, dict(arguments or {}), field_name)

    if is_annotated_record(field_type):
        return RandomDataClassGenerator().generate(field_type, **arguments)

    generator_class = defaults.TYPING_GENERATORS[field_type]
    generator = generator_class()
    return generator.generate(**arguments)


class RandomDataClassGenerator:
    def generate(self, data_class: Any, *args, **kwargs) -> Any:
        random_data = {}
        for field_name, field_type in data_class.__annotations__.items():

            arguments = kwargs.get(field_name, {})
            if arguments.get(defaults.IGNORE_ARG):
                random_data[field_name] = None
                continue

            if defaults.FIXED_VALUE_ARG in arguments:  # Value fixed
                random_data[field_name] = arguments[defaults.FIXED_VALUE_ARG]
                continue

            if defaults.GENERATOR_ARG in arguments:  # Generator fixed
                generator = arguments[defaults.GENERATOR_ARG]()
                field_randomized = generator.generate(**arguments)
                random_data[field_name] = field_randomized
                continue

            random_data[field_name] = generate_value(field_type, arguments, field_name)

        return data_class(**random_data)
