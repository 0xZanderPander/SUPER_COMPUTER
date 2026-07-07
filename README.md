# SUPER_COMPUTER v0.1

SUPER_COMPUTER is a tiny offline Raspberry Pi desk object for an SSD1306 I2C OLED display. It loops forever between handcrafted ASCII animations and short quotes, with a retro terminal mood and no networked features.

This first milestone implements terminal simulation mode for macOS development.

## Scope

- No Wi-Fi features
- No APIs
- No AI
- No buttons
- No menus
- No sensors
- No clock/date display
- No database

## Hardware Target

- Original Raspberry Pi Model A
- SSD1306 I2C OLED display
- 8GB SD card
- Python 3
- Raspberry Pi OS Lite

## Run On macOS

```sh
python src/main.py --display terminal
```

If your macOS shell does not have a `python` alias:

```sh
python3 src/main.py --display terminal
```

Stop with `Ctrl+C`.

For a quick smoke test:

```sh
python src/main.py --display terminal --cycles 1 --animation-duration 2
```

## Project Layout

```text
src/
  main.py
  config.py
  renderer.py
  scene_manager.py
  quote_manager.py
  display/
    base.py
    terminal_display.py
    oled_display.py
assets/
  animations/
  quotes/
docs/
```

## Adding Animations

Create a folder under `assets/animations/` and add frame files:

```text
assets/animations/my_animation/
  frame_001.txt
  frame_002.txt
  frame_003.txt
```

Frames are loaded alphabetically. Keep them small; the terminal simulation uses a tiny 21x8 character canvas to approximate a 128x64 OLED.

## Adding Quotes

Add plain text files under `assets/quotes/`. Each non-empty line is one possible quote. Lines beginning with `#` are ignored.

## OLED Status

`src/display/oled_display.py` is intentionally a placeholder in v0.1. Hardware-specific code will be added in a later milestone without changing the scene or quote loading logic.
