from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_generator import RandomGenerator


class RandomDictGenerator(RandomGenerator):
    """
    Class to generate random dict
    """

    def generate(self, *args, **kwargs) -> dict:
        max_length = defaults.MAX_DICT_LENGTH

        default_key_type = defaults.DEFAULT_KEY_TYPE
        default_value_type = defaults.DEFAULT_VALUE_TYPE

        key_type = kwargs.get("key_type", default_key_type)
        value_type = kwargs.get("value_type", default_value_type)

        key_generator = defaults.TYPING_GENERATORS[key_type]()
        value_generator = defaults.TYPING_GENERATORS[value_type]()

        random_dict = {}
        for _ in range(max_length):
            dict_key = key_generator.generate()
            dict_value = value_generator.generate()
            random_dict[dict_key] = dict_value

        return random_dict
