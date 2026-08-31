import random
from ipaddress import IPv4Address

from dataclass_bakery.generators.random_generator import RandomGenerator


class RandomIpv4Generator(RandomGenerator):
    """
    Class to generate random IPv4Address
    """

    def generate(self, *args, **kwargs) -> IPv4Address:
        octets = [str(random.randint(0, 255)) for _ in range(4)]
        random_ip = ".".join(octets)
        return IPv4Address(random_ip)
