import tempfile
import unittest
from pathlib import Path

from src.scene_manager import SceneManager


class SceneManagerTest(unittest.TestCase):
    def test_loads_animation_folders_and_sorted_frames(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            animation_dir = Path(temp_dir)
            blink_dir = animation_dir / "blink"
            blink_dir.mkdir()
            (blink_dir / "frame_002.txt").write_text("two\n", encoding="utf-8")
            (blink_dir / "frame_001.txt").write_text("one\n", encoding="utf-8")

            manager = SceneManager(animation_dir)

        self.assertEqual(len(manager.animations), 1)
        self.assertEqual(manager.animations[0].name, "blink")
        self.assertEqual(manager.animations[0].frames, (("one",), ("two",)))

    def test_random_animation_fails_when_empty(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            manager = SceneManager(Path(temp_dir))

        with self.assertRaisesRegex(RuntimeError, "No animations found"):
            manager.random_animation()


if __name__ == "__main__":
    unittest.main()
