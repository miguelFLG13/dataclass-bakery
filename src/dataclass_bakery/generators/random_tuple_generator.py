from dataclasses import is_dataclass

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators import random_data_class_generator
from dataclass_bakery.generators.random_generator import RandomGenerator


class RandomTupleGenerator(RandomGenerator):
    """
    Class to generate random tuple
    """

    def generate(self, *args, **kwargs) -> tuple:
        max_length = defaults.MAX_TUPLE_LENGTH

        default_value_type = defaults.DEFAULT_VALUE_TYPE

        value_type = kwargs.get("value_type", default_value_type)

        if is_dataclass(value_type):
            generator = random_data_class_generator.RandomDataClassGenerator()
        else:
            generator = defaults.TYPING_GENERATORS[value_type]()

        random_tuple = []
        for _ in range(max_length):
            if is_dataclass(value_type):
                tuple_value = generator.generate(value_type)
            else:
                tuple_value = generator.generate()
            random_tuple.append(tuple_value)

        return tuple(random_tuple)
