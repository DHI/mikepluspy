using System.CommandLine;

namespace MikePlusCli.Commands;

/// <summary>
/// The "model" command group — create, open, and inspect MIKE+ models.
///
/// Wraps <c>BaseDataSource.Create / OpenDatabase / CloseDatabase</c> and
/// <c>DataTableContainer</c> metadata.
///
///   mikeplus model create  -d model.sqlite --projection "PROJCS[…]" --srid 32632
///   mikeplus model info    -d model.sqlite
///   mikeplus model tables  -d model.sqlite
///   mikeplus model columns -d model.sqlite --table msm_Node
/// </summary>
public static class ModelCommand
{
    public static Command Build()
    {
        var cmd = new Command("model", "Create, open, and inspect MIKE+ model databases");
        cmd.AddCommand(BuildCreate());
        cmd.AddCommand(BuildInfo());
        cmd.AddCommand(BuildTables());
        cmd.AddCommand(BuildColumns());
        return cmd;
    }

    // ── model create ──────────────────────────────────────────────────

    private static Command BuildCreate()
    {
        var dbOpt = SharedOptions.Database();
        var projOpt = new Option<string>("--projection", () => "", "Coordinate system as WKT projection string");
        var sridOpt = new Option<int>("--srid", () => -1, "Spatial Reference ID (EPSG code)");

        var cmd = new Command("create", "Create a new MIKE+ model database with Amelia");
        cmd.AddOption(dbOpt);
        cmd.AddOption(projOpt);
        cmd.AddOption(sridOpt);

        cmd.SetHandler((string db, string proj, int srid) =>
        {
            try
            {
                using var ctx = AmeliaContext.Create(db, proj, srid);
                CliResult.Ok("model create", db, new { created = true, projection = proj, srid }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("model create", ex.Message, db).Print();
            }
        }, dbOpt, projOpt, sridOpt);

        return cmd;
    }

    // ── model info ────────────────────────────────────────────────────

    private static Command BuildInfo()
    {
        var dbOpt = SharedOptions.Database();

        var cmd = new Command("info", "Display model metadata (projection, version, active model, simulation)");
        cmd.AddOption(dbOpt);

        cmd.SetHandler((string db) =>
        {
            try
            {
                using var ctx = AmeliaContext.Open(db);
                CliResult.Ok("model info", db, new
                {
                    projection = ctx.ProjectionString,
                    srid = ctx.Srid,
                    version = ctx.Version,
                    active_model = ctx.ActiveModel.ToString(),
                    active_simulation = ctx.ActiveSimulation,
                }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("model info", ex.Message, db).Print();
            }
        }, dbOpt);

        return cmd;
    }

    // ── model tables ──────────────────────────────────────────────────

    private static Command BuildTables()
    {
        var dbOpt = SharedOptions.Database();

        var cmd = new Command("tables", "List all model tables registered in the Amelia container");
        cmd.AddOption(dbOpt);

        cmd.SetHandler((string db) =>
        {
            try
            {
                using var ctx = AmeliaContext.Open(db);
                var names = ctx.GetTableNames();
                CliResult.Ok("model tables", db, new { count = names.Count, tables = names }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("model tables", ex.Message, db).Print();
            }
        }, dbOpt);

        return cmd;
    }

    // ── model columns ─────────────────────────────────────────────────

    private static Command BuildColumns()
    {
        var dbOpt = SharedOptions.Database();
        var tableOpt = new Option<string>("--table", "Table name (e.g. msm_Node, mw_Pipe)") { IsRequired = true };

        var cmd = new Command("columns", "List columns and types for a model table");
        cmd.AddOption(dbOpt);
        cmd.AddOption(tableOpt);

        cmd.SetHandler((string db, string table) =>
        {
            try
            {
                using var ctx = AmeliaContext.Open(db);
                var muTable = ctx.GetTable(table);
                // Column metadata comes from the IMuTable schema
                CliResult.Ok("model columns", db, new
                {
                    table = muTable.TableName,
                    display_name = muTable.TableDisplayName,
                    description = muTable.Description,
                }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("model columns", ex.Message, db).Print();
            }
        }, dbOpt, tableOpt);

        return cmd;
    }
}
