from ipaddress import IPv4Address
from unittest import TestCase

from dataclass_bakery.generators.random_ipv4_generator import RandomIpv4Generator


class TestRandomIpv4Generator(TestCase):
    def setUp(self):
        self.random_ipv4_generator = RandomIpv4Generator()

    def test_generate_ipv4_ok(self):
        random_ip = self.random_ipv4_generator.generate()
        self.assertIsInstance(random_ip, IPv4Address)
