from abc import ABC, abstractmethod
from typing import Any


class RandomGenerator(ABC):
    @abstractmethod
    def generate(self, *args, **kwargs) -> Any:
        pass
