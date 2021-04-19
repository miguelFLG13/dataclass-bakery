from unittest import TestCase

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_option_generator import RandomOptionGenerator


class TestRandomOptionGenerator(TestCase):
    def setUp(self):
        self.random_option_generator = RandomOptionGenerator()
        self.options = ["a", "s", "d"]

    def test_generate_option_ok(self):
        random_option = self.random_option_generator.generate(
            **{defaults.OPTIONS_ARG: self.options}
        )
        self.assertTrue(random_option in self.options)
