from collections import OrderedDict

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators import random_data_class_generator
from dataclass_bakery.generators.random_generator import RandomGenerator


class RandomOrderedDictGenerator(RandomGenerator):
    """
    Class to generate random OrderedDict
    """

    def generate(self, *args, **kwargs) -> OrderedDict:
        max_length = kwargs.get(defaults.MAX_LENGTH_ARG, defaults.MAX_ORDERED_DICT_LENGTH)

        default_key_type = kwargs.get(
            defaults.DEFAULT_KEY_TYPE_ARG, defaults.DEFAULT_KEY_TYPE
        )
        default_value_type = kwargs.get(
            defaults.DEFAULT_VALUE_TYPE_ARG, defaults.DEFAULT_VALUE_TYPE
        )

        key_type = kwargs.get(defaults.KEY_TYPE_ARG, default_key_type)
        value_type = kwargs.get(defaults.VALUE_TYPE_ARG, default_value_type)

        random_ordered_dict = OrderedDict()
        for _ in range(max_length):
            dict_key = random_data_class_generator.generate_value(key_type)
            dict_value = random_data_class_generator.generate_value(value_type)
            random_ordered_dict[dict_key] = dict_value

        return random_ordered_dict
