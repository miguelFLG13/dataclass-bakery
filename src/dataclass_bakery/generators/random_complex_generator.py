import random

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_generator import RandomGenerator


class RandomComplexGenerator(RandomGenerator):
    """
    Class to generate random complex number
    """

    def generate(self, *args, **kwargs) -> complex:
        min_limit = kwargs.get(defaults.NUMBER_MIN_LIMIT_ARG, defaults.NUMBER_MIN_LIMIT)
        max_limit = kwargs.get(defaults.NUMBER_MAX_LIMIT_ARG, defaults.NUMBER_MAX_LIMIT)

        decimals = kwargs.get(defaults.DECIMALS_ARG, defaults.DECIMALS)
        real_part = random.uniform(min_limit, max_limit)
        rounded_real_part = round(real_part, decimals)
        imaginary_part = random.uniform(min_limit, max_limit)
        rounded_imaginary_part = round(imaginary_part, decimals)
        return complex(rounded_real_part, rounded_imaginary_part)
