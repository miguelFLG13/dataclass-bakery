from unittest import TestCase

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_str_generator import RandomStrGenerator


class TestRandomStrGenerator(TestCase):
    def setUp(self):
        self.random_str_generator = RandomStrGenerator()

    def test_generate_str_ok(self):
        random_str = self.random_str_generator.generate()
        self.assertIsInstance(random_str, str)

    def test_generate_str_correct_max_length_ok(self):
        str_length = 20
        random_str = self.random_str_generator.generate(
            **{defaults.MAX_LENGTH_ARG: str_length}
        )
        self.assertIsInstance(random_str, str)
        self.assertEqual(len(random_str), str_length)

    def test_generate_int_incorrect_max_length_ko(self):
        with self.assertRaises(TypeError):
            self.random_str_generator.generate(**{defaults.MAX_LENGTH_ARG: "asd"})
