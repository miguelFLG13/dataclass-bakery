from collections import Counter
from unittest import TestCase

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_counter_generator import (
    RandomCounterGenerator,
)


class TestRandomCounterGenerator(TestCase):
    def setUp(self):
        self.random_counter_generator = RandomCounterGenerator()

    def test_generate_counter_ok(self):
        random_counter = self.random_counter_generator.generate()

        self.assertIsInstance(random_counter, Counter)
        self.assertTrue(len(random_counter) <= defaults.MAX_COUNTER_LENGTH)
        item = next(iter(random_counter))
        self.assertIsInstance(item, defaults.DEFAULT_KEY_TYPE)
        self.assertIsInstance(random_counter[item], int)

    def test_generate_counter_changing_item_generator_ok(self):
        item_type = float
        random_counter = self.random_counter_generator.generate(
            **{defaults.VALUE_TYPE_ARG: item_type}
        )

        self.assertIsInstance(random_counter, Counter)
        item = next(iter(random_counter))
        self.assertIsInstance(item, item_type)

    def test_generate_counter_incorrect_generator_ko(self):
        with self.assertRaises(KeyError):
            self.random_counter_generator.generate(**{defaults.VALUE_TYPE_ARG: None})
