from ipaddress import IPv6Address
from unittest import TestCase

from dataclass_bakery.generators.random_ipv6_generator import RandomIpv6Generator


class TestRandomIpv6Generator(TestCase):
    def setUp(self):
        self.random_ipv6_generator = RandomIpv6Generator()

    def test_generate_ipv6_ok(self):
        random_ip = self.random_ipv6_generator.generate()
        self.assertIsInstance(random_ip, IPv6Address)
