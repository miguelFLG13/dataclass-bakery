from unittest import TestCase

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_int_generator import RandomIntGenerator


class TestRandomIntGenerator(TestCase):
    def setUp(self):
        self.random_int_generator = RandomIntGenerator()

    def test_generate_int_ok(self):
        random_int = self.random_int_generator.generate()
        self.assertIsInstance(random_int, int)

    def test_generate_int_correct_min_limit_ok(self):
        min_limit = defaults.NUMBER_MAX_LIMIT - 1
        random_int = self.random_int_generator.generate(
            **{defaults.NUMBER_MIN_LIMIT_ARG: min_limit}
        )
        self.assertIsInstance(random_int, int)

        self.assertTrue(min_limit <= random_int <= defaults.NUMBER_MAX_LIMIT)

    def test_generate_int_correct_max_limit_ok(self):
        max_limit = defaults.NUMBER_MIN_LIMIT + 1
        random_int = self.random_int_generator.generate(
            **{defaults.NUMBER_MAX_LIMIT_ARG: max_limit}
        )
        self.assertIsInstance(random_int, int)

        self.assertTrue(defaults.NUMBER_MIN_LIMIT <= random_int <= max_limit)

    def test_generate_int_incorrect_min_limit_ko(self):
        with self.assertRaises(ValueError):
            self.random_int_generator.generate(**{defaults.NUMBER_MIN_LIMIT_ARG: "asd"})

    def test_generate_int_incorrect_max_limit_ko(self):
        with self.assertRaises(TypeError):
            self.random_int_generator.generate(**{defaults.NUMBER_MAX_LIMIT_ARG: "asd"})
