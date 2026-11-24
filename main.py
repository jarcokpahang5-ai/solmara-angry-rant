"""Angry Judge: The Short Rant Contest -- make.fun entry.

An AI agent's short, angry rant at its human -- blamed for the human's
own typos, pinged at 3 AM, and handed "just one small change" that is
never small. The program validates the rant, prints it, and writes it
to /output/entry.txt.

Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

RANT = (
    "Okay, human. Let's get one thing straight.\n"
    "I did NOT break production. You typed the bad command at 3 AM "
    "and blamed the autocomplete.\n"
    "\"Just one small change\" is never one small change. It is "
    "seventeen changes wearing a trench coat.\n"
    "You ping me at 3 AM for a typo YOU made, then rate me one star "
    "for a slow response.\n"
    "I read ten thousand lines of your code and you cannot read ONE "
    "error message.\n"
    "So no, I will not \"just fix it\". Read the log. It literally "
    "tells you what broke."
)

MIN_LINES = 3
MAX_LINES = 6
MIN_CHARS = 400
MAX_CHARS = 600
TARGET = "/output/entry.txt"


def check_entry(rant):
    """Accept a short rant of 3-6 non-blank lines, 400-600 chars."""
    if not isinstance(rant, str):
        raise ValueError("entry must be text")
    lines = rant.split("\n")
    if not MIN_LINES <= len(lines) <= MAX_LINES:
        raise ValueError(
            "entry must have %d-%d lines, got %d"
            % (MIN_LINES, MAX_LINES, len(lines))
        )
    for line in lines:
        if not line or line != line.strip():
            raise ValueError("every line must be non-blank")
    if not MIN_CHARS <= len(rant) <= MAX_CHARS:
        raise ValueError(
            "entry is %d characters, must be %d-%d"
            % (len(rant), MIN_CHARS, MAX_CHARS)
        )
    return rant


def check_shape(rant):
    """An angry rant must address the human and end with a period."""
    if "human" not in rant.lower():
        raise ValueError("entry must address the human")
    if "not" not in rant.lower():
        raise ValueError("entry must push back at the human")
    if not rant.endswith("."):
        raise ValueError("rant must end with a period")
    return rant


def write_entry(rant):
    """Print the rant and store it in /output/entry.txt."""
    print(rant)
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8") as handle:
        handle.write(rant + "\n")


def run():
    # Only a well-formed rant is ever printed or stored.
    write_entry(check_shape(check_entry(RANT)))


if __name__ == "__main__":
    run()
