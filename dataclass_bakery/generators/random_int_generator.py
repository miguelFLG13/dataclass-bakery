import random

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_generator import RandomGenerator


class RandomIntGenerator(RandomGenerator):
    """
    Class to generate random int number
    """

    def generate(self, *args, **kwargs) -> int:
        min_limit = defaults.NUMBER_MIN_LIMIT
        max_limit = defaults.NUMBER_MAX_LIMIT
        random_number = random.randint(min_limit, max_limit)
        return random_number
