import random
from pathlib import Path
from typing import List


class QuoteManager:
    def __init__(self, quote_dir: Path) -> None:
        self.quote_dir = quote_dir
        self.quotes = self._load_quotes()

    def random_quote(self) -> str:
        if not self.quotes:
            raise RuntimeError(f"No quotes found in {self.quote_dir}")
        return random.choice(self.quotes)

    def _load_quotes(self) -> List[str]:
        if not self.quote_dir.exists():
            return []

        quotes: List[str] = []
        for quote_path in sorted(self.quote_dir.glob("*.txt")):
            for line in quote_path.read_text(encoding="utf-8").splitlines():
                cleaned = line.strip()
                if cleaned and not cleaned.startswith("#"):
                    quotes.append(cleaned)
        return quotes
