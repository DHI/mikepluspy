# ADR 0004: MIKE+ is a black box; its source stays inside DHI

- Status: Accepted
- Date: 2026-10-01

## Context

MIKE+Py is public: the repository, its history, pull requests, issues, the docs site and the PyPI package can all be read by anyone. MIKE+ is proprietary. Its source code is DHI's intellectual property and is not published.

DHI employees who work on MIKE+Py can often read the MIKE+ source, and sometimes have to, to find out why a .NET call behaves the way it does. Coding agents working for them may have the same access. That makes it easy for MIKE+ code to leak across the boundary: a snippet pasted into a comment to explain a workaround, a decompiled method quoted in an issue, a commit message that walks through an internal code path. Once something is pushed or posted publicly it can be cached, forked or indexed, so deleting it later doesn't undo the leak.

## Decision

MIKE+Py treats MIKE+ as a black box. It depends only on what anyone with a MIKE+ install can observe from outside: the public types and members of the installed assemblies, their signatures, and how they behave when called.

MIKE+ code never enters this repository or any other public medium. That covers source files, commits and commit messages, branch names, pull requests, reviews, issues, discussions, the docs site, release notes and package contents. "MIKE+ code" includes:

- Source code from internal DHI repositories, whole or in part.
- Decompiled or disassembled output from the MIKE+ assemblies.
- Close paraphrases of either, such as a line-by-line description of a method body, or names and logic of private or internal members.

DHI employees, and agents working for them, may read the MIKE+ source to understand a behaviour. What they bring across the boundary is the *observed behaviour* and the fix, written as a black-box description:

- Allowed: "`UpdateGeomByCommand` rejects a `POINT` on a link and returns `CmdCommitted=False`." "This signature changed between 2026 GA and U1." "MIKE+ requires the column name in canonical casing."
- Not allowed: a quoted or reconstructed method body, an internal class or call chain from the MIKE+ source, or a stack trace that exposes MIKE+ internals beyond the public member that was called.

If a behaviour can only be explained by pointing at MIKE+ internals, describe the symptom and the workaround, and keep the explanation internal to DHI (for example in an internal ticket).

## Consequences

- Code comments, tests and PR descriptions justify workarounds by observable behaviour. A reader outside DHI can verify every claim against their own MIKE+ install.
- Agents with access to MIKE+ source keep it out of everything they write here, including draft PR text and issue comments. `AGENTS.md` carries this rule.
- If MIKE+ code is found in the repository or its history, treat it as a security incident: remove it, and contact the maintainers so they can decide whether the history needs rewriting and whether other copies (forks, PyPI releases, the docs site) need removing.
- Some explanations will be less complete in public than they could be. That is the price of the boundary.
