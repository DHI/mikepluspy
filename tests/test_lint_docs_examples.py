"""Tests for scripts/linters/lint_docs_examples.py, the static docs example linter.

The linter reads the package with griffe and pyrefly and never imports it, so these
tests need no MIKE+ install.
"""

from __future__ import annotations

import json
import sys
import textwrap
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.linters.lint_docs_examples import (
    PACKAGE,
    Package,
    Page,
    Snippet,
    check_docstring_sections,
    code_blocks,
    docstring_pages,
    lint_pages,
    notebook_snippets,
)

PAGE = ROOT / "docs" / "example.qmd"


@pytest.fixture(scope="module")
def package() -> Package:
    """Load the package once for the module."""
    return Package()


def make_package(tmp_path: Path, source: str) -> Package:
    """Load a stand-in package whose ``__init__.py`` is ``source``."""
    (tmp_path / PACKAGE).mkdir()
    (tmp_path / PACKAGE / "__init__.py").write_text(
        textwrap.dedent(source), encoding="utf-8"
    )
    return Package(tmp_path)


def lint(package: Package, *blocks: str) -> list[str]:
    """Check code blocks as one page; return the findings as ``line check: message``."""
    page = Page(PAGE, [Snippet(PAGE, 1, textwrap.dedent(b).strip("\n")) for b in blocks])
    findings = sorted(lint_pages(package, [page]), key=lambda f: f.line)
    return [f"{f.line} {f.check}: {f.message}" for f in findings]


def test_unknown_keyword(package):
    """A keyword the signature does not take is reported."""
    (finding,) = lint(package, 'db.run(model_option="CS_MIKE_1D")')
    assert finding.startswith("1 unexpected-keyword:")
    assert "model_option" in finding


def test_literal_value_outside_the_allowed_set(package):
    """A constant outside a Literal annotation is reported."""
    (finding,) = lint(package, 'db.run(sim_option="CS_MIKE1D")')
    assert finding.startswith("1 bad-argument-type:")
    assert "CS_MIKE1D" in finding


def test_types_flow_through_with_and_properties(package):
    """Types follow mp.open, the with target and properties."""
    findings = lint(
        package,
        """
        import mikeplus as mp
        with mp.open("model.sqlite") as model:
            model.tables.msm_Node.select().where("x").to_pandas()
            model.tables.msm_Node.selectt()
        """,
    )
    assert len(findings) == 1
    assert findings[0].startswith("4 missing-attribute:")
    assert "selectt" in findings[0]


def test_blocks_of_a_page_share_bindings(package):
    """A name bound in one block is known in the next."""
    findings = lint(package, "groups = db.alternative_groups", "groups.keys()")
    assert len(findings) == 1
    assert "has no attribute `keys`" in findings[0]


def test_findings_are_reported_at_their_docs_line(package):
    """A finding in a block points at the docs line the code is on."""
    page = Page(PAGE, [Snippet(PAGE, 10, "x = 1"), Snippet(PAGE, 20, "y = 2\ndb.nope")])
    (finding,) = lint_pages(package, [page])
    assert (finding.path, finding.line) == (PAGE, 21)


def test_assuming_comment_gives_a_type(package):
    """An 'Assuming x is a Y object' comment types x."""
    (finding,) = lint(package, "# Assuming 'alt' is a valid Alternative object\nalt.nme")
    assert finding.startswith("2 missing-attribute:")
    assert "Alternative" in finding


def test_assuming_comment_after_code_keeps_the_code(package):
    """A hint trailing a line of code does not replace that code."""
    (finding,) = lint(
        package, "db.tables.msm_Node.selectt()  # 'alt' is an Alternative object"
    )
    assert finding.startswith("1 missing-attribute:")


def test_imports_are_checked(package):
    """Imports of missing package modules and names are reported."""
    findings = lint(
        package,
        "import mikeplus.engines\nfrom mikeplus.tools import CatchSlopeLengthProcess",
    )
    assert [f.split(":")[0] for f in findings] == ["1 missing-import", "2 missing-module-attribute"]


def test_other_packages_need_not_be_installed(package):
    """Imports of other packages, installed or not, are not reported."""
    assert lint(package, "import mikeio\nfrom contextily import providers\nimport pandas") == []


def test_lookups_are_assumed_to_succeed(package):
    """Using an ``X | None`` lookup result as an ``X`` is not reported."""
    findings = lint(
        package,
        """
        scenario = db.scenarios.by_name("Base")
        scenario.activate()
        db.active_scenario = scenario
        """,
    )
    assert findings == []


def test_notebook_magics_are_ignored(package):
    """IPython magics and shell escapes are not Python, and not reported."""
    assert lint(package, "%matplotlib inline\n!pip install mikeplus\nx = 1") == []


def test_read_only_property(package):
    """Assigning to a property without a setter is reported."""
    (finding,) = lint(package, "db.unit_system = 'SI'")
    assert finding.startswith("1 read-only:")


def test_missing_and_extra_arguments(package):
    """A call that leaves out a required argument, or passes too many, is reported."""
    findings = lint(package, "import mikeplus as mp\nmp.open()\ndb.close(1)")
    assert [f.split(" ")[0] for f in findings] == ["2", "3"]


def test_query_reused_after_it_ran(package):
    """A query variable that runs twice is reported until reset() is called."""
    findings = lint(
        package,
        """
        query = db.tables.msm_Node.select()
        df = query.where("Diameter > 1").to_pandas()
        df = query.by_muid("N1").to_pandas()
        query.reset()
        df = query.to_pandas()
        """,
    )
    assert findings == [
        "3 query-reused: query 'query' already ran; a query runs once, "
        "so build a new one or call reset()"
    ]


