"""Lesson 1 exercise: score one doc against a query, the way tsbuddy-ai's retrieval does.

Write both function bodies yourself: no AI, no autocomplete, and don't open
tsbuddy-ai/app/corpus.py until the tests pass.

Check your work:  python3 test_score.py
"""

import re

WORD_RE = re.compile(r"[a-z0-9]+")


def words(text: str) -> set[str]:
    """The distinct lowercase words in `text`. Anything that isn't a-z or 0-9 separates words."""
    raise NotImplementedError


def score(query: str, title: str, summary: str, body: str) -> float:
    """How well one doc matches the query.

    Each distinct query word earns 3.0 if it appears in the title, 1.5 if it appears in
    the summary and 1.0 if it appears in the body. A word found in several fields earns
    points in each of them.
    """
    raise NotImplementedError
