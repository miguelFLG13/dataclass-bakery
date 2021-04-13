import random

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_generator import RandomGenerator


class RandomRangeGenerator(RandomGenerator):
    """
    Class to generate random range
    """

    def generate(self, *args, **kwargs) -> range:
        min_limit = defaults.NUMBER_MIN_LIMIT
        max_limit = defaults.NUMBER_MAX_LIMIT
        range_start = random.randint(min_limit, max_limit)
        range_end = random.randint(min_limit, max_limit)
        random_range = range(range_start, range_end)
        return random_range
