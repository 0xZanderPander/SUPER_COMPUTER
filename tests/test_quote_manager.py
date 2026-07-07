import tempfile
import unittest
from pathlib import Path

from src.quote_manager import QuoteManager


class QuoteManagerTest(unittest.TestCase):
    def test_loads_non_empty_non_comment_lines(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            quote_dir = Path(temp_dir)
            (quote_dir / "quotes.txt").write_text(
                "\n# ignored\nFirst quote\n  Second quote  \n",
                encoding="utf-8",
            )

            manager = QuoteManager(quote_dir)

        self.assertEqual(manager.quotes, ["First quote", "Second quote"])

    def test_random_quote_fails_when_empty(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            manager = QuoteManager(Path(temp_dir))

        with self.assertRaisesRegex(RuntimeError, "No quotes found"):
            manager.random_quote()


if __name__ == "__main__":
    unittest.main()
