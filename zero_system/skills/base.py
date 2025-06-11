from abc import ABC, abstractmethod

class AbstractSkill(ABC):
    """Base interface for all skills."""

    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def execute(self, **kwargs):
        pass
