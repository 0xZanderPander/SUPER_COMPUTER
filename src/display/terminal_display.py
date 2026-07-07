import sys
from typing import Sequence

from src.display.base import Display


class TerminalDisplay(Display):
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def start(self) -> None:
        self._hide_cursor()
        self._clear()

    def render(self, lines: Sequence[str]) -> None:
        self._clear()
        border = "+" + ("-" * self.width) + "+"
        print("\033[32m", end="")
        print(border)
        for index in range(self.height):
            line = lines[index] if index < len(lines) else ""
            print(f"|{line[: self.width].ljust(self.width)}|")
        print(border)
        print("\033[0m", end="")
        sys.stdout.flush()

    def stop(self) -> None:
        print("\033[0m", end="")
        self._show_cursor()
        sys.stdout.flush()

    def _clear(self) -> None:
        print("\033[2J\033[H", end="")

    def _hide_cursor(self) -> None:
        print("\033[?25l", end="")

    def _show_cursor(self) -> None:
        print("\033[?25h", end="")
