"""Small string utilities."""

import re


def slugify(text):
    """Return a lowercase, hyphen-separated slug for ``text``."""
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def truncate(text, n):
    """Return ``text`` shortened to at most ``n`` characters.

    If truncation happens, the result ends with an ellipsis and its total
    length is exactly ``n``.
    """
    if len(text) <= n:
        return text
    return text[:n] + "…"


def word_count(text):
    """Return the number of whitespace-separated words in ``text``."""
    return len(text.split())
