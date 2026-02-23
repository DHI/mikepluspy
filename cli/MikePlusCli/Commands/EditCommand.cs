using System.CommandLine;
using System.Text.Json;

namespace MikePlusCli.Commands;

/// <summary>
/// The "edit" command group — read and write model data through Amelia's IMuTable.
///
/// Unlike raw SQL, these operations go through the Amelia query engine which
/// respects scenarios, alternatives, undo/redo, and geometry handling.
///
/// Single-row usage (via --set flags):
///   mikeplus edit select msm_Node -d model.sqlite --columns Diameter,InvertLevel
///   mikeplus edit select msm_Node -d model.sqlite --where "Diameter > 0.5" --order-by Diameter
///   mikeplus edit insert msm_Node -d model.sqlite --set MUID=N1 --set Diameter=1.5
///   mikeplus edit update msm_Node -d model.sqlite --set Diameter=2.0 --where "MUID='N1'"
///   mikeplus edit delete msm_Node -d model.sqlite --where "MUID='N1'"
///
/// Bulk usage (via --input file or stdin):
///   mikeplus edit insert msm_Node -d model.sqlite --input nodes.json
///   cat nodes.json | mikeplus edit insert msm_Node -d model.sqlite --input -
///   mikeplus edit update msm_Node -d model.sqlite --input updates.json --where "TypeNo=1"
///
/// The --input file must be a JSON array of objects, where each object maps column
/// names to values.  Example:
///   [
///     {"MUID": "N1", "Diameter": 1.5, "InvertLevel": 10.0},
///     {"MUID": "N2", "Diameter": 2.0, "InvertLevel": 12.5}
///   ]
/// </summary>
public static class EditCommand
{
    public static Command Build()
    {
        var cmd = new Command("edit", "Read and write model data via the Amelia query engine");
        cmd.AddCommand(BuildSelect());
        cmd.AddCommand(BuildInsert());
        cmd.AddCommand(BuildUpdate());
        cmd.AddCommand(BuildDelete());
        return cmd;
    }

    // ── Helpers ───────────────────────────────────────────────────────

    private static Argument<string> TableArg()
        => new("table", "Model table name (e.g. msm_Node, msm_Link, mw_Pipe)");

    private static Option<string[]> SetOption()
        => new("--set", "Column=Value pair (repeatable, for single-row operations)")
        {
            AllowMultipleArgumentsPerToken = true,
            Arity = ArgumentArity.ZeroOrMore,
        };

    private static Option<string?> InputOption()
        => new("--input", "Path to JSON file with row data, or '-' for stdin (for bulk operations)");

    private static Dictionary<string, object> ParseSetValues(string[] pairs)
    {
        var dict = new Dictionary<string, object>(StringComparer.OrdinalIgnoreCase);
        foreach (var pair in pairs)
        {
            var eqIdx = pair.IndexOf('=');
            if (eqIdx <= 0)
                throw new ArgumentException($"Invalid --set value '{pair}'. Expected Column=Value.");
            var key = pair[..eqIdx].Trim();
            var raw = pair[(eqIdx + 1)..].Trim();
            dict[key] = ParseValue(raw);
        }
        return dict;
    }

    private static object ParseValue(string raw)
    {
        if (string.Equals(raw, "NULL", StringComparison.OrdinalIgnoreCase))
            return DBNull.Value;
        if (long.TryParse(raw, out var l))
            return l;
        if (double.TryParse(raw, System.Globalization.NumberStyles.Float,
                System.Globalization.CultureInfo.InvariantCulture, out var d))
            return d;
        return raw;
    }

