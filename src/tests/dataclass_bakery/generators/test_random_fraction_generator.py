from fractions import Fraction
from unittest import TestCase

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_fraction_generator import (
    RandomFractionGenerator,
)


class TestRandomFractionGenerator(TestCase):
    def setUp(self):
        self.random_fraction_generator = RandomFractionGenerator()

    def test_generate_fraction_ok(self):
        random_fraction = self.random_fraction_generator.generate()
        self.assertIsInstance(random_fraction, Fraction)

    def test_generate_fraction_incorrect_min_denominator_ko(self):
        with self.assertRaises(ValueError):
            self.random_fraction_generator.generate(
                **{defaults.FRACTION_DENOMINATOR_MIN_LIMIT_ARG: 0}
            )

    def test_generate_fraction_incorrect_denominator_range_ko(self):
        with self.assertRaises(ValueError):
            self.random_fraction_generator.generate(
                **{
                    defaults.FRACTION_DENOMINATOR_MIN_LIMIT_ARG: 10,
                    defaults.FRACTION_DENOMINATOR_MAX_LIMIT_ARG: 5,
                }
            )
