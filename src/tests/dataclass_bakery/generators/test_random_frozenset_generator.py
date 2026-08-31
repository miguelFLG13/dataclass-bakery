from unittest import TestCase

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_frozenset_generator import (
    RandomFrozensetGenerator,
)


class TestRandomFrozensetGenerator(TestCase):
    def setUp(self):
        self.random_frozenset_generator = RandomFrozensetGenerator()

    def test_generate_frozenset_ok(self):
        random_frozenset = self.random_frozenset_generator.generate()

        self.assertIsInstance(random_frozenset, frozenset)
        self.assertTrue(len(random_frozenset) <= defaults.MAX_FROZENSET_LENGTH)

    def test_generate_frozenset_correct_max_length_ok(self):
        max_length = 20
        random_frozenset = self.random_frozenset_generator.generate(
            **{defaults.MAX_LENGTH_ARG: max_length}
        )

        self.assertIsInstance(random_frozenset, frozenset)
        self.assertTrue(len(random_frozenset) <= max_length)

    def test_generate_frozenset_changing_values_generator_ok(self):
        value_type = str
        random_frozenset = self.random_frozenset_generator.generate(
            **{defaults.VALUE_TYPE_ARG: value_type}
        )

        self.assertIsInstance(random_frozenset, frozenset)
        self.assertIsInstance(next(iter(random_frozenset)), value_type)

    def test_generate_frozenset_incorrect_max_length_ko(self):
        with self.assertRaises(TypeError):
            self.random_frozenset_generator.generate(
                **{defaults.MAX_LENGTH_ARG: "asd"}
            )

    def test_generate_frozenset_incorrect_generator_ko(self):
        with self.assertRaises(KeyError):
            self.random_frozenset_generator.generate(**{defaults.VALUE_TYPE_ARG: None})
