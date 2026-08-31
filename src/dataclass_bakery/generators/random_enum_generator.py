import random

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_generator import RandomGenerator


class RandomEnumGenerator(RandomGenerator):
    """
    Class to generate a random member of an Enum (or IntEnum, StrEnum,
    Flag, IntFlag, ...) class
    """

    def generate(self, *args, **kwargs):
        enum_class = kwargs[defaults.ENUM_CLASS_ARG]
        members = list(enum_class)
        return random.choice(members)
