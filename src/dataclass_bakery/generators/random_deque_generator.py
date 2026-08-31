from collections import deque

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators import random_data_class_generator
from dataclass_bakery.generators.random_generator import RandomGenerator


class RandomDequeGenerator(RandomGenerator):
    """
    Class to generate random deque
    """

    def generate(self, *args, **kwargs) -> deque:
        max_length = kwargs.get(defaults.MAX_LENGTH_ARG, defaults.MAX_DEQUE_LENGTH)

        default_value_type = kwargs.get(
            defaults.DEFAULT_VALUE_TYPE_ARG, defaults.DEFAULT_VALUE_TYPE
        )

        value_type = kwargs.get(defaults.VALUE_TYPE_ARG, default_value_type)

        random_deque = deque()
        for _ in range(max_length):
            deque_value = random_data_class_generator.generate_value(value_type)
            random_deque.append(deque_value)

        return random_deque
