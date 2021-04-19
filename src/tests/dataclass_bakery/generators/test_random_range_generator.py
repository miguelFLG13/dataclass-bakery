from unittest import TestCase

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_range_generator import RandomRangeGenerator


class TestRandomRangeGenerator(TestCase):
    def setUp(self):
        self.random_range_generator = RandomRangeGenerator()

    def test_generate_range_ok(self):
        random_range = self.random_range_generator.generate()
        self.assertIsInstance(random_range, range)

    def test_generate_range_correct_min_limit_ok(self):
        min_limit = defaults.NUMBER_MAX_LIMIT - 1
        random_range = self.random_range_generator.generate(
            **{defaults.NUMBER_MIN_LIMIT_ARG: min_limit}
        )
        self.assertIsInstance(random_range, range)

        self.assertTrue(min_limit <= random_range.start <= defaults.NUMBER_MAX_LIMIT)
        self.assertTrue(min_limit <= random_range.stop <= defaults.NUMBER_MAX_LIMIT)

    def test_generate_range_correct_max_limit_ok(self):
        max_limit = defaults.NUMBER_MIN_LIMIT + 1
        random_range = self.random_range_generator.generate(
            **{defaults.NUMBER_MAX_LIMIT_ARG: max_limit}
        )
        self.assertIsInstance(random_range, range)

        self.assertTrue(defaults.NUMBER_MIN_LIMIT <= random_range.start <= max_limit)
        self.assertTrue(defaults.NUMBER_MIN_LIMIT <= random_range.stop <= max_limit)

    def test_generate_range_incorrect_min_limit(self):
        with self.assertRaises(ValueError):
            self.random_range_generator.generate(
                **{defaults.NUMBER_MIN_LIMIT_ARG: "asd"}
            )

    def test_generate_range_incorrect_max_limit(self):
        with self.assertRaises(TypeError):
            self.random_range_generator.generate(
                **{defaults.NUMBER_MAX_LIMIT_ARG: "asd"}
            )
