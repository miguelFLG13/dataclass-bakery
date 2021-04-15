from dataclasses import is_dataclass
from typing import _GenericAlias, Any, Literal, Union

from dataclass_bakery.generators.defaults import TYPING_GENERATORS


class RandomDataClassGenerator:
    def generate(self, data_class: Any, *args, **kwargs) -> Any:
        random_data = {}
        for field_name, field_type in data_class.__annotations__.items():

            arguments = kwargs.get(field_name, {})

            if isinstance(field_type, _GenericAlias) and field_type.__origin__ == Union:
                has_new_type = False
                for argument in field_type.__args__:
                    if argument != type(None):
                        has_new_type = True
                        field_type = argument

                    if (
                        not hasattr(field_type, "__origin__")
                        or field_type.__origin__ != Union
                    ):
                        break

                if not has_new_type:
                    raise TypeError(f"Union without Typing in dataclass {field_name}")

            if (
                isinstance(field_type, _GenericAlias)
                and field_type.__origin__ != Literal
            ):
                arguments_lenght = len(field_type.__args__)
                if arguments_lenght > 1:  # Is a Dict
                    arguments["key_type"] = field_type.__args__[0]
                    arguments["value_type"] = field_type.__args__[1]
                elif arguments_lenght > 0:  # Is a List or Tuple
                    arguments["value_type"] = field_type.__args__[0]

                field_type = field_type.__origin__

            elif (
                isinstance(field_type, _GenericAlias)
                and field_type.__origin__ == Literal
            ):
                arguments["options"] = field_type.__args__
                field_type = field_type.__origin__

            if is_dataclass(field_type):
                generator = RandomDataClassGenerator()
                field_randomized = generator.generate(field_type, **arguments)
            else:
                generator_class = TYPING_GENERATORS.get(field_type)
                generator = generator_class()
                field_randomized = generator.generate(**arguments)

            random_data[field_name] = field_randomized

        return data_class(**random_data)
