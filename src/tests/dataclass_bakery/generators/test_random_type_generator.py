from unittest import TestCase

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_type_generator import RandomTypeGenerator


class TestRandomTypeGenerator(TestCase):
    def setUp(self):
        self.random_type_generator = RandomTypeGenerator()

    def test_generate_type_default_ok(self):
        random_type = self.random_type_generator.generate()
        self.assertEqual(random_type, defaults.DEFAULT_VALUE_TYPE)

    def test_generate_type_correct_value_type_ok(self):
        random_type = self.random_type_generator.generate(
            **{defaults.VALUE_TYPE_ARG: str}
        )
        self.assertEqual(random_type, str)
