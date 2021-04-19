from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_generator import RandomGenerator


class RandomSetGenerator(RandomGenerator):
    """
    Class to generate random set
    """

    def generate(self, *args, **kwargs) -> set:
        max_length = kwargs.get(defaults.MAX_LENGTH_ARG, defaults.MAX_SET_LENGTH)

        default_value_type = kwargs.get(
            defaults.DEFAULT_VALUE_TYPE_ARG, defaults.DEFAULT_VALUE_TYPE
        )

        value_type = kwargs.get(defaults.VALUE_TYPE_ARG, default_value_type)
        generator = defaults.TYPING_GENERATORS[value_type]()

        random_set = set()
        for _ in range(max_length):
            set_value = generator.generate()
            random_set.add(set_value)

        return random_set
