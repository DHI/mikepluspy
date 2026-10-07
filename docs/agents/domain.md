# Domain Docs

How the engineering skills should consume this repo's domain documentation when exploring the codebase. This is a single-context repo.

## Before exploring, read these

- **`GLOSSARY.md`** at the repo root.
- **`adr/`** at the repo root: read ADRs that touch the area you're about to work in.

If either doesn't exist, **proceed silently**. Don't flag its absence; don't suggest creating it upfront. The `/domain-modeling` skill creates them lazily when terms or decisions actually get resolved.

## File structure

```
/
├── GLOSSARY.md
├── adr/
│   ├── 0001-no-mocking-dotnet.md
│   └── 0004-mikeplus-is-a-black-box.md
└── mikeplus/
```

New ADRs continue the numbering as `adr/NNNN-kebab-title.md`.

Per ADR-0004, glossary entries and ADRs describe MIKE+ only by its observed behaviour and public surface, never its internals.

## Use the glossary's vocabulary

When your output names a domain concept (in an issue title, a refactor proposal, a hypothesis, a test name), use the term as defined in `GLOSSARY.md`. Don't drift to synonyms the glossary explicitly avoids.

If the concept you need isn't in the glossary yet, that's a signal: either you're inventing language the project doesn't use (reconsider) or there's a real gap (note it for `/domain-modeling`).

## Flag ADR conflicts

If your output contradicts an existing ADR, surface it explicitly rather than silently overriding:

> _Contradicts ADR-0001 (no mocking .NET), but worth reopening because…_
