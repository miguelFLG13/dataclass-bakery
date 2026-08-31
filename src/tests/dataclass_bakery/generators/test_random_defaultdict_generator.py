from collections import defaultdict
from unittest import TestCase

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_defaultdict_generator import (
    RandomDefaultdictGenerator,
)


class TestRandomDefaultdictGenerator(TestCase):
    def setUp(self):
        self.random_defaultdict_generator = RandomDefaultdictGenerator()

    def test_generate_defaultdict_ok(self):
        random_defaultdict = self.random_defaultdict_generator.generate()

        self.assertIsInstance(random_defaultdict, defaultdict)
        keys = [*random_defaultdict]
        self.assertIsInstance(keys[0], defaults.DEFAULT_KEY_TYPE)
        values = list(random_defaultdict.values())
        self.assertIsInstance(values[0], defaults.DEFAULT_VALUE_TYPE)
        self.assertEqual(len(random_defaultdict), defaults.MAX_DEFAULTDICT_LENGTH)

    def test_generate_defaultdict_missing_key_uses_factory_ok(self):
        random_defaultdict = self.random_defaultdict_generator.generate(
            **{defaults.VALUE_TYPE_ARG: int}
        )
        self.assertEqual(random_defaultdict["a missing key"], 0)

    def test_generate_defaultdict_correct_max_length_ok(self):
        max_length = 20
        random_defaultdict = self.random_defaultdict_generator.generate(
            **{defaults.MAX_LENGTH_ARG: max_length}
        )
        self.assertEqual(len(random_defaultdict), max_length)

    def test_generate_defaultdict_incorrect_value_generator_ko(self):
        with self.assertRaises(KeyError):
            self.random_defaultdict_generator.generate(
                **{defaults.VALUE_TYPE_ARG: "not a type"}
            )
