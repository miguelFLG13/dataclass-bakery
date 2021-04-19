import random
from decimal import Decimal

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_generator import RandomGenerator


class RandomDecimalGenerator(RandomGenerator):
    """
    Class to generate random decimal number
    """

    def generate(self, *args, **kwargs) -> Decimal:
        min_limit = kwargs.get(defaults.NUMBER_MIN_LIMIT_ARG, defaults.NUMBER_MIN_LIMIT)
        max_limit = kwargs.get(defaults.NUMBER_MAX_LIMIT_ARG, defaults.NUMBER_MAX_LIMIT)
        decimals = kwargs.get(defaults.DECIMALS_ARG, defaults.DECIMALS)
        random_number = random.uniform(min_limit, max_limit)
        rounded_number = round(random_number, decimals)
        string_number = str(rounded_number)
        return Decimal(string_number)
