from unittest import TestCase

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_bytearray_generator import (
    RandomBytearrayGenerator,
)


class TestRandomBytearrayGenerator(TestCase):
    def setUp(self):
        self.random_bytearray_generator = RandomBytearrayGenerator()

    def test_generate_bytearray_ok(self):
        random_bytearray = self.random_bytearray_generator.generate()

        self.assertIsInstance(random_bytearray, bytearray)
        self.assertEqual(len(random_bytearray), defaults.MAX_BYTEARRAY_LENGTH)

    def test_generate_bytearray_correct_max_length_ok(self):
        max_length = 20
        random_bytearray = self.random_bytearray_generator.generate(
            **{defaults.MAX_LENGTH_ARG: max_length}
        )

        self.assertIsInstance(random_bytearray, bytearray)
        self.assertEqual(len(random_bytearray), max_length)

    def test_generate_bytearray_incorrect_max_length_ko(self):
        with self.assertRaises(TypeError):
            self.random_bytearray_generator.generate(
                **{defaults.MAX_LENGTH_ARG: "asd"}
            )
