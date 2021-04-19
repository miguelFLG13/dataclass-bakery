from unittest import TestCase

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_float_generator import RandomFloatGenerator


class TestRandomFloatGenerator(TestCase):
    def setUp(self):
        self.random_float_generator = RandomFloatGenerator()

    def test_generate_float_ok(self):
        random_float = self.random_float_generator.generate()
        self.assertIsInstance(random_float, float)

    def test_generate_float_correct_min_limit_ok(self):
        min_limit = defaults.NUMBER_MAX_LIMIT - 1
        random_float = self.random_float_generator.generate(
            **{defaults.NUMBER_MIN_LIMIT_ARG: min_limit}
        )
        self.assertIsInstance(random_float, float)

        self.assertTrue(min_limit <= random_float <= defaults.NUMBER_MAX_LIMIT)

    def test_generate_float_correct_max_limit_ok(self):
        max_limit = defaults.NUMBER_MIN_LIMIT + 1
        random_float = self.random_float_generator.generate(
            **{defaults.NUMBER_MAX_LIMIT_ARG: max_limit}
        )
        self.assertIsInstance(random_float, float)

        self.assertTrue(defaults.NUMBER_MIN_LIMIT <= random_float <= max_limit)

    def test_generate_float_incorrect_min_limit_ko(self):
        with self.assertRaises(TypeError):
            self.random_float_generator.generate(
                **{defaults.NUMBER_MIN_LIMIT_ARG: "asd"}
            )

    def test_generate_float_incorrect_max_limit_ko(self):
        with self.assertRaises(TypeError):
            self.random_float_generator.generate(
                **{defaults.NUMBER_MAX_LIMIT_ARG: "asd"}
            )
