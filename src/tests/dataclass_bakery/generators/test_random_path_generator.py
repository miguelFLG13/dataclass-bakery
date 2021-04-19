from pathlib import Path
from unittest import TestCase

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_path_generator import RandomPathGenerator


class TestRandomPathGenerator(TestCase):
    def setUp(self):
        self.random_path_generator = RandomPathGenerator()

    def test_generate_path_ok(self):
        random_path = self.random_path_generator.generate()
        self.assertIsInstance(random_path, Path)
        random_path_count = str(random_path).count("/") + 1
        self.assertEqual(random_path_count, defaults.MAX_PATH_LENGTH)

    def test_generate_path_correct_max_length_ok(self):
        path_length = 10
        random_path = self.random_path_generator.generate(
            **{defaults.MAX_LENGTH_ARG: path_length}
        )
        self.assertIsInstance(random_path, Path)
        random_path_count = str(random_path).count("/") + 1
        self.assertEqual(random_path_count, path_length)

    def test_generate_int_incorrect_max_length_ko(self):
        with self.assertRaises(TypeError):
            self.random_path_generator.generate(**{defaults.MAX_LENGTH_ARG: "asd"})
