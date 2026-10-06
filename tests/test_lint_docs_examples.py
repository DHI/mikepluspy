"""Tests for scripts/lint_docs_examples.py, the static docs example linter.

The linter reads the package with griffe and never imports it, so these tests need no
MIKE+ install.
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

from scripts.lint_docs_examples import (
    PACKAGE,
    Checker,
    Package,
    Page,
    Snippet,
    check_docstring_sections,
    code_blocks,
    docstring_pages,
    notebook_snippets,
    parse_all_docstrings,
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


def lint(package: Package, *blocks: str, inline: list[str] | None = None) -> list[str]:
    """Check code blocks as one page; return the findings as ``check: message``."""
    page = Page(PAGE, [Snippet(PAGE, 1, textwrap.dedent(b)) for b in blocks])
    page.inline = [(1, code) for code in inline or []]
    checker = Checker(package, page)
    checker.run()
    return [f"{f.check}: {f.message}" for f in checker.findings]


def test_unknown_keyword_suggests_the_real_one(package):
    """A misspelt keyword is reported with the closest real one."""
    findings = lint(package, 'db.run(model_option="CS_MIKE_1D")')
    assert findings == [
        (
            "unknown-keyword: Database.run() has no parameter 'model_option'; "
            "did you mean 'sim_option'?"
        )
    ]


def test_literal_value_outside_the_allowed_set(package):
    """A constant outside a Literal annotation is reported."""
    findings = lint(package, 'db.run(sim_option="CS_MIKE1D")')
    assert len(findings) == 1
    assert findings[0].startswith(
        "invalid-literal: Database.run(): sim_option='CS_MIKE1D'"
    )


def test_types_flow_through_with_and_properties(package):
    """Types follow mp.open, the with target, properties and Returns sections."""
    findings = lint(
        package,
        """
        import mikeplus as mp
        with mp.open("model.sqlite") as model:
            model.tables.msm_Node.select().where("x").to_pandas()
            model.tables.msm_Node.selectt()
        """,
    )
    assert findings == [
        "unknown-attribute: msm_NodeTable has no attribute 'selectt'; did you mean 'select'?"
    ]


def test_blocks_of_a_page_share_bindings(package):
    """A name bound in one block is known in the next."""
    findings = lint(package, "groups = db.alternative_groups", "groups.keys()")
    assert findings == [
        "unknown-attribute: AlternativeGroupCollection has no attribute 'keys'"
    ]


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
    assert len(findings) == 1
    assert findings[0].startswith("query-reused: query 'query' already ran on line 3")


def test_commented_out_code_is_checked_without_rebinding(package):
    """Commented-out code is checked, but does not replace the page's bindings."""
    findings = lint(
        package,
        """
        nodes = db.tables.msm_Node
        # nodes = db.tables["msm_Node"]
        # db.active_scenario = "Other"
        nodes.columns.MUID
        """,
    )
    assert findings == [
        (
            "wrong-type: Database.active_scenario takes a Scenario, not a str literal "
            "(in commented-out code)"
        )
    ]


def test_assuming_comment_gives_a_type(package):
    """An 'Assuming x is a Y object' comment types x."""
    findings = lint(package, "# Assuming 'alt' is a valid Alternative object\nalt.nme")
    assert findings == [
        "unknown-attribute: Alternative has no attribute 'nme'; did you mean 'name'?"
    ]


def test_imports_are_checked(package):
    """Imports of missing modules and names are reported."""
    findings = lint(
        package,
        "import mikeplus.engines\nfrom mikeplus.tools import CatchSlopeLengthProcess",
    )
    assert findings == [
        "unknown-module: 'mikeplus.engines' is not a module of the package",
        (
            "unknown-import: module mikeplus.tools has no 'CatchSlopeLengthProcess'; "
            "did you mean 'CathSlopeLengthProcess'?"
        ),
    ]


def test_inline_code_in_prose(package):
    """Inline code naming a near-miss class, or an expression on db, is checked."""
    findings = lint(
        package,
        inline=[
            "CatchSlopeLengthProcess",
            "RuntimeError",
            "db.scenarios.alternative_groups",
            "mp.open()",
        ],
    )
    assert findings == [
        (
            "unknown-name: 'CatchSlopeLengthProcess' is not a class of the package; "
            "did you mean 'CathSlopeLengthProcess'?"
        ),
        "unknown-attribute: ScenarioCollection has no attribute 'alternative_groups'",
    ]


