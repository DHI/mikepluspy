"""Claude Code hooks that put lint and type errors in front of the agent as it works.

edit   PostToolUse on Edit|Write. Formats and fixes the edited file with ruff, then reports
       what ruff and pyrefly still find in it. Only package files, which is what CI checks.
stop   Stop. If code or docs changed, runs ``just lint`` and ``just typecheck`` and
       reports a failure once; ``stop_hook_active`` lets the agent stop the second time.

Exit code 2 sends stderr to the agent. Nothing is printed on success.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PACKAGE = ROOT / "mikeplus"
GENERATED = PACKAGE / "tables" / "auto_generated"
CHECKED_SUFFIXES = {".py", ".qmd", ".md", ".ipynb", ".toml", ".yml"}
MAX_LINES = 60


def tool(name: str) -> str:
    """Return the path of a tool installed next to this Python, or its bare name."""
    scripts = Path(sys.executable).parent
    for candidate in (scripts / name, scripts / f"{name}.exe"):
        if candidate.is_file():
            return str(candidate)
    return shutil.which(name) or name


def run(*command: str) -> tuple[int, str]:
    """Run a command in the repository; return its exit code and combined output."""
    result = subprocess.run(
        command, cwd=ROOT, capture_output=True, text=True, encoding="utf-8"
    )
    return result.returncode, (result.stdout + result.stderr).strip()


def report(output: str) -> int:
    """Send output to the agent, trimmed to its last lines, and return exit code 2."""
    lines = output.splitlines()
    if len(lines) > MAX_LINES:
        lines = [f"... {len(lines) - MAX_LINES} lines cut", *lines[-MAX_LINES:]]
    print("\n".join(lines), file=sys.stderr)
    return 2


def edit(event: dict) -> int:
    """Fix the edited package file, then report what is left in it."""
    raw = event.get("tool_input", {}).get("file_path", "")
    path = (ROOT / raw).resolve() if raw else None
    if (
        path is None
        or path.suffix != ".py"
        or not path.is_relative_to(PACKAGE)
        or path.is_relative_to(GENERATED)
        or not path.is_file()
    ):
        return 0
    ruff = tool("ruff")
    run(ruff, "format", "--quiet", str(path))
    run(ruff, "check", "--fix", "--quiet", str(path))
    problems = []
    for command in (
        (ruff, "check", "--quiet", "--output-format", "concise", str(path)),
        (tool("pyrefly"), "check", "--output-format", "min-text", "--summary=none", str(path)),
    ):
        code, output = run(*command)
        if code != 0:
            problems.append(output)
    return report("\n".join(problems)) if problems else 0


def stop(event: dict) -> int:
    """Run the fast CI checks if anything they cover changed; report a failure once."""
    if event.get("stop_hook_active"):
        return 0
    _, status = run("git", "status", "--porcelain")
    changed = [line[3:].strip('"') for line in status.splitlines()]
    if not any(Path(p).suffix in CHECKED_SUFFIXES for p in changed):
        return 0
    failures = []
    for recipe in ("lint", "typecheck"):
        code, output = run("just", recipe)
        if code != 0:
            failures.append(f"just {recipe} failed:\n{output}")
    return report("\n\n".join(failures)) if failures else 0


def main() -> int:
    """Dispatch on the hook named in the first argument."""
    try:
        event = json.load(sys.stdin)
    except json.JSONDecodeError:
        event = {}
    hooks = {"edit": edit, "stop": stop}
    return hooks[sys.argv[1]](event)


if __name__ == "__main__":
    sys.exit(main())
