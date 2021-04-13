from dataclasses import is_dataclass, make_dataclass
from typing import _GenericAlias, Any

from dataclass_bakery.generators.defaults import TYPING_GENERATORS


class RandomDataClassGenerator:
    def generate(self, data_class: Any, *args, **kwargs) -> Any:
        random_data = {}
        for field_name, field_type in data_class.__annotations__.items():

            field_is_dataclass = is_dataclass(field_type)

            arguments = {}
            if field_is_dataclass:
                generator = RandomDataClassGenerator()
                field_randomized = generator.generate(field_type, **arguments)
            else:
                if isinstance(field_type, _GenericAlias):
                    arguments_lenght = len(field_type.__args__)
                    if arguments_lenght > 1:  # Is a Dict
                        arguments["key_type"] = field_type.__args__[0]
                        arguments["value_type"] = field_type.__args__[1]
                    elif arguments_lenght > 0:  # Is a List or Tuple
                        arguments["value_type"] = field_type.__args__[0]

                    field_type = field_type.__origin__

                generator_class = TYPING_GENERATORS.get(field_type)
                generator = generator_class()
                field_randomized = generator.generate(**arguments)

            random_data[field_name] = field_randomized

        return data_class(**random_data)
