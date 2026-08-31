import random
from ipaddress import IPv6Address

from dataclass_bakery.generators.random_generator import RandomGenerator


class RandomIpv6Generator(RandomGenerator):
    """
    Class to generate random IPv6Address
    """

    def generate(self, *args, **kwargs) -> IPv6Address:
        hex_digits = "0123456789abcdef"
        groups = [
            "".join(random.choices(hex_digits, k=4)) for _ in range(8)
        ]
        random_ip = ":".join(groups)
        return IPv6Address(random_ip)
