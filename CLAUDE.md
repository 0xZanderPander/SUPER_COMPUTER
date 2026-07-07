# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

SUPER_COMPUTER is a tiny offline Raspberry Pi desk object driving an SSD1306 I2C OLED display. It loops forever between handcrafted ASCII animations and short quotes, retro-terminal mood, no networked features. v0.1 (current milestone) only implements a terminal simulation of the display for macOS development; the real OLED backend is not yet implemented.

Explicitly out of scope (do not add): Wi-Fi, APIs, AI, buttons, menus, sensors, clock/date display, database.

## Commands

Run in terminal simulation mode:

```sh
python3 src/main.py --display terminal
```

Quick smoke test (single cycle):

```sh
python3 src/main.py --display terminal --cycles 1 --animation-duration 2
```

Useful flags: `--cycles`, `--animation-duration`, `--quote-duration`, `--frame-delay` (all override defaults in `src/config.py`).

Run tests (stdlib `unittest`, no pytest/test runner dependency — `requirements.txt` is intentionally empty beyond a comment):

```sh
python3 -m unittest discover -s tests
```

Run a single test file or case:

```sh
python3 -m unittest tests.test_scene_manager
python3 -m unittest tests.test_scene_manager.SceneManagerTest.test_random_animation_fails_when_empty
```

## Architecture

Everything is data-driven off two asset directories, loaded once at startup and then sampled randomly in the main loop (`src/main.py`):

- `assets/animations/<name>/frame_*.txt` — each subfolder is one animation; frames within it are loaded alphabetically by filename. `SceneManager` (`src/scene_manager.py`) walks these into immutable `Animation(name, frames)` records.
- `assets/quotes/*.txt` — one quote per non-empty, non-`#`-prefixed line, aggregated across all files. `QuoteManager` (`src/quote_manager.py`) loads and picks randomly.

The main loop in `src/main.py` is: boot screen → repeat forever (or `--cycles` times) { play a random animation for `animation_duration` seconds, cycling its frames every `frame_delay` seconds → show a random quote for `quote_duration` seconds }.

`Renderer` (`src/renderer.py`) is the only place that knows about the fixed canvas size (`config.canvas_width` x `config.canvas_height`, default 21x8 to approximate a 128x64 OLED at its font size). It centers animation frames, and word-wraps + quote-marks text for the quote screen, always producing exactly `height` lines clipped/padded to `width`.

Display backends implement the abstract `Display` (`src/display/base.py`: `start`/`render`/`stop`) and are selected via `--display`:
- `TerminalDisplay` — ANSI box-drawn simulation for macOS/dev.
- `OledDisplay` — placeholder that raises `RuntimeError` on `start()`/`render()`; intentionally has no hardware imports yet so terminal development works without Pi-specific dependencies. Real SSD1306 support is future work and should slot in here without touching `SceneManager`/`QuoteManager`/`Renderer`.

`src/config.py` centralizes all tunables (`AppConfig` dataclass) and the boot-screen text (`BOOT_LINES`); CLI flags in `main.py` override these defaults when provided.

## Adding content

- New animation: create `assets/animations/<name>/` with `frame_001.txt`, `frame_002.txt`, etc. (alphabetical load order, keep within the 21x8 canvas).
- New quotes: add a `.txt` file under `assets/quotes/`, one quote per line, `#` for comments.

No code changes are needed for either — both managers pick these up automatically from disk.