def test_unknown_types_are_skipped(package):
    """Anything whose type is not inferred is skipped, not reported."""
    findings = lint(
        package,
        """
        import pandas as pd
        frame = pd.DataFrame()
        frame.anything.at_all()
        thing = some_function()
        thing.whatever(bad_keyword=1)
        db.tables["msm_Node"].get_number_of_links("N1")  # a BaseTable, but maybe a node table
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
    assert findings == []


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
    assert len(findings) == 1
    assert findings[0].startswith("query-reused: query 'query' already ran on line 4")


def test_commented_out_query_run_does_not_count_as_a_run(package):
    """A commented-out alternative run leaves the query unrun for the live line."""
    findings = lint(
        package,
        """
        query = db.tables.msm_Node.select()
        # df = query.to_pandas()  # or, with a filter:
        df = query.where("Diameter > 1").to_pandas()
        """,
    )
    assert findings == []


def test_commented_out_query_run_after_a_run_is_reported(package):
    """Uncommenting a run after the query ran would run it twice."""
    findings = lint(
        package,
        """
        query = db.tables.msm_Node.select()
        df = query.to_pandas()
        # df = query.where("Diameter > 1").to_pandas()
        """,
    )
    assert len(findings) == 1
    assert findings[0].startswith("query-reused: query 'query' already ran on line 3")
    assert findings[0].endswith("(in commented-out code)")


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


def test_a_bare_fence_starting_with_python_is_not_python():
    """``python -m pip`` on the first line of a bare fence is shell, not a fence class."""
    text = "```\npython -m pip install mikeplus\n```\n\n```python\nimport mikeplus\n```\n"
    assert [body for _, _, body in code_blocks(text)] == ["import mikeplus\n"]


def test_inline_code_on_the_package_name_is_checked(package):
    """Inline ``mikeplus.x`` is checked like ``mp.x``."""
    findings = lint(package, inline=["mikeplus.nonexistent_thing", "mikeplus.open"])
    assert findings == [
        "unknown-attribute: module mikeplus has no 'nonexistent_thing'"
    ]


def test_read_only_property(package):
    """Assigning to a property without a setter is reported."""
    assert lint(package, "db.unit_system = 'SI'") == [
        "read-only-property: Database.unit_system is a read-only property"
    ]


def test_missing_and_extra_arguments(package):
    """A call that leaves out a required argument, or passes too many, is reported."""
    findings = lint(package, "import mikeplus as mp\nmp.open()\ndb.close(1)")
    assert findings == [
        "missing-argument: open() is missing 'model_path'",
        "too-many-arguments: Database.close() takes 0 positional arguments, 1 given",
    ]


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


def test_attribute_checks_leave_open_types_alone(tmp_path):
    """Only closed types are checked: not iterables, stdlib instances or late ``self.x``."""
    package = make_package(
        tmp_path,
        """
        import subprocess
        from collections.abc import Iterator, Sequence


        class Thing:
            def __init__(self):
                self.early = 1

            def setup(self):
                self.late = 2

            def items(self) -> Sequence[int]: ...

            def stream(self) -> Iterator[int]: ...

            def process(self) -> subprocess.CompletedProcess: ...

            def name(self) -> str: ...
        """,
    )
    findings = lint(
        package,
        """
        import mikeplus
        thing = mikeplus.Thing()
        thing.items().count(1)
        thing.stream().anything
        thing.process().returncode
        thing.early, thing.late
        thing.name().nope
        thing.missing
        """,
    )
    assert findings == [
        "unknown-attribute: str has no attribute 'nope'",
        "unknown-attribute: Thing has no attribute 'missing'",
    ]


def test_open_annotations_are_not_checked(tmp_path):
    """``Literal | str``, ``type[X]`` and ``object`` allow more than they name."""
    package = make_package(
        tmp_path,
        """
        from typing import Literal


        class Thing:
            def go(self, mode: Literal["a", "b"] | str) -> None: ...

            def go_or_none(self, mode: Literal["a", "b"] | None = None) -> None: ...

            def kind(self) -> type[Thing]: ...

            def anything(self) -> object: ...

            def many(self) -> list[Thing]: ...
        """,
    )
    findings = lint(
        package,
        """
        import mikeplus
        thing = mikeplus.Thing()
        thing.go("c")
        thing.go_or_none("c")
        thing.kind().build()
        thing.anything().whatever
        thing.many()[:2].append(thing)
        thing.many()[0].nope
        """,
    )
    assert findings == [
        "invalid-literal: Thing.go_or_none(): mode='c' is not one of 'a', 'b'",
        "unknown-attribute: Thing has no attribute 'nope'",
    ]


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
    """``Attributes`` and ``Parameters`` entries that the code lacks are reported."""
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
            """

            def __init__(self):
                self.size = 1

            def paint(self):
                self.colour = "red"

            def grow(self, by: int) -> None:
                """Grow.

                Parameters
                ----------
                by
                    How much.
                amount
                    Not a parameter.
                """
        ''',
    )
    findings = [
        (f.check, f.message)
        for f in [*parse_all_docstrings(package), *check_docstring_sections(package)]
    ]
    assert len(findings) == 2
    assert findings[0][0] == "docstring-params"
    assert "amount" in findings[0][1]
    assert findings[1] == (
        "docstring-attrs",
        "Thing documents attribute 'weight', which it does not have",
    )
