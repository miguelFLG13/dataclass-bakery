from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_generator import RandomGenerator


class RandomListGenerator(RandomGenerator):
    """
    Class to generate random list
    """

    def generate(self, *args, **kwargs) -> list:
        max_length = defaults.MAX_LIST_LENGTH

        default_value_type = defaults.DEFAULT_VALUE_TYPE

        value_type = kwargs.get("value_type", default_value_type)
        generator = defaults.TYPING_GENERATORS[value_type]()

        random_list = []
        for _ in range(max_length):
            list_value = generator.generate()
            random_list.append(list_value)

        return random_list
