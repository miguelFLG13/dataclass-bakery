from unittest import TestCase

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_tuple_generator import RandomTupleGenerator
from dataclass_bakery.generators.random_str_generator import RandomStrGenerator


class TestRandomTupleGenerator(TestCase):
    def setUp(self):
        self.random_tuple_generator = RandomTupleGenerator()

    def test_generate_tuple_ok(self):
        random_tuple = self.random_tuple_generator.generate()

        self.assertIsInstance(random_tuple, tuple)
        self.assertIsInstance(random_tuple[0], int)
        self.assertEqual(len(random_tuple), defaults.MAX_LIST_LENGTH)

    def test_generate_tuple_correct_max_length_ok(self):
        max_length = 20
        random_tuple = self.random_tuple_generator.generate(
            **{defaults.MAX_LENGTH_ARG: max_length}
        )

        self.assertIsInstance(random_tuple, tuple)
        self.assertIsInstance(random_tuple[0], int)
        self.assertEqual(len(random_tuple), max_length)

    def test_generate_tuple_changing_values_generator_ok(self):
        value_type = str
        random_tuple = self.random_tuple_generator.generate(
            **{defaults.VALUE_TYPE_ARG: value_type}
        )

        self.assertIsInstance(random_tuple, tuple)
        self.assertIsInstance(random_tuple[0], value_type)

    def test_generate_tuple_incorrect_max_length_ko(self):
        with self.assertRaises(TypeError):
            self.random_tuple_generator.generate(**{defaults.MAX_LENGTH_ARG: "asd"})

    def test_generate_tuple_incorrect_generator_ko(self):
        with self.assertRaises(KeyError):
            self.random_tuple_generator.generate(**{defaults.VALUE_TYPE_ARG: None})
