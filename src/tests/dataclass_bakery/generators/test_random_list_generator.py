from unittest import TestCase

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_list_generator import RandomListGenerator
from dataclass_bakery.generators.random_str_generator import RandomStrGenerator


class TestRandomListGenerator(TestCase):
    def setUp(self):
        self.random_list_generator = RandomListGenerator()

    def test_generate_list_ok(self):
        random_list = self.random_list_generator.generate()

        self.assertIsInstance(random_list, list)
        self.assertIsInstance(random_list[0], int)
        self.assertEqual(len(random_list), defaults.MAX_LIST_LENGTH)

    def test_generate_list_correct_max_length_ok(self):
        max_length = 20
        random_list = self.random_list_generator.generate(
            **{defaults.MAX_LENGTH_ARG: max_length}
        )

        self.assertIsInstance(random_list, list)
        self.assertIsInstance(random_list[0], int)
        self.assertEqual(len(random_list), max_length)

    def test_generate_list_changing_values_generator_ok(self):
        value_type = str
        random_list = self.random_list_generator.generate(
            **{defaults.VALUE_TYPE_ARG: value_type}
        )

        self.assertIsInstance(random_list, list)
        self.assertIsInstance(random_list[0], value_type)

    def test_generate_list_incorrect_max_length_ko(self):
        with self.assertRaises(TypeError):
            self.random_list_generator.generate(**{defaults.MAX_LENGTH_ARG: "asd"})

    def test_generate_list_incorrect_generator_ko(self):
        with self.assertRaises(KeyError):
            self.random_list_generator.generate(**{defaults.VALUE_TYPE_ARG: None})
