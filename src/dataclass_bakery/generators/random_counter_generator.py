import random
from collections import Counter

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators import random_data_class_generator
from dataclass_bakery.generators.random_generator import RandomGenerator


class RandomCounterGenerator(RandomGenerator):
    """
    Class to generate random Counter. The generic type argument (if any)
    represents the type of the counted items, following ``Counter[str]``
    typing semantics; counts are always random ints.
    """

    def generate(self, *args, **kwargs) -> Counter:
        max_length = kwargs.get(defaults.MAX_LENGTH_ARG, defaults.MAX_COUNTER_LENGTH)

        default_item_type = kwargs.get(
            defaults.DEFAULT_VALUE_TYPE_ARG, defaults.DEFAULT_KEY_TYPE
        )
        item_type = kwargs.get(defaults.VALUE_TYPE_ARG, default_item_type)

        min_limit = kwargs.get(defaults.NUMBER_MIN_LIMIT_ARG, defaults.NUMBER_MIN_LIMIT)
        max_limit = kwargs.get(defaults.NUMBER_MAX_LIMIT_ARG, defaults.NUMBER_MAX_LIMIT)

        random_counter = Counter()
        for _ in range(max_length):
            item = random_data_class_generator.generate_value(item_type)
            random_counter[item] = random.randint(min_limit, max_limit)

        return random_counter
