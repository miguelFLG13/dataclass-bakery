from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_generator import RandomGenerator


class RandomTupleGenerator(RandomGenerator):
    """
    Class to generate random tuple
    """

    def generate(self, *args, **kwargs) -> list:
        max_length = defaults.MAX_TUPLE_LENGTH

        default_value_type = defaults.DEFAULT_VALUE_TYPE

        value_type = kwargs.get("value_type", default_value_type)
        generator = defaults.TYPING_GENERATORS[value_type]()

        random_tuple = []
        for _ in range(max_length):
            tuple_value = generator.generate()
            random_tuple.append(tuple_value)

        return tuple(random_tuple)
