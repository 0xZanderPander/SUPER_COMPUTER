from dataclasses import dataclass
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class AppConfig:
    assets_dir: Path = PROJECT_ROOT / "assets"
    animation_dir: Path = assets_dir / "animations"
    quote_dir: Path = assets_dir / "quotes"
    canvas_width: int = 21
    canvas_height: int = 8
    frame_delay_seconds: float = 0.45
    animation_duration_seconds: float = 12.0
    quote_duration_seconds: float = 4.0
    boot_duration_seconds: float = 2.0


BOOT_LINES = [
    "SUPER_COMPUTER",
    "v0.1",
    "",
    "offline system",
    "warming phosphor...",
]
