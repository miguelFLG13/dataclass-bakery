from unittest import TestCase

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_bytes_generator import RandomBytesGenerator


class TestRandomBytesGenerator(TestCase):
    def setUp(self):
        self.random_bytes_generator = RandomBytesGenerator()

    def test_generate_bytes_ok(self):
        random_bytes = self.random_bytes_generator.generate()

        self.assertIsInstance(random_bytes, bytes)
        self.assertEqual(len(random_bytes), defaults.MAX_BYTES_LENGTH)

    def test_generate_bytes_correct_max_length_ok(self):
        max_length = 20
        random_bytes = self.random_bytes_generator.generate(
            **{defaults.MAX_LENGTH_ARG: max_length}
        )

        self.assertIsInstance(random_bytes, bytes)
        self.assertEqual(len(random_bytes), max_length)

    def test_generate_bytes_incorrect_max_length_ko(self):
        with self.assertRaises(TypeError):
            self.random_bytes_generator.generate(**{defaults.MAX_LENGTH_ARG: "asd"})
