import random
from fractions import Fraction

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_generator import RandomGenerator


class RandomFractionGenerator(RandomGenerator):
    """
    Class to generate random Fraction
    """

    def generate(self, *args, **kwargs) -> Fraction:
        min_limit = kwargs.get(defaults.NUMBER_MIN_LIMIT_ARG, defaults.NUMBER_MIN_LIMIT)
        max_limit = kwargs.get(defaults.NUMBER_MAX_LIMIT_ARG, defaults.NUMBER_MAX_LIMIT)

        min_denominator_limit = kwargs.get(
            defaults.FRACTION_DENOMINATOR_MIN_LIMIT_ARG,
            defaults.FRACTION_DENOMINATOR_MIN_LIMIT,
        )
        if min_denominator_limit < 1:
            raise ValueError("Error: Min denominator incorrect")

        max_denominator_limit = kwargs.get(
            defaults.FRACTION_DENOMINATOR_MAX_LIMIT_ARG,
            defaults.FRACTION_DENOMINATOR_MAX_LIMIT,
        )
        if min_denominator_limit > max_denominator_limit:
            raise ValueError("Error: Min denominator > Max denominator")

        numerator = random.randint(min_limit, max_limit)
        denominator = random.randint(min_denominator_limit, max_denominator_limit)

        return Fraction(numerator, denominator)
