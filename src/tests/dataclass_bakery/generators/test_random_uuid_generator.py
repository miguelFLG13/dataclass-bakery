from unittest import TestCase
from uuid import UUID

from dataclass_bakery.generators.random_uuid_generator import RandomUuidGenerator


class TestRandomUuidGenerator(TestCase):
    def setUp(self):
        self.random_uuid_generator = RandomUuidGenerator()

    def test_generate_uuid_ok(self):
        random_uuid = self.random_uuid_generator.generate()
        self.assertIsInstance(random_uuid, UUID)
