import argparse
import sys
import time
from itertools import cycle
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.config import BOOT_LINES, AppConfig
from src.display.base import Display
from src.display.oled_display import OledDisplay
from src.display.terminal_display import TerminalDisplay
from src.quote_manager import QuoteManager
from src.renderer import Renderer
from src.scene_manager import Animation, SceneManager


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run SUPER_COMPUTER.")
    parser.add_argument(
        "--display",
        choices=("terminal", "oled"),
        default="terminal",
        help="Display backend to use.",
    )
    parser.add_argument(
        "--cycles",
        type=int,
        default=None,
        help="Number of animation/message cycles to run. Defaults to forever.",
    )
    parser.add_argument(
        "--animation-duration",
        type=float,
        default=None,
        help="Seconds to play each animation.",
    )
    parser.add_argument(
        "--quote-duration",
        type=float,
        default=None,
        help="Seconds to show each quote.",
    )
    parser.add_argument(
        "--frame-delay",
        type=float,
        default=None,
        help="Seconds between animation frames.",
    )
    return parser.parse_args()


def build_display(name: str, config: AppConfig) -> Display:
    if name == "terminal":
        return TerminalDisplay(config.canvas_width, config.canvas_height)
    return OledDisplay(config.canvas_width, config.canvas_height)


def show_for(display: Display, lines: list[str], seconds: float) -> None:
    display.render(lines)
    time.sleep(seconds)


def play_animation(
    display: Display,
    renderer: Renderer,
    animation: Animation,
    duration: float,
    frame_delay: float,
) -> None:
    end_time = time.monotonic() + duration
    for raw_frame in cycle(animation.frames):
        display.render(renderer.frame(raw_frame))
        time.sleep(frame_delay)
        if time.monotonic() >= end_time:
            break


def main() -> int:
    args = parse_args()
    config = AppConfig()
    animation_duration = args.animation_duration or config.animation_duration_seconds
    quote_duration = args.quote_duration or config.quote_duration_seconds
    frame_delay = args.frame_delay or config.frame_delay_seconds

    display = build_display(args.display, config)
    renderer = Renderer(config.canvas_width, config.canvas_height)
    scenes = SceneManager(config.animation_dir)
    quotes = QuoteManager(config.quote_dir)

    try:
        display.start()
    except RuntimeError as error:
        print(f"SUPER_COMPUTER: {error}", file=sys.stderr)
        return 1

    try:
        show_for(display, renderer.boot(BOOT_LINES), config.boot_duration_seconds)

        completed_cycles = 0
        while args.cycles is None or completed_cycles < args.cycles:
            play_animation(
                display,
                renderer,
                scenes.random_animation(),
                animation_duration,
                frame_delay,
            )
            show_for(display, renderer.message(quotes.random_quote()), quote_duration)
            completed_cycles += 1
    except KeyboardInterrupt:
        pass
    finally:
        display.stop()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
