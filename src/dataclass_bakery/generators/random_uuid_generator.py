from uuid import UUID, uuid4

from dataclass_bakery.generators.random_generator import RandomGenerator


class RandomUuidGenerator(RandomGenerator):
    """
    Class to generate uuid
    """

    def generate(self, *args, **kwargs) -> UUID:
        return uuid4()
