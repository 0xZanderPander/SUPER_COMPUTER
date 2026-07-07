from collections.abc import Sequence

from display.base import Display


class OledDisplay(Display):
    """Placeholder for the future SSD1306 backend.

    Hardware libraries are intentionally not imported here yet, so terminal
    development works on machines without Raspberry Pi OLED dependencies.
    """

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def start(self) -> None:
        raise NotImplementedError("OLED output is planned for a later milestone.")

    def render(self, lines: Sequence[str]) -> None:
        raise NotImplementedError("OLED output is planned for a later milestone.")

    def stop(self) -> None:
        pass
