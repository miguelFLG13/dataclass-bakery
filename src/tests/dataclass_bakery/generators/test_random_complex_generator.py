from unittest import TestCase

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_complex_generator import RandomComplexGenerator


class TestRandomComplexGenerator(TestCase):
    def setUp(self):
        self.random_complex_generator = RandomComplexGenerator()

    def test_generate_complex_ok(self):
        random_complex = self.random_complex_generator.generate()
        self.assertIsInstance(random_complex, complex)

    def test_generate_complex_correct_min_limit_ok(self):
        min_limit = defaults.NUMBER_MAX_LIMIT - 1
        random_complex = self.random_complex_generator.generate(
            **{defaults.NUMBER_MIN_LIMIT_ARG: min_limit}
        )
        self.assertIsInstance(random_complex, complex)

        self.assertTrue(min_limit <= random_complex.imag <= defaults.NUMBER_MAX_LIMIT)
        self.assertTrue(min_limit <= random_complex.real <= defaults.NUMBER_MAX_LIMIT)

    def test_generate_complex_correct_max_limit_ok(self):
        max_limit = defaults.NUMBER_MIN_LIMIT + 1
        random_complex = self.random_complex_generator.generate(
            **{defaults.NUMBER_MAX_LIMIT_ARG: max_limit}
        )
        self.assertIsInstance(random_complex, complex)

        self.assertTrue(defaults.NUMBER_MIN_LIMIT <= random_complex.imag <= max_limit)
        self.assertTrue(defaults.NUMBER_MIN_LIMIT <= random_complex.real <= max_limit)

    def test_generate_complex_incorrect_min_limit_ko(self):
        with self.assertRaises(TypeError):
            self.random_complex_generator.generate(
                **{defaults.NUMBER_MIN_LIMIT_ARG: "asd"}
            )

    def test_generate_complex_incorrect_max_limit_ko(self):
        with self.assertRaises(TypeError):
            self.random_complex_generator.generate(
                **{defaults.NUMBER_MAX_LIMIT_ARG: "asd"}
            )