    /// <summary>
    /// Read bulk row data from a JSON file or stdin.
    /// Returns a list of column→value dictionaries.
    /// </summary>
    private static List<Dictionary<string, object>> ReadBulkInput(string inputPath)
    {
        string json;
        if (inputPath == "-")
        {
            json = Console.In.ReadToEnd();
        }
        else
        {
            if (!File.Exists(inputPath))
                throw new FileNotFoundException($"Input file not found: {inputPath}");
            json = File.ReadAllText(inputPath);
        }

        var rows = JsonSerializer.Deserialize<List<Dictionary<string, JsonElement>>>(json)
            ?? throw new InvalidOperationException(
                "Failed to parse input JSON. Expected a JSON array of objects, e.g. [{\"MUID\":\"N1\",\"Diameter\":1.5}, ...].");

        return rows.Select(row =>
        {
            var dict = new Dictionary<string, object>(StringComparer.OrdinalIgnoreCase);
            foreach (var kv in row)
            {
                dict[kv.Key] = kv.Value.ValueKind switch
                {
                    JsonValueKind.Number when kv.Value.TryGetInt64(out var lv) => (object)lv,
                    JsonValueKind.Number => kv.Value.GetDouble(),
                    JsonValueKind.True => true,
                    JsonValueKind.False => false,
                    JsonValueKind.Null => DBNull.Value,
                    _ => kv.Value.GetString() ?? "",
                };
            }
            return dict;
        }).ToList();
    }

    // ── edit select ───────────────────────────────────────────────────

