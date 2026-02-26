# MikePlusJsonCli — JSON Streaming CLI for MIKE+

## Design overview

This directory contains a **design alternative** to the traditional subcommand-based CLI
described in PR #113 (`cli/MikePlusCli`).  The key difference is the communication
protocol: instead of mapping each operation to a distinct `mikeplus <verb> <noun>`
invocation, this CLI speaks a **Newline-Delimited JSON (NDJSON) streaming protocol**.
The process reads an arbitrary sequence of JSON command objects from stdin and emits
a corresponding sequence of JSON result objects to stdout.

```
[caller / AI agent / script]
          │  stdin  (NDJSON commands)
          ▼
  ┌───────────────────┐
  │  mikeplus-json    │   one process, one Amelia session
  │  ─────────────── │
  │  Program.cs       │◄─ reads line by line
  │  CommandDispatcher│─► routes to ICommandHandler
  │  Session          │─► holds open AmeliaContexts
  └───────────────────┘
          │  stdout (NDJSON results)
          ▼
[caller / AI agent / script]
```

---

## Why a streaming protocol?

### The per-invocation cost problem

PR #113's design is "one invocation = one operation":

```bash
mikeplus edit insert msm_Node -d model.sqlite --set MUID=N1 --set Diameter=1.5
mikeplus edit insert msm_Node -d model.sqlite --set MUID=N2 --set Diameter=2.0
# … 998 more times for 1 000 nodes
```

Each invocation:
1. Starts the .NET runtime
2. Loads all Amelia assemblies from disk
3. Opens the SQLite database via Amelia's `BaseDataSource`
4. Performs the operation
5. Closes the database and exits

For bulk workflows (the common case in MIKE+ modelling) this is prohibitively slow.
PR #113 partially mitigates this with `--input file.json`, but that requires
buffering all rows before processing and only applies to `edit insert/update`.

### The streaming solution

```bash
cat nodes.ndjson | mikeplus-json
# or equivalently:
generate_nodes.py | mikeplus-json
```

A single `mikeplus-json` process handles the entire stream:
- Assemblies are loaded once
- The database is opened once (on the first `model.open` command, or lazily on
  the first command that references a database path)
- All subsequent commands reuse the same `AmeliaContext` — the same
  `DataTableContainer`, `UndoRedoManager`, and `IScenarioManager` that the
  MIKE+ GUI maintains for the lifetime of a project

For 1 000 inserts, this collapses the lifecycle cost from O(N) to O(1).

---

## Protocol

### Input — one JSON object per line (stdin)

```jsonc
// Minimal command
{"id":"1","command":"model.open","database":"model.sqlite"}

// Command with query parameters
{"id":"2","command":"edit.select","table":"msm_Node","columns":["MUID","Diameter"],"where":"Diameter > 0.5"}

// Single-row mutation
{"id":"3","command":"edit.insert","table":"msm_Node","row":{"MUID":"N1","Diameter":1.5}}

// The same handler processes 1 000 inserts in the same open session
{"id":"4","command":"edit.insert","table":"msm_Node","row":{"MUID":"N2","Diameter":2.0}}

// Session-level state changes persist for all subsequent commands
{"id":"5","command":"scenario.activate","scenario":"Climate 2050"}

// No --engine flag needed again — session remembers the open database
{"id":"6","command":"simulate.run","muid":"Sim1","engine":"CS_MIKE_1D"}

// Explicit close (or omit; process exits cleanly on EOF)
{"id":"7","command":"model.close"}
```

Optional control fields:

| Field       | Values           | Description                                                  |
|-------------|------------------|--------------------------------------------------------------|
| `id`        | any string       | Echoed back in the response for correlation                  |
| `on_error`  | `"continue"` (default) / `"abort"` | Stop the entire session on this command's failure |

### Output — one JSON object per line (stdout)

```jsonc
{"id":"1","status":"ok","command":"model.open"}
{"id":"2","status":"ok","command":"edit.select","data":[{"MUID":"P1","Diameter":0.6}]}
{"id":"3","status":"ok","command":"edit.insert"}
{"id":"4","status":"ok","command":"edit.insert"}
{"id":"5","status":"ok","command":"scenario.activate"}
{"id":"6","status":"ok","command":"simulate.run","data":{"results":["model.res1d"]}}
{"id":"7","status":"ok","command":"model.close"}
```

On failure the envelope is:

```jsonc
{"id":"3","status":"error","command":"edit.insert","error":"Duplicate MUID 'N1'"}
```

Because each command is independent, a failure does **not** abort the session by
default — subsequent commands continue running.  Set `"on_error":"abort"` on any
command to change this for critical steps.

---

## Comparison with PR #113

