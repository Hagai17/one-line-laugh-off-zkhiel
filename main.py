"""One-Line Laugh-Off entry.

The line is built as a three-beat escalation: one hour of grandpa dog-sitting
returns the dog with (1) a savings account, (2) a bedtime, and (3) a referral
to his accountant — the last beat is the laugh. It won local duels, run with
the kit's published judge brief in both orders, against the strongest visible
field lines (see candidates.md).
"""

import os

SETUP = "Dad watched the dog for one hour and returned him with "
BEATS = ["a savings account", "a bedtime", "a referral to his accountant"]

OUTPUT_PATH = "/output/entry.txt"


def render() -> str:
    """Assemble the entry and hold it to the competition gate (1-200 chars)."""
    text = SETUP + ", ".join(BEATS[:-1]) + ", and " + BEATS[-1] + "."
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, gate is 1-200"
    assert text.strip(), "entry must not be only whitespace"
    return text


def main() -> None:
    line = render()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(line)
    print(line)


if __name__ == "__main__":
    main()
