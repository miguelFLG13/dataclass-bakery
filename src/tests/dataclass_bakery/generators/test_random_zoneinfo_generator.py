from unittest import TestCase
from zoneinfo import ZoneInfo

from dataclass_bakery.generators.random_zoneinfo_generator import (
    RandomZoneinfoGenerator,
)


class TestRandomZoneinfoGenerator(TestCase):
    def setUp(self):
        self.random_zoneinfo_generator = RandomZoneinfoGenerator()

    def test_generate_zoneinfo_ok(self):
        random_zoneinfo = self.random_zoneinfo_generator.generate()
        self.assertIsInstance(random_zoneinfo, ZoneInfo)
