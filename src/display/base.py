from abc import ABC, abstractmethod
from collections.abc import Sequence


class Display(ABC):
    width: int
    height: int

    @abstractmethod
    def start(self) -> None:
        """Prepare the display for drawing."""

    @abstractmethod
    def render(self, lines: Sequence[str]) -> None:
        """Draw a full frame of text."""

    @abstractmethod
    def stop(self) -> None:
        """Clean up display resources."""
