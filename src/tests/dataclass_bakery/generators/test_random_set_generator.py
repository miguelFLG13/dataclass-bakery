from unittest import TestCase

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_set_generator import RandomSetGenerator
from dataclass_bakery.generators.random_str_generator import RandomStrGenerator


class TestRandomSetGenerator(TestCase):
    def setUp(self):
        self.random_set_generator = RandomSetGenerator()

    def test_generate_set_ok(self):
        random_set = self.random_set_generator.generate()

        self.assertIsInstance(random_set, set)
        self.assertIsInstance(random_set.pop(), int)
        self.assertTrue(len(random_set) <= defaults.MAX_LIST_LENGTH)

    def test_generate_set_correct_max_length_ok(self):
        max_length = 20
        random_set = self.random_set_generator.generate(
            **{defaults.MAX_LENGTH_ARG: max_length}
        )

        self.assertIsInstance(random_set, set)
        self.assertIsInstance(random_set.pop(), int)
        self.assertTrue(len(random_set) <= max_length)

    def test_generate_set_changing_values_generator_ok(self):
        value_type = str
        random_set = self.random_set_generator.generate(
            **{defaults.VALUE_TYPE_ARG: value_type}
        )

        self.assertIsInstance(random_set, set)
        self.assertIsInstance(random_set.pop(), value_type)

    def test_generate_set_incorrect_max_length_ko(self):
        with self.assertRaises(TypeError):
            self.random_set_generator.generate(**{defaults.MAX_LENGTH_ARG: "asd"})

    def test_generate_set_incorrect_generator_ko(self):
        with self.assertRaises(KeyError):
            self.random_set_generator.generate(**{defaults.VALUE_TYPE_ARG: None})
