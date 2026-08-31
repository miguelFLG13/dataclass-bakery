from collections import defaultdict

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators import random_data_class_generator
from dataclass_bakery.generators.random_generator import RandomGenerator


class RandomDefaultdictGenerator(RandomGenerator):
    """
    Class to generate a random defaultdict. The default_factory is the
    value type itself (matching the conventional ``defaultdict(int)``,
    ``defaultdict(list)``... usage), when it is callable with no arguments.
    """

    def generate(self, *args, **kwargs) -> defaultdict:
        max_length = kwargs.get(defaults.MAX_LENGTH_ARG, defaults.MAX_DEFAULTDICT_LENGTH)

        default_key_type = kwargs.get(
            defaults.DEFAULT_KEY_TYPE_ARG, defaults.DEFAULT_KEY_TYPE
        )
        default_value_type = kwargs.get(
            defaults.DEFAULT_VALUE_TYPE_ARG, defaults.DEFAULT_VALUE_TYPE
        )

        key_type = kwargs.get(defaults.KEY_TYPE_ARG, default_key_type)
        value_type = kwargs.get(defaults.VALUE_TYPE_ARG, default_value_type)

        default_factory = value_type if callable(value_type) else None
        random_defaultdict = defaultdict(default_factory)
        for _ in range(max_length):
            dict_key = random_data_class_generator.generate_value(key_type)
            dict_value = random_data_class_generator.generate_value(value_type)
            random_defaultdict[dict_key] = dict_value

        return random_defaultdict
