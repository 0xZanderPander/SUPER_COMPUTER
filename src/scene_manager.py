import random
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Animation:
    name: str
    frames: tuple[tuple[str, ...], ...]


class SceneManager:
    def __init__(self, animation_dir: Path) -> None:
        self.animation_dir = animation_dir
        self.animations = self._load_animations()

    def random_animation(self) -> Animation:
        if not self.animations:
            raise RuntimeError(f"No animations found in {self.animation_dir}")
        return random.choice(self.animations)

    def _load_animations(self) -> list[Animation]:
        if not self.animation_dir.exists():
            return []

        animations: list[Animation] = []
        for folder in sorted(path for path in self.animation_dir.iterdir() if path.is_dir()):
            frames = self._load_frames(folder)
            if frames:
                animations.append(Animation(name=folder.name, frames=tuple(frames)))
        return animations

    def _load_frames(self, folder: Path) -> list[tuple[str, ...]]:
        frames: list[tuple[str, ...]] = []
        for frame_path in sorted(folder.glob("*.txt")):
            frame_text = frame_path.read_text(encoding="utf-8").splitlines()
            frames.append(tuple(frame_text))
        return frames
