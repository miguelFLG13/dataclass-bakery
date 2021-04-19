from pathlib import Path

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_generator import RandomGenerator
from dataclass_bakery.generators.random_str_generator import RandomStrGenerator


class RandomPathGenerator(RandomGenerator):
    def generate(self, *args, **kwargs) -> Path:
        generator = RandomStrGenerator()
        max_path_length = kwargs.get(defaults.MAX_LENGTH_ARG, defaults.MAX_PATH_LENGTH)
        folders = [generator.generate() for _ in range(max_path_length)]
        random_path = "/".join(folders)
        return Path(random_path)