    private static Command BuildSelect()
    {
        var tableArg = TableArg();
        var dbOpt = SharedOptions.Database();
        var columnsOpt = new Option<string?>("--columns", "Comma-separated column names (default: all)");
        var whereOpt = new Option<string?>("--where", "Filter expression (Amelia WHERE syntax)");
        var orderByOpt = new Option<string?>("--order-by", "Column to sort by");
        var descOpt = new Option<bool>("--descending", () => false, "Sort descending");

        var cmd = new Command("select", "Query rows from a model table");
        cmd.AddArgument(tableArg);
        cmd.AddOption(dbOpt);
        cmd.AddOption(columnsOpt);
        cmd.AddOption(whereOpt);
        cmd.AddOption(orderByOpt);
        cmd.AddOption(descOpt);

        cmd.SetHandler((string table, string db, string? columns, string? where, string? orderBy, bool desc) =>
        {
            try
            {
                using var ctx = AmeliaContext.Open(db);
                var cols = columns?.Split(',', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries);
                var result = ctx.SelectRows(table, cols, where, orderBy, desc);
                var rowCount = result?.Count ?? 0;
                CliResult.Ok("edit select", db, new { table, row_count = rowCount, rows = result }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("edit select", ex.Message, db).Print();
            }
        }, tableArg, dbOpt, columnsOpt, whereOpt, orderByOpt, descOpt);

        return cmd;
    }

    // ── edit insert ───────────────────────────────────────────────────

    private static Command BuildInsert()
    {
        var tableArg = TableArg();
        var dbOpt = SharedOptions.Database();
        var setOpt = SetOption();
        var inputOpt = InputOption();

        var cmd = new Command("insert",
            "Insert rows into a model table (use --set for one row, --input for bulk)");
        cmd.AddArgument(tableArg);
        cmd.AddOption(dbOpt);
        cmd.AddOption(setOpt);
        cmd.AddOption(inputOpt);

        cmd.SetHandler((string table, string db, string[] sets, string? input) =>
        {
            try
            {
                using var ctx = AmeliaContext.Open(db);

                if (!string.IsNullOrEmpty(input))
                {
                    // Bulk insert from JSON file or stdin
                    var rows = ReadBulkInput(input);
                    var muids = ctx.InsertRows(table, rows);
                    CliResult.Ok("edit insert", db, new
                    {
                        table,
                        inserted_rows = muids.Count,
                        muids,
                    }).Print();
                }
                else if (sets.Length > 0)
                {
                    // Single-row insert from --set flags
                    var values = ParseSetValues(sets);
                    var muid = ctx.InsertRow(table, values);
                    CliResult.Ok("edit insert", db, new
                    {
                        table,
                        inserted_rows = 1,
                        muids = new[] { muid },
                    }).Print();
                }
                else
                {
                    CliResult.Fail("edit insert",
                        "Provide --set Column=Value pairs or --input <file|-> for bulk insert.", db).Print();
                }
            }
            catch (Exception ex)
            {
                CliResult.Fail("edit insert", ex.Message, db).Print();
            }
        }, tableArg, dbOpt, setOpt, inputOpt);

        return cmd;
    }

    // ── edit update ───────────────────────────────────────────────────

    private static Command BuildUpdate()
    {
        var tableArg = TableArg();
        var dbOpt = SharedOptions.Database();
        var setOpt = SetOption();
        var inputOpt = InputOption();
        var whereOpt = new Option<string?>("--where", "Filter expression (required unless --all)");
        var allOpt = new Option<bool>("--all", () => false, "Apply to ALL rows (safety flag)");

        var cmd = new Command("update",
            "Update rows (--set for uniform values, --input for per-row values keyed by MUID)");
        cmd.AddArgument(tableArg);
        cmd.AddOption(dbOpt);
        cmd.AddOption(setOpt);
        cmd.AddOption(inputOpt);
        cmd.AddOption(whereOpt);
        cmd.AddOption(allOpt);

        cmd.SetHandler((context) =>
        {
            var table = context.ParseResult.GetValueForArgument(tableArg);
            var db = context.ParseResult.GetValueForOption(dbOpt)!;
            var sets = context.ParseResult.GetValueForOption(setOpt) ?? Array.Empty<string>();
            var input = context.ParseResult.GetValueForOption(inputOpt);
            var where = context.ParseResult.GetValueForOption(whereOpt);
            var all = context.ParseResult.GetValueForOption(allOpt);

            try
            {
                using var ctx = AmeliaContext.Open(db);

                if (!string.IsNullOrEmpty(input))
                {
                    // Bulk per-row update: each JSON object must contain a MUID key
                    var rows = ReadBulkInput(input);
                    var updated = ctx.UpdateRowsBulk(table, rows);
                    CliResult.Ok("edit update", db, new
                    {
                        table,
                        affected_rows = updated.Count,
                        muids = updated,
                    }).Print();
                }
                else if (sets.Length > 0)
                {
                    // Uniform update: apply same values to all matching rows
                    var values = ParseSetValues(sets);
                    var updated = ctx.UpdateRows(table, values, where, all);
                    CliResult.Ok("edit update", db, new
                    {
                        table,
                        affected_rows = updated.Count,
                        muids = updated,
                    }).Print();
                }
                else
                {
                    CliResult.Fail("edit update",
                        "Provide --set Column=Value pairs or --input <file|-> for bulk update.", db).Print();
                }
            }
            catch (Exception ex)
            {
                CliResult.Fail("edit update", ex.Message, db).Print();
            }
        });

        return cmd;
    }

    // ── edit delete ───────────────────────────────────────────────────

    private static Command BuildDelete()
    {
        var tableArg = TableArg();
        var dbOpt = SharedOptions.Database();
        var whereOpt = new Option<string?>("--where", "Filter expression (required unless --all)");
        var allOpt = new Option<bool>("--all", () => false, "Delete ALL rows (safety flag)");

        var cmd = new Command("delete", "Delete rows from a model table");
        cmd.AddArgument(tableArg);
        cmd.AddOption(dbOpt);
        cmd.AddOption(whereOpt);
        cmd.AddOption(allOpt);

        cmd.SetHandler((string table, string db, string? where, bool all) =>
        {
            try
            {
                using var ctx = AmeliaContext.Open(db);
                var deleted = ctx.DeleteRows(table, where, all);
                CliResult.Ok("edit delete", db, new { table, affected_rows = deleted.Count, muids = deleted }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("edit delete", ex.Message, db).Print();
            }
        }, tableArg, dbOpt, whereOpt, allOpt);

        return cmd;
    }
}
