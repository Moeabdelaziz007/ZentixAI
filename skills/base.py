from abc import ABC, abstractmethod


class AbstractSkill(ABC):
    """Base interface for all ZeroSystem skills."""

    @abstractmethod
    def get_description(self):
        """Return a human readable description of the skill."""
        raise NotImplementedError

    @abstractmethod
    def execute(self, **kwargs):
        """Execute the skill and return a result dictionary."""
        raise NotImplementedError
