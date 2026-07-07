import unittest

from src.renderer import Renderer


class RendererTest(unittest.TestCase):
    def test_frame_centers_and_pads_lines(self) -> None:
        renderer = Renderer(width=5, height=3)

        self.assertEqual(renderer.frame(["x"]), ["", "  x  ", ""])

    def test_message_wraps_inside_canvas(self) -> None:
        renderer = Renderer(width=8, height=4)

        self.assertEqual(renderer.message("hello world"), ["", ' "hello ', ' world" ', ""])

    def test_frame_trims_to_canvas(self) -> None:
        renderer = Renderer(width=4, height=2)

        self.assertEqual(renderer.frame(["abcdef", "xy"]), ["abcd", " xy "])


if __name__ == "__main__":
    unittest.main()
