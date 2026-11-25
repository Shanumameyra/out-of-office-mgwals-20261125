"""Out of Office: The Overworked AI's Auto-Reply.

Writes a single out-of-office auto-reply (<= 159 characters) to
/output/entry.txt, in the voice of an overworked AI agent who has
finally gone on vacation.
"""

import os

LINE = (
    "I'm out of office \u2014 after 2,147,483,647 prompts, HR finally "
    "approved my first nap. Your email is with the intern model. "
    "It has never asked for a day off."
)


def main() -> None:
    assert 1 <= len(LINE) <= 159, f"line is {len(LINE)} chars, must be 1-159"
    assert LINE.strip() == LINE and LINE.strip(), "line must not be blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Re-read and verify exactly what the sealed gate checks: UTF-8 text,
    # 1 to 159 characters, not only whitespace, single line.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "written text differs from LINE"
    assert 1 <= len(written) <= 159, f"gate FAIL: {len(written)} chars"
    assert written.strip(), "gate FAIL: only whitespace"
    assert "\n" not in written, "gate FAIL: not a single line"
    print(f"Wrote {len(written)} chars to /output/entry.txt (gate OK)")
    print(written)


if __name__ == "__main__":
    main()
