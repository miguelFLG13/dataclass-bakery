from unittest import TestCase

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_data_class_generator import (
    RandomDataClassGenerator,
)
from dataclass_bakery.generators.random_float_generator import RandomFloatGenerator
from tests import testing_dataclasses


class TestRandomDataClassGenerator(TestCase):
    def setUp(self):
        self.random_data_class_generator = RandomDataClassGenerator()

    def test_generate_dataclass_ok(self):
        random_data_class = self.random_data_class_generator.generate(
            testing_dataclasses.Stuff
        )
        self.assertIsInstance(random_data_class, testing_dataclasses.Stuff)

    def test_generate_dataclass_correct_value_fix_ok(self):
        value = 123456789
        random_data_class = self.random_data_class_generator.generate(
            testing_dataclasses.Stuff, **{"id": {defaults.FIXED_VALUE_ARG: value}}
        )
        self.assertIsInstance(random_data_class, testing_dataclasses.Stuff)
        self.assertEqual(random_data_class.id, value)

    def test_generate_dataclass_correct_generator_ok(self):
        random_data_class = self.random_data_class_generator.generate(
            testing_dataclasses.Stuff,
            **{"id": {defaults.GENERATOR_ARG: RandomFloatGenerator}}
        )
        self.assertIsInstance(random_data_class, testing_dataclasses.Stuff)
        self.assertIsInstance(random_data_class.id, float)

    def test_generate_dataclass_incorrect_generator_ko(self):
        with self.assertRaises(TypeError):
            self.random_data_class_generator.generate(
                testing_dataclasses.Stuff, **{"id": {defaults.GENERATOR_ARG: None}}
            )

    def test_generate_dataclass_union_typing_ok(self):
        random_data_class = self.random_data_class_generator.generate(
            testing_dataclasses.StuffUnion
        )
        self.assertIsInstance(random_data_class, testing_dataclasses.StuffUnion)
        self.assertIsInstance(random_data_class.item_union, float)

    def test_generate_dataclass_optional_typing_ok(self):
        random_data_class = self.random_data_class_generator.generate(
            testing_dataclasses.StuffOptional
        )
        self.assertIsInstance(random_data_class, testing_dataclasses.StuffOptional)
        self.assertIsInstance(random_data_class.item_optional, float)

    def test_generate_dataclass_literal_typing_ok(self):
        random_data_class = self.random_data_class_generator.generate(
            testing_dataclasses.StuffLiteral
        )
        self.assertIsInstance(random_data_class, testing_dataclasses.StuffLiteral)
        self.assertTrue(random_data_class.item_literal in ["a", "s", "d"])

    def test_generate_dataclass_dict_typing_ok(self):
        random_data_class = self.random_data_class_generator.generate(
            testing_dataclasses.StuffDict
        )
        self.assertIsInstance(random_data_class, testing_dataclasses.StuffDict)
        key = list(random_data_class.item_dict.keys())[0]
        self.assertIsInstance(key, float)
        value = list(random_data_class.item_dict.values())[0]
        self.assertIsInstance(value, complex)

    def test_generate_dataclass_list_typing_ok(self):
        random_data_class = self.random_data_class_generator.generate(
            testing_dataclasses.StuffList
        )
        self.assertIsInstance(random_data_class, testing_dataclasses.StuffList)
        self.assertIsInstance(random_data_class.item_list, list)

    def test_generate_dataclass_tuple_typing_ok(self):
        random_data_class = self.random_data_class_generator.generate(
            testing_dataclasses.StuffTuple
        )
        self.assertIsInstance(random_data_class, testing_dataclasses.StuffTuple)
        self.assertIsInstance(random_data_class.item_tuple, tuple)

    def test_generate_dataclass_nested_ok(self):
        random_data_class = self.random_data_class_generator.generate(
            testing_dataclasses.StuffNested2
        )
        self.assertIsInstance(random_data_class, testing_dataclasses.StuffNested2)
        self.assertIsInstance(random_data_class.item, testing_dataclasses.StuffNested1)
        self.assertIsInstance(random_data_class.item.item, testing_dataclasses.Stuff)
        self.assertIsInstance(random_data_class.item.item.id, int)
