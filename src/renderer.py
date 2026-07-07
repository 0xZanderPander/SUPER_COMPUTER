from collections.abc import Sequence
from textwrap import wrap


class Renderer:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def frame(self, raw_lines: Sequence[str]) -> list[str]:
        lines = [line.rstrip("\n") for line in raw_lines]
        return self._center_block(lines)

    def message(self, text: str) -> list[str]:
        wrapped = wrap(text, width=self.width - 2) or [""]
        if len(wrapped) == 1:
            quoted = [f'"{wrapped[0]}"']
        else:
            quoted = [f'"{line}' if index == 0 else line for index, line in enumerate(wrapped)]
            quoted[-1] = f'{quoted[-1]}"'
        return self._center_block(quoted)

    def boot(self, lines: Sequence[str]) -> list[str]:
        return self._center_block(lines)

    def _center_block(self, lines: Sequence[str]) -> list[str]:
        trimmed = [line[: self.width] for line in lines]
        visible = trimmed[: self.height]
        top_padding = max((self.height - len(visible)) // 2, 0)
        output = [""] * top_padding
        output.extend(line.center(self.width) for line in visible)
        output.extend([""] * max(self.height - len(output), 0))
        return output[: self.height]
