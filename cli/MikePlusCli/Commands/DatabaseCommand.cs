using System.CommandLine;

namespace MikePlusCli.Commands;

/// <summary>
/// The "database" command group.
///
///   mikeplus database info     --database model.sqlite
///   mikeplus database create   --database new.sqlite --projection "PROJCS[...]" --srid 32632
///   mikeplus database tables   --database model.sqlite
///   mikeplus database columns  --database model.sqlite --table msm_Node
/// </summary>
public static class DatabaseCommand
{
    private static readonly Option<string> DatabaseOption = new(
        aliases: new[] { "--database", "-d" },
        description: "Path to the MIKE+ SQLite database file")
    { IsRequired = true };

    public static Command Build()
    {
        var cmd = new Command("database", "Open, create, and inspect MIKE+ databases");
        cmd.AddCommand(BuildInfo());
        cmd.AddCommand(BuildCreate());
        cmd.AddCommand(BuildTables());
        cmd.AddCommand(BuildColumns());
        return cmd;
    }

    // ── database info ─────────────────────────────────────────────────

    private static Command BuildInfo()
    {
        var cmd = new Command("info", "Show database metadata (projection, version, unit system, table list)");
        cmd.AddOption(DatabaseOption);

        cmd.SetHandler((string db) =>
        {
            try
            {
                using var ctx = DatabaseContext.Open(db);
                CliResult.Ok("database info", db, ctx.GetProjectInfo()).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("database info", ex.Message, db).Print();
            }
        }, DatabaseOption);

        return cmd;
    }

    // ── database create ───────────────────────────────────────────────

    private static Command BuildCreate()
    {
        var projOpt = new Option<string>("--projection", () => "", "Projection string (WKT)");
        var sridOpt = new Option<int>("--srid", () => -1, "Spatial Reference ID");
        var overwriteOpt = new Option<bool>("--overwrite", () => false, "Overwrite if file exists");

        var cmd = new Command("create", "Create a new MIKE+ database");
        cmd.AddOption(DatabaseOption);
        cmd.AddOption(projOpt);
        cmd.AddOption(sridOpt);
        cmd.AddOption(overwriteOpt);

        cmd.SetHandler((string db, string proj, int srid, bool overwrite) =>
        {
            try
            {
                using var ctx = DatabaseContext.Create(db, proj, srid, overwrite);
                CliResult.Ok("database create", db, new { created = true }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("database create", ex.Message, db).Print();
            }
        }, DatabaseOption, projOpt, sridOpt, overwriteOpt);

        return cmd;
    }

    // ── database tables ───────────────────────────────────────────────

    private static Command BuildTables()
    {
        var cmd = new Command("tables", "List all tables in the database");
        cmd.AddOption(DatabaseOption);

        cmd.SetHandler((string db) =>
        {
            try
            {
                using var ctx = DatabaseContext.Open(db);
                CliResult.Ok("database tables", db, ctx.GetTableNames()).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("database tables", ex.Message, db).Print();
            }
        }, DatabaseOption);

        return cmd;
    }

    // ── database columns ──────────────────────────────────────────────

    private static Command BuildColumns()
    {
        var tableOpt = new Option<string>("--table", "Table name to inspect") { IsRequired = true };

        var cmd = new Command("columns", "List columns and types for a table");
        cmd.AddOption(DatabaseOption);
        cmd.AddOption(tableOpt);

        cmd.SetHandler((string db, string table) =>
        {
            try
            {
                using var ctx = DatabaseContext.Open(db);
                CliResult.Ok("database columns", db, ctx.GetTableColumns(table)).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("database columns", ex.Message, db).Print();
            }
        }, DatabaseOption, tableOpt);

        return cmd;
    }
}
