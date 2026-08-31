import random

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_generator import RandomGenerator


class RandomBytearrayGenerator(RandomGenerator):
    """
    Class to generate random bytearray
    """

    def generate(self, *args, **kwargs) -> bytearray:
        max_length = kwargs.get(defaults.MAX_LENGTH_ARG, defaults.MAX_BYTEARRAY_LENGTH)
        random_bytearray = bytearray(random.randbytes(max_length))
        return random_bytearray
