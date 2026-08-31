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
        types_seen = set()
        for _ in range(60):
            random_data_class = self.random_data_class_generator.generate(
                testing_dataclasses.StuffUnion
            )
            self.assertIsInstance(random_data_class, testing_dataclasses.StuffUnion)
            self.assertIsInstance(random_data_class.item_union, (float, complex))
            types_seen.add(type(random_data_class.item_union))
        self.assertEqual(types_seen, {float, complex})

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

    def test_generate_dataclass_enum_typing_ok(self):
        random_data_class = self.random_data_class_generator.generate(
            testing_dataclasses.StuffEnum
        )
        self.assertIsInstance(random_data_class, testing_dataclasses.StuffEnum)
        self.assertIsInstance(
            random_data_class.item_enum, testing_dataclasses.Color
        )

    def test_generate_dataclass_optional_enum_typing_ok(self):
        random_data_class = self.random_data_class_generator.generate(
            testing_dataclasses.StuffOptionalEnum
        )
        self.assertIsInstance(
            random_data_class, testing_dataclasses.StuffOptionalEnum
        )
        self.assertIsInstance(
            random_data_class.item_optional_enum, testing_dataclasses.Color
        )

    def test_generate_dataclass_multi_union_typing_ok(self):
        types_seen = set()
        for _ in range(60):
            random_data_class = self.random_data_class_generator.generate(
                testing_dataclasses.StuffMultiUnion
            )
            self.assertIsInstance(
                random_data_class, testing_dataclasses.StuffMultiUnion
            )
            types_seen.add(type(random_data_class.item_multi_union))
        self.assertEqual(types_seen, {int, str, float})

    def test_generate_dataclass_nested_list_typing_ok(self):
        random_data_class = self.random_data_class_generator.generate(
            testing_dataclasses.StuffNestedList
        )
        self.assertIsInstance(random_data_class, testing_dataclasses.StuffNestedList)
        self.assertIsInstance(random_data_class.item_nested_list, list)
        self.assertIsInstance(random_data_class.item_nested_list[0], list)
        self.assertIsInstance(random_data_class.item_nested_list[0][0], int)

    def test_generate_dataclass_nested_dict_typing_ok(self):
        random_data_class = self.random_data_class_generator.generate(
            testing_dataclasses.StuffNestedDict
        )
        self.assertIsInstance(random_data_class, testing_dataclasses.StuffNestedDict)
        values = list(random_data_class.item_nested_dict.values())
        self.assertIsInstance(values[0], list)
        self.assertIsInstance(values[0][0], int)

    def test_generate_dataclass_named_tuple_typing_ok(self):
        random_data_class = self.random_data_class_generator.generate(
            testing_dataclasses.StuffNamedTuple
        )
        self.assertIsInstance(random_data_class, testing_dataclasses.StuffNamedTuple)
        self.assertIsInstance(
            random_data_class.item_named_tuple, testing_dataclasses.Point
        )
        self.assertIsInstance(random_data_class.item_named_tuple.x, int)
        self.assertIsInstance(random_data_class.item_named_tuple.y, int)

    def test_generate_dataclass_typed_dict_typing_ok(self):
        random_data_class = self.random_data_class_generator.generate(
            testing_dataclasses.StuffTypedDict
        )
        self.assertIsInstance(random_data_class, testing_dataclasses.StuffTypedDict)
        self.assertIsInstance(random_data_class.item_typed_dict, dict)
        self.assertIsInstance(random_data_class.item_typed_dict["name"], str)
        self.assertIsInstance(random_data_class.item_typed_dict["age"], int)

    def test_generate_dataclass_nested_ok(self):
        random_data_class = self.random_data_class_generator.generate(
            testing_dataclasses.StuffNested2
        )
        self.assertIsInstance(random_data_class, testing_dataclasses.StuffNested2)
        self.assertIsInstance(random_data_class.item, testing_dataclasses.StuffNested1)
        self.assertIsInstance(random_data_class.item.item, testing_dataclasses.Stuff)
        self.assertIsInstance(random_data_class.item.item.id, int)
