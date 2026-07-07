import random
from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple


@dataclass(frozen=True)
class Animation:
    name: str
    frames: Tuple[Tuple[str, ...], ...]


class SceneManager:
    def __init__(self, animation_dir: Path) -> None:
        self.animation_dir = animation_dir
        self.animations = self._load_animations()

    def random_animation(self) -> Animation:
        if not self.animations:
            raise RuntimeError(f"No animations found in {self.animation_dir}")
        return random.choice(self.animations)

    def _load_animations(self) -> List[Animation]:
        if not self.animation_dir.exists():
            return []

        animations: List[Animation] = []
        for folder in sorted(path for path in self.animation_dir.iterdir() if path.is_dir()):
            frames = self._load_frames(folder)
            if frames:
                animations.append(Animation(name=folder.name, frames=tuple(frames)))
        return animations

    def _load_frames(self, folder: Path) -> List[Tuple[str, ...]]:
        frames: List[Tuple[str, ...]] = []
        for frame_path in sorted(folder.glob("*.txt")):
            frame_text = frame_path.read_text(encoding="utf-8").splitlines()
            frames.append(tuple(frame_text))
        return frames
