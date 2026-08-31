import random

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_generator import RandomGenerator


class RandomBytesGenerator(RandomGenerator):
    """
    Class to generate random bytes
    """

    def generate(self, *args, **kwargs) -> bytes:
        max_length = kwargs.get(defaults.MAX_LENGTH_ARG, defaults.MAX_BYTES_LENGTH)
        random_bytes = random.randbytes(max_length)
        return random_bytes