def test_new_query_and_one_off_queries_are_not_reuse(package):
    """Assigning a new query, or running ``select()`` inline each time, is not reuse."""
    findings = lint(
        package,
        """
        query = db.tables.msm_Node.select()
        df = query.to_pandas()
        query = db.tables.msm_Node.select()
        df = query.to_pandas()
        db.tables.msm_Link.select().execute()
        db.tables.msm_Link.select().execute()
        """,
    )
    assert findings == []


def test_query_run_in_alternative_branches_runs_once(package):
    """Runs in an ``if`` and its ``else``, or a ``try`` and its handler, are not reuse."""
    findings = lint(
        package,
        """
        query = db.tables.msm_Node.select()
        if condition:
            df = query.to_pandas()
        else:
            rows = query.execute()
        other = db.tables.msm_Link.select()
        try:
            df = other.to_pandas()
        except RuntimeError:
            rows = other.execute()
        """,
    )
    assert [f for f in findings if "query-reused" in f] == []


def test_query_run_after_a_branch_that_ran_it_is_reported(package):
    """A run after an ``if`` that may have run the query is reuse."""
    findings = lint(
        package,
        """
        query = db.tables.msm_Node.select()
        if condition:
            df = query.to_pandas()
        rows = query.execute()
        """,
    )
    assert [f for f in findings if "query-reused" in f] == [
        "4 query-reused: query 'query' already ran; a query runs once, "
        "so build a new one or call reset()"
    ]


def test_docstring_examples_keep_their_source_lines(package):
    """Each line of a docstring example is reported at its own line of the module."""
    pages = docstring_pages(package)
    to_sql = next(
        p.snippets[0] for p in pages if p.snippets[0].source.startswith("to_sql(10)")
    )
    source = to_sql.path.read_text(encoding="utf-8").splitlines()
    assert source[to_sql.line - 1 + 2].strip() == ">>> to_sql(10.5)"
    for page in pages:
        snippet = page.snippets[0]
        source = snippet.path.read_text(encoding="utf-8").splitlines()
        for index, line in enumerate(snippet.source.splitlines()):
            if line.strip():
                assert line.strip() in source[snippet.line - 1 + index]


def test_docstring_examples_see_their_module(package):
    """A docstring example may use the names of its module without importing them."""
    page = next(p for p in docstring_pages(package) if "to_sql(10)" in p.snippets[0].source)
    assert lint_pages(package, [page]) == []


def test_a_bare_fence_starting_with_python_is_not_python():
    """``python -m pip`` on the first line of a bare fence is shell, not a fence class."""
    text = "```\npython -m pip install mikeplus\n```\n\n```python\nimport mikeplus\n```\n"
    assert [body for _, _, body in code_blocks(text)] == ["import mikeplus\n"]


def test_notebook_cells_report_their_json_lines():
    """A notebook cell's lines are numbered by the JSON line they are on."""
    text = textwrap.dedent(
        """\
        {
         "cells": [
          {
           "cell_type": "markdown",
           "source": [
            "# Title"
           ]
          },
          {
           "cell_type": "code",
           "source": [
            "import mikeplus as mp\\n",
            "mp.nope"
           ]
          }
         ]
        }
        """
    )
    snippets = notebook_snippets(PAGE, text)
    assert [(s.line, s.source) for s in snippets] == [
        (12, "import mikeplus as mp\nmp.nope")
    ]


def test_notebook_cells_on_one_line_are_numbered_as_one_file():
    """A notebook not written one line per JSON line falls back to cumulative lines."""
    cells = [
        {"cell_type": "markdown", "source": "# Title\ntext"},
        {"cell_type": "code", "source": "import mikeplus"},
    ]
    snippets = notebook_snippets(PAGE, json.dumps({"cells": cells}))
    assert [(s.line, s.source) for s in snippets] == [(3, "import mikeplus")]


def test_docstring_opening_on_its_own_line_keeps_source_lines(tmp_path):
    """A docstring whose text starts on the line after the quotes is not off by one."""
    package = make_package(
        tmp_path,
        '''
        class Thing:
            """
            A thing.

            Attributes
            ----------
            weight : float
                Not set anywhere.

            Examples
            --------
            >>> Thing().nope
            """
        ''',
    )
    source = (tmp_path / PACKAGE / "__init__.py").read_text().splitlines()
    snippet = docstring_pages(package)[0].snippets[0]
    assert source[snippet.line - 1].strip() == ">>> Thing().nope"
    (finding,) = check_docstring_sections(package)
    assert source[finding.line - 1].strip() == "weight : float"


def test_docstring_sections_are_checked_against_the_class(tmp_path):
    """``Attributes`` and ``Methods`` entries that the class lacks are reported."""
    package = make_package(
        tmp_path,
        '''
        class Thing:
            """A thing.

            Attributes
            ----------
            size : int
                Set in ``__init__``.
            colour : str
                Set in ``paint``.
            weight : float
                Not set anywhere.

            Methods
            -------
            grow(by)
                Grow.
            shrink(by)
                Not a method.
            paint(colour)
                Not a parameter.
            """

            def __init__(self):
                self.size = 1

            def grow(self, by: int) -> None: ...

            def paint(self):
                self.colour = "red"
        ''',
    )
    findings = [(f.check, f.message) for f in check_docstring_sections(package)]
    assert findings == [
        ("docstring-attrs", "Thing documents attribute 'weight', which it does not have"),
        ("docstring-methods", "Thing documents method 'shrink', which it does not have"),
        (
            "docstring-methods",
            "Thing documents paint(colour=...), but paint has no parameter 'colour'",
        ),
    ]
