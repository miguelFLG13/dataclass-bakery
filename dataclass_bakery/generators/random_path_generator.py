from pathlib import Path

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_generator import RandomGenerator
from dataclass_bakery.generators.random_str_generator import RandomStrGenerator


class RandomPathGenerator(RandomGenerator):
    def generate(self, *args, **kwargs) -> Path:
        generator = RandomStrGenerator()
        folders = [generator.generate() for _ in range(defaults.MAX_PATH_LENGTH)]
        random_path = "/".join(folders)
        return random_path
