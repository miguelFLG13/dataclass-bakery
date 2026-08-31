from unittest import TestCase

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_enum_generator import RandomEnumGenerator
from tests.testing_dataclasses import Color


class TestRandomEnumGenerator(TestCase):
    def setUp(self):
        self.random_enum_generator = RandomEnumGenerator()

    def test_generate_enum_ok(self):
        random_enum = self.random_enum_generator.generate(
            **{defaults.ENUM_CLASS_ARG: Color}
        )
        self.assertIsInstance(random_enum, Color)
        self.assertIn(random_enum, list(Color))

    def test_generate_enum_incorrect_class_ko(self):
        with self.assertRaises(KeyError):
            self.random_enum_generator.generate()
