"""Tests for scripts/lint_docs_examples.py, the static docs example linter.

The linter reads the package with griffe and never imports it, so these tests need no
MIKE+ install.
"""

from __future__ import annotations

import sys
import textwrap
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.lint_docs_examples import Checker, Package, Page, Snippet

PAGE = ROOT / "docs" / "example.qmd"


@pytest.fixture(scope="module")
def package() -> Package:
    """Load the package once for the module."""
    return Package()


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
