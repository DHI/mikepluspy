using System.CommandLine;

namespace MikePlusCli.Commands;

/// <summary>
/// The "edit" command group — read and write model data through Amelia's IMuTable.
///
/// Unlike raw SQL, these operations go through the Amelia query engine which
/// respects scenarios, alternatives, undo/redo, and geometry handling.
///
///   mikeplus edit select msm_Node -d model.sqlite --columns Diameter,InvertLevel
///   mikeplus edit select msm_Node -d model.sqlite --where "Diameter &gt; 0.5" --order-by Diameter
///   mikeplus edit insert msm_Node -d model.sqlite --set MUID=N1 --set Diameter=1.5
///   mikeplus edit update msm_Node -d model.sqlite --set Diameter=2.0 --where "MUID='N1'"
///   mikeplus edit delete msm_Node -d model.sqlite --where "MUID='N1'"
///   mikeplus edit delete msm_Node -d model.sqlite --all
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
        => new("--set", "Column=Value pair (repeatable)")
        {
            AllowMultipleArgumentsPerToken = true,
            Arity = ArgumentArity.OneOrMore,
        };

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

        var cmd = new Command("insert", "Insert a row into a model table");
        cmd.AddArgument(tableArg);
        cmd.AddOption(dbOpt);
        cmd.AddOption(setOpt);

        cmd.SetHandler((string table, string db, string[] sets) =>
        {
            try
            {
                var values = ParseSetValues(sets);
                using var ctx = AmeliaContext.Open(db);
                var muid = ctx.InsertRow(table, values);
                CliResult.Ok("edit insert", db, new { table, muid }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("edit insert", ex.Message, db).Print();
            }
        }, tableArg, dbOpt, setOpt);

        return cmd;
    }

    // ── edit update ───────────────────────────────────────────────────

    private static Command BuildUpdate()
    {
        var tableArg = TableArg();
        var dbOpt = SharedOptions.Database();
        var setOpt = SetOption();
        var whereOpt = new Option<string?>("--where", "Filter expression (required unless --all)");
        var allOpt = new Option<bool>("--all", () => false, "Apply to ALL rows (safety flag)");

        var cmd = new Command("update", "Update rows in a model table");
        cmd.AddArgument(tableArg);
        cmd.AddOption(dbOpt);
        cmd.AddOption(setOpt);
        cmd.AddOption(whereOpt);
        cmd.AddOption(allOpt);

        cmd.SetHandler((string table, string db, string[] sets, string? where, bool all) =>
        {
            try
            {
                var values = ParseSetValues(sets);
                using var ctx = AmeliaContext.Open(db);
                var updated = ctx.UpdateRows(table, values, where, all);
                CliResult.Ok("edit update", db, new { table, affected_rows = updated.Count, muids = updated }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("edit update", ex.Message, db).Print();
            }
        }, tableArg, dbOpt, setOpt, whereOpt, allOpt);

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
