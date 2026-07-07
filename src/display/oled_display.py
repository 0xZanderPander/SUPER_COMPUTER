from typing import Sequence

from src.display.base import Display


OLED_NOT_READY_MESSAGE = (
    "OLED output is not implemented in SUPER_COMPUTER v0.1. "
    "Use '--display terminal' for this milestone."
)


class OledDisplay(Display):
    """Placeholder for the future SSD1306 backend.

    Hardware libraries are intentionally not imported here yet, so terminal
    development works on machines without Raspberry Pi OLED dependencies.
    """

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def start(self) -> None:
        raise RuntimeError(OLED_NOT_READY_MESSAGE)

    def render(self, lines: Sequence[str]) -> None:
        raise RuntimeError(OLED_NOT_READY_MESSAGE)

    def stop(self) -> None:
        pass
