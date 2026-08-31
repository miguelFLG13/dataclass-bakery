from collections import OrderedDict
from unittest import TestCase

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_ordered_dict_generator import (
    RandomOrderedDictGenerator,
)


class TestRandomOrderedDictGenerator(TestCase):
    def setUp(self):
        self.random_ordered_dict_generator = RandomOrderedDictGenerator()

    def test_generate_ordered_dict_ok(self):
        random_ordered_dict = self.random_ordered_dict_generator.generate()

        self.assertIsInstance(random_ordered_dict, OrderedDict)
        keys = [*random_ordered_dict]
        self.assertIsInstance(keys[0], defaults.DEFAULT_KEY_TYPE)
        values = list(random_ordered_dict.values())
        self.assertIsInstance(values[0], defaults.DEFAULT_VALUE_TYPE)
        self.assertEqual(len(random_ordered_dict), defaults.MAX_ORDERED_DICT_LENGTH)

    def test_generate_ordered_dict_correct_max_length_ok(self):
        max_length = 20
        random_ordered_dict = self.random_ordered_dict_generator.generate(
            **{defaults.MAX_LENGTH_ARG: max_length}
        )

        self.assertIsInstance(random_ordered_dict, OrderedDict)
        self.assertEqual(len(random_ordered_dict), max_length)

    def test_generate_ordered_dict_incorrect_max_length_ko(self):
        with self.assertRaises(TypeError):
            self.random_ordered_dict_generator.generate(
                **{defaults.MAX_LENGTH_ARG: "asd"}
            )

    def test_generate_ordered_dict_incorrect_value_generator_ko(self):
        with self.assertRaises(KeyError):
            self.random_ordered_dict_generator.generate(
                **{defaults.VALUE_TYPE_ARG: None}
            )

    def test_generate_ordered_dict_incorrect_key_generator_ko(self):
        with self.assertRaises(KeyError):
            self.random_ordered_dict_generator.generate(
                **{defaults.KEY_TYPE_ARG: None}
            )
