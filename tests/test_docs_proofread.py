"""Tests for the Markdown that scripts/docs.py proofreads in place of Python modules."""

from __future__ import annotations

import sys
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.docs import docstring_markdown

MODULE = textwrap.dedent('''\
    """Module summary."""

    # A comment with Nonwordz.


    def run(muid):
        """Run a simulation.

        Prose can quote `names`.

        Parameters
        ----------
        muid : str, optional
            Simulation MUID.

        Returns
        -------
        list[Path]
            Result files.

        Examples
        --------
        >>> db.run("Nonwordz")
        ['Nonwordz.res1d']

        Back to prose.
        """
''')


def test_docstrings_keep_their_lines():
    markdown = docstring_markdown(MODULE).splitlines()
    assert len(markdown) == len(MODULE.splitlines())
    assert markdown[0] == "Module summary."
    assert markdown[6] == "Run a simulation."
    assert markdown[8] == "Prose can quote `names`."


def test_comments_and_code_are_blank():
    markdown = docstring_markdown(MODULE).splitlines()
    assert markdown[2] == ""
    assert markdown[5] == ""


def test_term_lines_are_code_and_descriptions_are_prose():
    markdown = docstring_markdown(MODULE).splitlines()
    assert markdown[10:15] == [
        "Parameters",
        "----------",
        "`muid : str, optional`",
        "Simulation MUID.",
        "",
    ]
    assert markdown[17] == "`list[Path]`"


def test_doctests_are_blank():
    markdown = docstring_markdown(MODULE)
    assert "Nonwordz" not in markdown
    assert "Back to prose." in markdown
