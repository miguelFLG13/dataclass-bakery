import random, string

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_generator import RandomGenerator


class RandomStrGenerator(RandomGenerator):
    """
    Class to generate random string
    """

    def generate(self, *args, **kwargs) -> str:
        max_length = kwargs.get(defaults.MAX_LENGTH_ARG, defaults.MAX_STR_LENGTH)
        characters = string.ascii_uppercase + string.ascii_lowercase
        random_choices = random.choices(characters, k=max_length)
        random_str = "".join(random_choices)
        return random_str
