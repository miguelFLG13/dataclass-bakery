from collections import deque
from unittest import TestCase

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_deque_generator import RandomDequeGenerator


class TestRandomDequeGenerator(TestCase):
    def setUp(self):
        self.random_deque_generator = RandomDequeGenerator()

    def test_generate_deque_ok(self):
        random_deque = self.random_deque_generator.generate()

        self.assertIsInstance(random_deque, deque)
        self.assertIsInstance(random_deque[0], int)
        self.assertEqual(len(random_deque), defaults.MAX_DEQUE_LENGTH)

    def test_generate_deque_correct_max_length_ok(self):
        max_length = 20
        random_deque = self.random_deque_generator.generate(
            **{defaults.MAX_LENGTH_ARG: max_length}
        )

        self.assertIsInstance(random_deque, deque)
        self.assertEqual(len(random_deque), max_length)

    def test_generate_deque_changing_values_generator_ok(self):
        value_type = str
        random_deque = self.random_deque_generator.generate(
            **{defaults.VALUE_TYPE_ARG: value_type}
        )

        self.assertIsInstance(random_deque, deque)
        self.assertIsInstance(random_deque[0], value_type)

    def test_generate_deque_incorrect_max_length_ko(self):
        with self.assertRaises(TypeError):
            self.random_deque_generator.generate(**{defaults.MAX_LENGTH_ARG: "asd"})

    def test_generate_deque_incorrect_generator_ko(self):
        with self.assertRaises(KeyError):
            self.random_deque_generator.generate(**{defaults.VALUE_TYPE_ARG: None})
