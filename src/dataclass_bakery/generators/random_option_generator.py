import random
from typing import Any

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_generator import RandomGenerator


class RandomOptionGenerator(RandomGenerator):
    """
    Class to generate random option
    """

    def generate(self, *args, **kwargs) -> Any:
        START_POSITION = 1
        options = kwargs[defaults.OPTIONS_ARG]
        positions = len(options) - 1
        random_position = random.randint(START_POSITION, positions)
        return options[random_position]
