from unittest import TestCase

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_dict_generator import RandomDictGenerator
from dataclass_bakery.generators.random_str_generator import RandomStrGenerator


class TestRandomDictGenerator(TestCase):
    def setUp(self):
        self.random_dict_generator = RandomDictGenerator()

    def test_generate_dict_ok(self):
        random_dict = self.random_dict_generator.generate()

        self.assertIsInstance(random_dict, dict)
        keys = [*random_dict]
        self.assertIsInstance(keys[0], defaults.DEFAULT_KEY_TYPE)
        values = list(random_dict.values())
        self.assertIsInstance(values[0], defaults.DEFAULT_VALUE_TYPE)
        self.assertEqual(len(random_dict), defaults.MAX_DICT_LENGTH)

    def test_generate_dict_correct_max_length_ok(self):
        max_length = 20
        random_dict = self.random_dict_generator.generate(
            **{defaults.MAX_LENGTH_ARG: max_length}
        )

        self.assertIsInstance(random_dict, dict)
        keys = [*random_dict]
        self.assertIsInstance(keys[0], defaults.DEFAULT_KEY_TYPE)
        values = list(random_dict.values())
        self.assertIsInstance(values[0], defaults.DEFAULT_VALUE_TYPE)
        self.assertEqual(len(random_dict), max_length)

    def test_generate_dict_changing_values_generator_ok(self):
        key_type = float
        random_dict = self.random_dict_generator.generate(
            **{defaults.VALUE_TYPE_ARG: key_type}
        )

        self.assertIsInstance(random_dict, dict)
        values = list(random_dict.values())
        self.assertIsInstance(values[0], key_type)

    def test_generate_dict_changing_keys_generator_ok(self):
        key_type = float
        random_dict = self.random_dict_generator.generate(
            **{defaults.KEY_TYPE_ARG: key_type}
        )

        self.assertIsInstance(random_dict, dict)
        keys = [*random_dict]
        self.assertIsInstance(keys[0], key_type)

    def test_generate_dict_incorrect_max_length_ko(self):
        with self.assertRaises(TypeError):
            self.random_dict_generator.generate(**{defaults.MAX_LENGTH_ARG: "asd"})

    def test_generate_dict_incorrect_value_generator_ko(self):
        with self.assertRaises(KeyError):
            self.random_dict_generator.generate(**{defaults.VALUE_TYPE_ARG: None})

    def test_generate_dict_incorrect_key_generator_ko(self):
        with self.assertRaises(KeyError):
            self.random_dict_generator.generate(**{defaults.KEY_TYPE_ARG: None})
