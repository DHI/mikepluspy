# ADR 0003: Keep a changelog

- Status: Accepted
- Date: 2026-10-01

## Context

`CHANGELOG.md` is where release notes are written. GitHub release notes are copied from it, and `great-docs.yml` turns off the docs site's GitHub Releases changelog in its favour. The file already roughly follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), but nothing said so, and it had drifted:

- It had no link references, so version headings weren't links.
- A `2026.1.0` section was dated 2026-06-23, although 2026.1.0 was never tagged or published. Its entries looked released when they weren't.
- Changes merged after v2026.0.0 were missing, such as the river junction coupling utilities (#112), case-insensitive names (#128) and the moved API reference.

Users of a year line (GA, U1, U2…) upgrade expecting nothing to break. They need one place that tells them what did change, in their terms.

## Decision

`CHANGELOG.md` follows [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/):

- Every PR with a user-visible change adds a line under `## [Unreleased]` in the same PR. That means changes to the public API (see "Public API" in `DEVELOPMENT.md`), behaviour, supported MIKE+ versions, platforms, Python or dependency floors, and the documentation site's URLs. Internal refactors, tests, CI and development tooling don't get a line.
- Entries go under `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed` or `Security`, describe the change from the user's side, and cite the issue when there is one. Empty sections are left out.
- A version heading is `## [<version>] - <YYYY-MM-DD>` and is added only when that version is released, by renaming `[Unreleased]` and adding a fresh one above it. Versions follow the MIKE+ year (`2026.x.x`), not SemVer, so the file doesn't claim to follow SemVer.
- Each heading has a link reference at the bottom of the file: `[Unreleased]` compares the latest tag with `main`, and each version compares its tag with the one before it.

## Consequences

- Reviewers check for the changelog line as part of review. CI doesn't enforce it.
- Releasing includes moving `[Unreleased]` to a dated heading and adding its link reference. The release checklist in `DEVELOPMENT.md` lists this step.
- The unpublished `2026.1.0` entries were moved back under `[Unreleased]`. They'll ship in the next release.
- `2025.1.2` has no tag or PyPI release, so its heading has no link. It stays as a historical entry.
