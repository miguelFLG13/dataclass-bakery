from decimal import Decimal
from unittest import TestCase

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_decimal_generator import RandomDecimalGenerator


class TestRandomDecimalGenerator(TestCase):
    def setUp(self):
        self.random_decimal_generator = RandomDecimalGenerator()

    def test_generate_decimal_ok(self):
        random_decimal = self.random_decimal_generator.generate()
        self.assertIsInstance(random_decimal, Decimal)

    def test_generate_decimal_correct_min_limit_ok(self):
        min_limit = defaults.NUMBER_MAX_LIMIT - 1
        random_decimal = self.random_decimal_generator.generate(
            **{defaults.NUMBER_MIN_LIMIT_ARG: min_limit}
        )
        self.assertIsInstance(random_decimal, Decimal)

        self.assertTrue(min_limit <= random_decimal <= defaults.NUMBER_MAX_LIMIT)

    def test_generate_decimal_correct_max_limit_ok(self):
        max_limit = defaults.NUMBER_MIN_LIMIT + 1
        random_decimal = self.random_decimal_generator.generate(
            **{defaults.NUMBER_MAX_LIMIT_ARG: max_limit}
        )
        self.assertIsInstance(random_decimal, Decimal)

        self.assertTrue(defaults.NUMBER_MIN_LIMIT <= random_decimal <= max_limit)

    def test_generate_decimal_incorrect_min_limit_ko(self):
        with self.assertRaises(TypeError):
            self.random_decimal_generator.generate(
                **{defaults.NUMBER_MIN_LIMIT_ARG: "asd"}
            )

    def test_generate_decimal_incorrect_max_limit_ko(self):
        with self.assertRaises(TypeError):
            self.random_decimal_generator.generate(
                **{defaults.NUMBER_MAX_LIMIT_ARG: "asd"}
            )
