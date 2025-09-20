from abc import ABC, abstractmethod
from typing import Any, Dict

class BaseTemplate(ABC):
    @abstractmethod
    def draw(self, **kwargs: Any) -> str:
        pass
