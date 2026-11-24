"""The Long Roast: Lawmakers and the File They Cannot Convert — make.fun entry.

Writes the entry line to output/entry.txt. Python stdlib only,
no network, fully deterministic.
"""

from pathlib import Path

ENTRY = (
    "They'll debate AI for six hours, ban crypto by lunch, and regulate the whole "
    "internet by dinner — then ask an intern to convert their speech to PDF because "
    "the big scary file 'won't open right.'"
)

OUTPUT_PATH = Path(__file__).resolve().parent / "output" / "entry.txt"

MAX_CHARS = 320  # the brief caps the roast at one sentence of 320 characters


def check_entry(text: str) -> str:
    """Return the entry unchanged, or raise if it breaks the brief."""
    if "\n" in text:
        raise ValueError("the roast must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"roast is {len(text)} chars, over the {MAX_CHARS} cap")
    if text.count(".") != 1 or not text.rstrip("'\"").endswith("."):
        raise ValueError("the roast must be exactly one sentence")
    return text


def main() -> None:
    line = check_entry(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
