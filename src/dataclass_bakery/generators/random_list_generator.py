from dataclasses import is_dataclass

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators import random_data_class_generator
from dataclass_bakery.generators.random_generator import RandomGenerator


class RandomListGenerator(RandomGenerator):
    """
    Class to generate random list
    """

    def generate(self, *args, **kwargs) -> list:
        max_length = kwargs.get(defaults.MAX_LENGTH_ARG, defaults.MAX_LIST_LENGTH)

        default_value_type = kwargs.get(
            defaults.DEFAULT_VALUE_TYPE_ARG, defaults.DEFAULT_VALUE_TYPE
        )

        value_type = kwargs.get(defaults.VALUE_TYPE_ARG, default_value_type)

        if is_dataclass(value_type):
            generator = random_data_class_generator.RandomDataClassGenerator()
        else:
            generator = defaults.TYPING_GENERATORS[value_type]()

        random_list = []
        for _ in range(max_length):
            if is_dataclass(value_type):
                list_value = generator.generate(value_type)
            else:
                list_value = generator.generate()

            random_list.append(list_value)

        return random_list
