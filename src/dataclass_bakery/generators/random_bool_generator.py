import random

from dataclass_bakery.generators.random_generator import RandomGenerator


class RandomBoolGenerator(RandomGenerator):
    """
    Class to generate random booleans
    """

    def generate(self, *args, **kwargs) -> bool:
        random_bit = random.getrandbits(1)
        return bool(random_bit)
