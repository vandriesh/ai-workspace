"""Checks for score.py. Run: python3 test_score.py

These are ordinary pytest tests (files `test_*.py`, functions `test_*`). pytest isn't
installed yet, so the block at the bottom runs them without it.
"""

from score import score, words


def test_words_are_lowercase_and_distinct():
    got = words("Export to Excel, export!")
    assert got == {"export", "to", "excel"}, got


def test_punctuation_alone_has_no_words():
    got = words("?! --")
    assert got == set(), got


def test_a_title_match_earns_three():
    got = score("excel", title="Excel", summary="", body="")
    assert got == 3.0, got


def test_each_field_earns_its_own_points():
    got = score("excel", title="Export to Excel", summary="Excel files.", body="Excel")
    assert got == 5.5, got


def test_a_repeated_query_word_counts_once():
    got = score("excel excel", title="Excel", summary="", body="")
    assert got == 3.0, got


def test_no_shared_words_scores_zero():
    got = score("slack", title="Export to Excel", summary="Download hours.", body="Open Reports.")
    assert got == 0.0, got


def test_case_and_punctuation_do_not_matter():
    got = score("EXPORT, excel?", title="export-to-excel", summary="", body="")
    assert got == 6.0, got


def test_the_worked_example_from_the_lesson():
    got = score(
        "export excel",
        title="export-to-excel Export to Excel",
        summary="Download your hours as an Excel file.",
        body="Download your hours as an Excel file. Open Reports and choose Export.",
    )
    assert got == 9.5, got


if __name__ == "__main__":
    # A small stand-in for pytest, so this runs on a bare python3 with nothing installed.
    import sys

    failures = 0
    for name, test in list(globals().items()):
        if not name.startswith("test_"):
            continue
        try:
            test()
        except NotImplementedError:
            failures += 1
            print(f"todo  {name}")
        except AssertionError as error:
            failures += 1
            print(f"FAIL  {name}: got {error}")
        except Exception as error:
            failures += 1
            print(f"ERROR {name}: {type(error).__name__}: {error}")
        else:
            print(f"pass  {name}")

    print("\nAll green." if not failures else f"\n{failures} to go.")
    sys.exit(1 if failures else 0)
