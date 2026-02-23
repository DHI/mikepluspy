using System.CommandLine;

namespace MikePlusCli.Commands;

/// <summary>
/// The "table" command group — CRUD on any MIKE+ table.
///
///   mikeplus table select msm_Node -d model.sqlite --columns Diameter,InvertLevel
///   mikeplus table select msm_Node -d model.sqlite --where "Diameter > 0.5" --order-by Diameter --descending
///   mikeplus table insert msm_Node -d model.sqlite --set MUID=N1 --set Diameter=1.5
///   mikeplus table update msm_Node -d model.sqlite --set Diameter=2.0 --where "MUID = 'N1'"
///   mikeplus table delete msm_Node -d model.sqlite --where "MUID = 'N1'"
///   mikeplus table delete msm_Node -d model.sqlite --all
/// </summary>
public static class TableCommand
{
    private static readonly Option<string> DatabaseOption = new(
        aliases: new[] { "--database", "-d" },
        description: "Path to the MIKE+ SQLite database file")
    { IsRequired = true };

    public static Command Build()
    {
        var cmd = new Command("table", "Read and write rows in MIKE+ tables (select, insert, update, delete)");
        cmd.AddCommand(BuildSelect());
        cmd.AddCommand(BuildInsert());
        cmd.AddCommand(BuildUpdate());
        cmd.AddCommand(BuildDelete());
        return cmd;
    }

    // ── Shared options ────────────────────────────────────────────────

    private static Argument<string> TableArg(string desc = "Table name (e.g. msm_Node, msm_Link, mw_Pipe)")
        => new("table", desc);

    private static Option<string[]> SetOption()
        => new("--set", "Column=Value pair (repeatable)")
        {
            AllowMultipleArgumentsPerToken = true,
            Arity = ArgumentArity.OneOrMore,
        };

    private static Dictionary<string, string> ParseSetValues(string[] pairs)
    {
        var dict = new Dictionary<string, string>(StringComparer.OrdinalIgnoreCase);
        foreach (var pair in pairs)
        {
            var eqIdx = pair.IndexOf('=');
            if (eqIdx <= 0)
                throw new ArgumentException($"Invalid --set value '{pair}'. Expected Column=Value.");
            dict[pair[..eqIdx].Trim()] = pair[(eqIdx + 1)..].Trim();
        }
        return dict;
    }

    // ── table select ──────────────────────────────────────────────────

    private static Command BuildSelect()
    {
        var tableArg = TableArg();
        var columnsOpt = new Option<string?>("--columns", "Comma-separated column names (default: all)");
        var whereOpt = new Option<string?>("--where", "SQL WHERE clause (without the WHERE keyword)");
        var orderByOpt = new Option<string?>("--order-by", "Column to sort by");
        var descOpt = new Option<bool>("--descending", () => false, "Sort in descending order");

        var cmd = new Command("select", "Query rows from a table");
        cmd.AddArgument(tableArg);
        cmd.AddOption(DatabaseOption);
        cmd.AddOption(columnsOpt);
        cmd.AddOption(whereOpt);
        cmd.AddOption(orderByOpt);
        cmd.AddOption(descOpt);

        cmd.SetHandler((string table, string db, string? columns, string? where, string? orderBy, bool desc) =>
        {
            try
            {
                using var ctx = DatabaseContext.Open(db);
                var cols = columns?.Split(',', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries);
                var rows = ctx.Select(table, cols, where, orderBy, desc);
                CliResult.Ok("table select", db, new { table, row_count = rows.Count, rows }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("table select", ex.Message, db).Print();
            }
        }, tableArg, DatabaseOption, columnsOpt, whereOpt, orderByOpt, descOpt);

        return cmd;
    }

    // ── table insert ──────────────────────────────────────────────────

    private static Command BuildInsert()
    {
        var tableArg = TableArg();
        var setOpt = SetOption();

        var cmd = new Command("insert", "Insert a row into a table");
        cmd.AddArgument(tableArg);
        cmd.AddOption(DatabaseOption);
        cmd.AddOption(setOpt);

        cmd.SetHandler((string table, string db, string[] sets) =>
        {
            try
            {
                var values = ParseSetValues(sets);
                using var ctx = DatabaseContext.Open(db);
                var muid = ctx.Insert(table, values);
                CliResult.Ok("table insert", db, new { table, muid }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("table insert", ex.Message, db).Print();
            }
        }, tableArg, DatabaseOption, setOpt);

        return cmd;
    }

    // ── table update ──────────────────────────────────────────────────

    private static Command BuildUpdate()
    {
        var tableArg = TableArg();
        var setOpt = SetOption();
        var whereOpt = new Option<string?>("--where", "SQL WHERE clause (required unless --all is given)");
        var allOpt = new Option<bool>("--all", () => false, "Update ALL rows (safety flag)");

        var cmd = new Command("update", "Update rows in a table");
        cmd.AddArgument(tableArg);
        cmd.AddOption(DatabaseOption);
        cmd.AddOption(setOpt);
        cmd.AddOption(whereOpt);
        cmd.AddOption(allOpt);

        cmd.SetHandler((string table, string db, string[] sets, string? where, bool all) =>
        {
            try
            {
                var values = ParseSetValues(sets);
                using var ctx = DatabaseContext.Open(db);
                var affected = ctx.Update(table, values, where, all);
                CliResult.Ok("table update", db, new { table, affected_rows = affected }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("table update", ex.Message, db).Print();
            }
        }, tableArg, DatabaseOption, setOpt, whereOpt, allOpt);

        return cmd;
    }

    // ── table delete ──────────────────────────────────────────────────

    private static Command BuildDelete()
    {
        var tableArg = TableArg();
        var whereOpt = new Option<string?>("--where", "SQL WHERE clause (required unless --all is given)");
        var allOpt = new Option<bool>("--all", () => false, "Delete ALL rows (safety flag)");

        var cmd = new Command("delete", "Delete rows from a table");
        cmd.AddArgument(tableArg);
        cmd.AddOption(DatabaseOption);
        cmd.AddOption(whereOpt);
        cmd.AddOption(allOpt);

        cmd.SetHandler((string table, string db, string? where, bool all) =>
        {
            try
            {
                using var ctx = DatabaseContext.Open(db);
                var affected = ctx.Delete(table, where, all);
                CliResult.Ok("table delete", db, new { table, affected_rows = affected }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("table delete", ex.Message, db).Print();
            }
        }, tableArg, DatabaseOption, whereOpt, allOpt);

        return cmd;
    }
}
