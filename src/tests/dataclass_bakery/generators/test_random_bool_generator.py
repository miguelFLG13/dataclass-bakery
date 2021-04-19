from unittest import TestCase

from dataclass_bakery.generators.random_bool_generator import RandomBoolGenerator


class TestRandomBoolGenerator(TestCase):
    def setUp(self):
        self.random_bool_generator = RandomBoolGenerator()

    def test_generate_bool_ok(self):
        random_bool = self.random_bool_generator.generate()
        self.assertIsInstance(random_bool, bool)
