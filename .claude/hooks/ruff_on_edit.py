"""PostToolUse hook: format and lint-fix edited files under mikeplus/.

Remaining lint errors are reported back to Claude via exit code 2.
"""

import json
import shutil
import subprocess
import sys
from pathlib import Path

payload = json.load(sys.stdin)
file_path = payload.get("tool_input", {}).get("file_path")
if not file_path:
    sys.exit(0)

project = Path(payload.get("cwd") or ".").resolve()
path = Path(file_path).resolve()
try:
    rel = path.relative_to(project).as_posix()
except ValueError:
    sys.exit(0)

if (
    path.suffix != ".py"
    or not rel.startswith("mikeplus/")
    or rel.startswith("mikeplus/tables/auto_generated/")
):
    sys.exit(0)

ruff = ["ruff"] if shutil.which("ruff") else ["uv", "run", "--no-sync", "ruff"]

try:
    subprocess.run([*ruff, "format", "--quiet", str(path)], cwd=project, check=False)
    result = subprocess.run(
        [*ruff, "check", "--fix", "--quiet", str(path)],
        cwd=project,
        capture_output=True,
        text=True,
        check=False,
    )
except FileNotFoundError:
    sys.exit(0)

if result.returncode != 0 and result.stdout.strip():
    print(result.stdout, file=sys.stderr)
    sys.exit(2)