| Concern                          | PR #113 (`MikePlusCli`)               | This design (`MikePlusJsonCli`)            |
|----------------------------------|---------------------------------------|--------------------------------------------|
| Process start per operation      | Yes                                   | No — one process per session               |
| Assembly load per operation      | Yes                                   | No — loaded once                           |
| Database open/close per operation| Yes (except `--input` bulk mode)      | No — opened once, reused                  |
| Bulk operations                  | Special `--input file.json` flag      | Stream N ordinary commands                 |
| Adding a new command             | New `Command` class + argument schema | New `ICommandHandler` registration         |
| AI agent integration             | Shell arg escaping required           | LLMs emit JSON natively                    |
| Error recovery                   | Subprocess exit codes                 | Per-command `{"status":"error"}` responses |
| Session state (active scenario)  | Must re-specify on every call         | Set once, persists across commands         |
| Parallel databases               | One `-d` per invocation               | Multiple open contexts keyed by path       |
| Streaming pipeline               | Limited (`--input -` for bulk only)   | Entire workflow is a stream                |

---

## Architecture

```
cli/MikePlusJsonCli/
├── README.md                      ← this file
├── MikePlusJsonCli.csproj         ← net8.0, System.Text.Json, DHI.Amelia refs
├── Program.cs                     ← stdin→stdout NDJSON loop
├── Session.cs                     ← open AmeliaContexts, active database tracking
├── CommandDispatcher.cs           ← command-name → ICommandHandler registry
├── Protocol/
│   └── CommandEnvelope.cs         ← strongly-typed protocol envelope
└── Handlers/
    ├── ICommandHandler.cs         ← handler contract
    ├── ModelHandlers.cs           ← model.open / model.close / model.create / model.info / model.tables
    ├── EditHandlers.cs            ← edit.select / edit.insert / edit.update / edit.delete
    ├── ScenarioHandlers.cs        ← scenario.list / scenario.create / scenario.activate / scenario.alternative.*
    ├── ImportHandlers.cs          ← import.epanet / import.swmm / import.data
    ├── ToolHandlers.cs            ← tool.topo-repair / tool.interpolate / tool.connection-repair / tool.catchment-process
    └── SimulateHandlers.cs        ← simulate.run
```

### Session state

`Session` holds one `AmeliaContext` per open database path, keyed by the resolved
absolute path.  Most commands include a `"database"` field to identify which context
to use.  If the path is not yet open, the session opens it automatically
(lazy-open behaviour removes the need for an explicit `model.open` in simple scripts).

### Handler contract

```csharp
interface ICommandHandler
{
    string Command { get; }    // e.g. "edit.insert"
    Task<JsonObject> HandleAsync(JsonObject cmd, Session session);
}
```

Returning a `JsonObject` instead of a typed DTO keeps the protocol open for
extension: handlers can include any fields in their response without changing
shared types.

### Dispatcher registration

```csharp
var dispatcher = new CommandDispatcher()
    .Register(new ModelOpenHandler())
    .Register(new ModelCloseHandler())
    .Register(new EditSelectHandler())
    .Register(new EditInsertHandler())
    // …
    ;
```

Adding a new command requires only: (a) implementing `ICommandHandler` and
(b) one `.Register(...)` call — no changes to argument parsing infrastructure.

---

## Example workflows

### One-shot query (equivalent to PR #113 style)

```bash
echo '{"command":"edit.select","database":"model.sqlite","table":"msm_Node","where":"Diameter > 0.5"}' \
  | mikeplus-json
```

### Bulk insert from a generator script

```bash
python generate_nodes.py | mikeplus-json
```

`generate_nodes.py` writes NDJSON:

```python
import json, sys
# First open the database
print(json.dumps({"id":"init","command":"model.open","database":"model.sqlite"}))
for i in range(1000):
    print(json.dumps({"command":"edit.insert","table":"msm_Node",
                      "row":{"MUID":f"N{i}","Diameter":round(0.3+i*0.001,3)}}))
print(json.dumps({"command":"model.close"}))
```

All 1 000 inserts share **one Amelia session** — the cost of opening the database
is paid once.

### AI agent workflow

An LLM agent emits a sequence of JSON commands and reads back structured results
without any shell quoting or argument-parsing concerns:

```jsonc
// Agent output → mikeplus-json stdin
{"id":"a1","command":"model.info","database":"urban_drainage.sqlite"}
{"id":"a2","command":"edit.select","table":"msm_Node","columns":["MUID","InvertLevel"]}
{"id":"a3","command":"tool.interpolate","method":"dem","targetTable":"msm_Node","targetAttr":"InvertLevel","demFile":"terrain.tif"}
{"id":"a4","command":"simulate.run","engine":"CS_MIKE_1D","muid":"Baseline"}
```

---

## Notes on Amelia bulk operations

Amelia's `IMuTable` API (`InsertByCommand`, `SetValuesByCommand`) is inherently
per-row.  The JSON streaming design handles bulk operations by keeping **one open
session** for the lifetime of the stream rather than by buffering all rows before
processing.  This is equivalent to what the MIKE+ GUI does when a user edits many
rows in a table — each edit goes through the same `DataTableContainer` and
`UndoRedoManager` without reopening the database.

The `AmeliaContext` class (see `cli/MikePlusCli/AmeliaContext.cs` in PR #113) is
reused unchanged; the architectural difference is solely in how the process loop
and dispatcher are structured.
