from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_generator import RandomGenerator


class RandomTypeGenerator(RandomGenerator):
    """
    Class to generate a random value for a ``Type[X]``/``type[X]`` field:
    ``Type[X]`` means "a class that is X or a subclass of X", so the most
    sensible random value is the class itself.
    """

    def generate(self, *args, **kwargs) -> type:
        default_value_type = kwargs.get(
            defaults.DEFAULT_VALUE_TYPE_ARG, defaults.DEFAULT_VALUE_TYPE
        )
        return kwargs.get(defaults.VALUE_TYPE_ARG, default_value_type)
