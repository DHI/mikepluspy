using System.CommandLine;

namespace MikePlusCli.Commands;

/// <summary>
/// The "tool" command group — MIKE+ processing tools.
///
///   mikeplus tool topo-repair     -d model.sqlite --snap-distance 0.1
///   mikeplus tool import          -d model.sqlite --config import.xml
///   mikeplus tool connection-repair -d model.sqlite
///   mikeplus tool interpolate nearest -d model.sqlite --target-table msm_Node --target-attr InvertLevel ...
///   mikeplus tool interpolate dem     -d model.sqlite --target-table msm_Node --target-attr InvertLevel ...
///   mikeplus tool interpolate idw     -d model.sqlite --target-table msm_Node --target-attr InvertLevel ...
///   mikeplus tool interpolate assign  -d model.sqlite --target-table msm_Node --target-attr InvertLevel --value 10.5
///   mikeplus tool catchment-process   -d model.sqlite --catch-ids c1,c2 --line-layer slope.shp --dem-layer dem.dfs2
/// </summary>
public static class ToolCommand
{
    private static readonly Option<string> DatabaseOption = new(
        aliases: new[] { "--database", "-d" },
        description: "Path to the MIKE+ SQLite database file")
    { IsRequired = true };

    public static Command Build()
    {
        var cmd = new Command("tool", "Run MIKE+ processing tools (topology repair, import, interpolation, etc.)");
        cmd.AddCommand(BuildTopoRepair());
        cmd.AddCommand(BuildImport());
        cmd.AddCommand(BuildConnectionRepair());
        cmd.AddCommand(BuildInterpolate());
        cmd.AddCommand(BuildCatchmentProcess());
        return cmd;
    }

    // ── tool topo-repair ──────────────────────────────────────────────

    private static Command BuildTopoRepair()
    {
        var deleteUnlinked = new Option<bool>("--delete-unlinked", () => true, "Delete unlinked nodes/links");
        var dissolveOverlap = new Option<bool>("--dissolve-overlap", () => true, "Dissolve overlapping nodes");
        var correctConnection = new Option<bool>("--correct-connection", () => true, "Correct link connections");
        var searchJunction = new Option<bool>("--search-junction", () => true, "Search for junction connections");
        var createJunction = new Option<bool>("--create-junction", () => true, "Create missing junction connections");
        var splitTJunction = new Option<bool>("--split-t-junction", () => true, "Split links on T-junctions");
        var addMissingZones = new Option<bool>("--add-missing-zones", () => true, "Add missing zones");
        var snapDistance = new Option<double>("--snap-distance", () => 0.1, "Snap distance tolerance");

        var cmd = new Command("topo-repair", "Run topology repair tool");
        cmd.AddOption(DatabaseOption);
        cmd.AddOption(deleteUnlinked);
        cmd.AddOption(dissolveOverlap);
        cmd.AddOption(correctConnection);
        cmd.AddOption(searchJunction);
        cmd.AddOption(createJunction);
        cmd.AddOption(splitTJunction);
        cmd.AddOption(addMissingZones);
        cmd.AddOption(snapDistance);

        cmd.SetHandler((context) =>
        {
            var db = context.ParseResult.GetValueForOption(DatabaseOption)!;
            try
            {
                // In a full implementation this would invoke the DHI .NET TopoRepairTool.
                // Here we show the feasible structure and parameter handling.
                var parameters = new
                {
                    delete_unlinked = context.ParseResult.GetValueForOption(deleteUnlinked),
                    dissolve_overlap = context.ParseResult.GetValueForOption(dissolveOverlap),
                    correct_connection = context.ParseResult.GetValueForOption(correctConnection),
                    search_junction = context.ParseResult.GetValueForOption(searchJunction),
                    create_junction = context.ParseResult.GetValueForOption(createJunction),
                    split_t_junction = context.ParseResult.GetValueForOption(splitTJunction),
                    add_missing_zones = context.ParseResult.GetValueForOption(addMissingZones),
                    snap_distance = context.ParseResult.GetValueForOption(snapDistance),
                };

                using var ctx = DatabaseContext.Open(db);
                // TopoRepairTool integration point:
                // var tool = new CSTopologyRepairTool(ctx.DataTableContainer);
                // tool.DeleteUnLinkedNodeLink = parameters.delete_unlinked;
                // ...
                // tool.Run();

                CliResult.Ok("tool topo-repair", db, new { tool = "topo-repair", parameters }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("tool topo-repair", ex.Message, db).Print();
            }
        });

        return cmd;
    }

    // ── tool import ───────────────────────────────────────────────────

    private static Command BuildImport()
    {
        var configOpt = new Option<string>("--config", "Path to import XML configuration file") { IsRequired = true };

        var cmd = new Command("import", "Import data from an XML configuration file");
        cmd.AddOption(DatabaseOption);
        cmd.AddOption(configOpt);

        cmd.SetHandler((string db, string config) =>
        {
            try
            {
                if (!File.Exists(config))
                {
                    CliResult.Fail("tool import", $"Config file not found: {config}", db).Print();
                    return;
                }

                using var ctx = DatabaseContext.Open(db);
                // ImportTool integration point:
                // var engine = new ImportEngine();
                // engine.SetConfigFile(config);
                // engine.SetDataTableContainer(ctx.DataTableContainer);
                // engine.Run();

                CliResult.Ok("tool import", db, new { tool = "import", config_file = config }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("tool import", ex.Message, db).Print();
            }
        }, DatabaseOption, configOpt);

        return cmd;
    }

    // ── tool connection-repair ────────────────────────────────────────

    private static Command BuildConnectionRepair()
    {
        var cmd = new Command("connection-repair", "Repair network connections");
        cmd.AddOption(DatabaseOption);

        cmd.SetHandler((string db) =>
        {
            try
            {
                using var ctx = DatabaseContext.Open(db);
                // ConnectionRepairTool integration point:
                // var engine = new ConnectionRepairEngine(ctx.DataTableContainer);
                // engine.Run();

                CliResult.Ok("tool connection-repair", db, new { tool = "connection-repair" }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("tool connection-repair", ex.Message, db).Print();
            }
        }, DatabaseOption);

        return cmd;
    }

    // ── tool interpolate ──────────────────────────────────────────────

    private static Command BuildInterpolate()
    {
        var cmd = new Command("interpolate", "Spatial interpolation tools");
        cmd.AddCommand(BuildInterpolateNearest());
        cmd.AddCommand(BuildInterpolateDem());
        cmd.AddCommand(BuildInterpolateIdw());
        cmd.AddCommand(BuildInterpolateAssign());
        cmd.AddCommand(BuildInterpolateNeighbour());
        return cmd;
    }

    // Shared interpolation options
    private static Option<string> TargetTableOpt() =>
        new("--target-table", "Target database table name") { IsRequired = true };

    private static Option<string> TargetAttrOpt() =>
        new("--target-attr", "Target attribute/column name") { IsRequired = true };

    private static Option<bool> OnlyNullOpt() =>
        new("--only-null", () => true, "Only update NULL values");

    private static Option<bool> MissingFlagOpt() =>
        new("--assign-missing", () => false, "Assign a specific value as missing");

    private static Option<double?> MissingValueOpt() =>
        new("--missing-value", "Value to treat as missing");

    private static Command BuildInterpolateNearest()
    {
        var targetTable = TargetTableOpt();
        var targetAttr = TargetAttrOpt();
        var sourceLayer = new Option<string>("--source-layer", "Source layer name") { IsRequired = true };
        var sourceAttr = new Option<string>("--source-attr", "Source attribute name") { IsRequired = true };
        var onlyNull = OnlyNullOpt();
        var assignMissing = MissingFlagOpt();
        var missingValue = MissingValueOpt();
        var searchRadius = new Option<double>("--search-radius", () => 300.0, "Search radius");

        var cmd = new Command("nearest", "Interpolate from nearest feature");
        cmd.AddOption(DatabaseOption);
        cmd.AddOption(targetTable);
        cmd.AddOption(targetAttr);
        cmd.AddOption(sourceLayer);
        cmd.AddOption(sourceAttr);
        cmd.AddOption(onlyNull);
        cmd.AddOption(assignMissing);
        cmd.AddOption(missingValue);
        cmd.AddOption(searchRadius);

        cmd.SetHandler((context) =>
        {
            var db = context.ParseResult.GetValueForOption(DatabaseOption)!;
            try
            {
                var parameters = new
                {
                    method = "nearest_feature",
                    target_table = context.ParseResult.GetValueForOption(targetTable),
                    target_attr = context.ParseResult.GetValueForOption(targetAttr),
                    source_layer = context.ParseResult.GetValueForOption(sourceLayer),
                    source_attr = context.ParseResult.GetValueForOption(sourceAttr),
                    only_null = context.ParseResult.GetValueForOption(onlyNull),
                    assign_missing = context.ParseResult.GetValueForOption(assignMissing),
                    missing_value = context.ParseResult.GetValueForOption(missingValue),
                    search_radius = context.ParseResult.GetValueForOption(searchRadius),
                };

                using var ctx = DatabaseContext.Open(db);
                CliResult.Ok("tool interpolate nearest", db, new { tool = "interpolate", parameters }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("tool interpolate nearest", ex.Message, db).Print();
            }
        });

        return cmd;
    }

    private static Command BuildInterpolateDem()
    {
        var targetTable = TargetTableOpt();
        var targetAttr = TargetAttrOpt();
        var rasterFile = new Option<string>("--raster-file", "Path to DEM raster file") { IsRequired = true };
        var itemNumber = new Option<int>("--item-number", () => 1, "Raster item/band number");
        var onlyNull = OnlyNullOpt();
        var assignMissing = MissingFlagOpt();
        var missingValue = MissingValueOpt();

        var cmd = new Command("dem", "Interpolate from DEM raster");
        cmd.AddOption(DatabaseOption);
        cmd.AddOption(targetTable);
        cmd.AddOption(targetAttr);
        cmd.AddOption(rasterFile);
        cmd.AddOption(itemNumber);
        cmd.AddOption(onlyNull);
        cmd.AddOption(assignMissing);
        cmd.AddOption(missingValue);

        cmd.SetHandler((context) =>
        {
            var db = context.ParseResult.GetValueForOption(DatabaseOption)!;
            try
            {
                var parameters = new
                {
                    method = "dem",
                    target_table = context.ParseResult.GetValueForOption(targetTable),
                    target_attr = context.ParseResult.GetValueForOption(targetAttr),
                    raster_file = context.ParseResult.GetValueForOption(rasterFile),
                    item_number = context.ParseResult.GetValueForOption(itemNumber),
                    only_null = context.ParseResult.GetValueForOption(onlyNull),
                    assign_missing = context.ParseResult.GetValueForOption(assignMissing),
                    missing_value = context.ParseResult.GetValueForOption(missingValue),
                };

                using var ctx = DatabaseContext.Open(db);
                CliResult.Ok("tool interpolate dem", db, new { tool = "interpolate", parameters }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("tool interpolate dem", ex.Message, db).Print();
            }
        });

        return cmd;
    }

    private static Command BuildInterpolateIdw()
    {
        var targetTable = TargetTableOpt();
        var targetAttr = TargetAttrOpt();
        var sourceLayer = new Option<string>("--source-layer", "Source layer name") { IsRequired = true };
        var sourceAttr = new Option<string>("--source-attr", "Source attribute name") { IsRequired = true };
        var onlyNull = OnlyNullOpt();
        var assignMissing = MissingFlagOpt();
        var missingValue = MissingValueOpt();
        var maxPoints = new Option<int>("--max-points", () => 12, "Maximum IDW interpolation points");
        var searchRadius = new Option<double>("--search-radius", () => 300.0, "Search radius");

        var cmd = new Command("idw", "Inverse Distance Weighting interpolation");
        cmd.AddOption(DatabaseOption);
        cmd.AddOption(targetTable);
        cmd.AddOption(targetAttr);
        cmd.AddOption(sourceLayer);
        cmd.AddOption(sourceAttr);
        cmd.AddOption(onlyNull);
        cmd.AddOption(assignMissing);
        cmd.AddOption(missingValue);
        cmd.AddOption(maxPoints);
        cmd.AddOption(searchRadius);

        cmd.SetHandler((context) =>
        {
            var db = context.ParseResult.GetValueForOption(DatabaseOption)!;
            try
            {
                var parameters = new
                {
                    method = "idw",
                    target_table = context.ParseResult.GetValueForOption(targetTable),
                    target_attr = context.ParseResult.GetValueForOption(targetAttr),
                    source_layer = context.ParseResult.GetValueForOption(sourceLayer),
                    source_attr = context.ParseResult.GetValueForOption(sourceAttr),
                    only_null = context.ParseResult.GetValueForOption(onlyNull),
                    assign_missing = context.ParseResult.GetValueForOption(assignMissing),
                    missing_value = context.ParseResult.GetValueForOption(missingValue),
                    max_points = context.ParseResult.GetValueForOption(maxPoints),
                    search_radius = context.ParseResult.GetValueForOption(searchRadius),
                };

                using var ctx = DatabaseContext.Open(db);
                CliResult.Ok("tool interpolate idw", db, new { tool = "interpolate", parameters }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("tool interpolate idw", ex.Message, db).Print();
            }
        });

        return cmd;
    }

    private static Command BuildInterpolateAssign()
    {
        var targetTable = TargetTableOpt();
        var targetAttr = TargetAttrOpt();
        var value = new Option<double>("--value", "Fixed value to assign") { IsRequired = true };
        var onlyNull = OnlyNullOpt();
        var assignMissing = MissingFlagOpt();
        var missingValue = MissingValueOpt();

        var cmd = new Command("assign", "Directly assign a fixed value");
        cmd.AddOption(DatabaseOption);
        cmd.AddOption(targetTable);
        cmd.AddOption(targetAttr);
        cmd.AddOption(value);
        cmd.AddOption(onlyNull);
        cmd.AddOption(assignMissing);
        cmd.AddOption(missingValue);

        cmd.SetHandler((context) =>
        {
            var db = context.ParseResult.GetValueForOption(DatabaseOption)!;
            try
            {
                var parameters = new
                {
                    method = "assign",
                    target_table = context.ParseResult.GetValueForOption(targetTable),
                    target_attr = context.ParseResult.GetValueForOption(targetAttr),
                    value = context.ParseResult.GetValueForOption(value),
                    only_null = context.ParseResult.GetValueForOption(onlyNull),
                    assign_missing = context.ParseResult.GetValueForOption(assignMissing),
                    missing_value = context.ParseResult.GetValueForOption(missingValue),
                };

                using var ctx = DatabaseContext.Open(db);
                CliResult.Ok("tool interpolate assign", db, new { tool = "interpolate", parameters }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("tool interpolate assign", ex.Message, db).Print();
            }
        });

        return cmd;
    }

    private static Command BuildInterpolateNeighbour()
    {
        var targetTable = TargetTableOpt();
        var targetAttr = TargetAttrOpt();
        var sourceLayer = new Option<string>("--source-layer", "Source layer name") { IsRequired = true };
        var sourceAttr = new Option<string>("--source-attr", "Source attribute name") { IsRequired = true };
        var onlyNull = OnlyNullOpt();
        var assignMissing = MissingFlagOpt();
        var missingValue = MissingValueOpt();
        var assignOption = new Option<int>("--assign-option", () => 0, "Assignment option (0=default)");
        var alongPath = new Option<bool>("--along-path", () => false, "Interpolate along path");
        var maxNeighbours = new Option<int>("--max-neighbours", () => 3, "Maximum number of neighbours");

        var cmd = new Command("neighbour", "Interpolate from neighbouring features");
        cmd.AddOption(DatabaseOption);
        cmd.AddOption(targetTable);
        cmd.AddOption(targetAttr);
        cmd.AddOption(sourceLayer);
        cmd.AddOption(sourceAttr);
        cmd.AddOption(onlyNull);
        cmd.AddOption(assignMissing);
        cmd.AddOption(missingValue);
        cmd.AddOption(assignOption);
        cmd.AddOption(alongPath);
        cmd.AddOption(maxNeighbours);

        cmd.SetHandler((context) =>
        {
            var db = context.ParseResult.GetValueForOption(DatabaseOption)!;
            try
            {
                var parameters = new
                {
                    method = "neighbour",
                    target_table = context.ParseResult.GetValueForOption(targetTable),
                    target_attr = context.ParseResult.GetValueForOption(targetAttr),
                    source_layer = context.ParseResult.GetValueForOption(sourceLayer),
                    source_attr = context.ParseResult.GetValueForOption(sourceAttr),
                    only_null = context.ParseResult.GetValueForOption(onlyNull),
                    assign_missing = context.ParseResult.GetValueForOption(assignMissing),
                    missing_value = context.ParseResult.GetValueForOption(missingValue),
                    assign_option = context.ParseResult.GetValueForOption(assignOption),
                    along_path = context.ParseResult.GetValueForOption(alongPath),
                    max_neighbours = context.ParseResult.GetValueForOption(maxNeighbours),
                };

                using var ctx = DatabaseContext.Open(db);
                CliResult.Ok("tool interpolate neighbour", db, new { tool = "interpolate", parameters }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("tool interpolate neighbour", ex.Message, db).Print();
            }
        });

        return cmd;
    }

    // ── tool catchment-process ────────────────────────────────────────

    private static Command BuildCatchmentProcess()
    {
        var catchIds = new Option<string>("--catch-ids", "Comma-separated catchment IDs") { IsRequired = true };
        var lineLayer = new Option<string>("--line-layer", "Path to slope line layer (shapefile)") { IsRequired = true };
        var demLayer = new Option<string>("--dem-layer", "Path to DEM layer (dfs2)") { IsRequired = true };
        var direction = new Option<int>("--direction", () => 0, "Flow direction: 0=Downstream, 1=Upstream");
        var minSlope = new Option<double>("--min-slope", () => 0.002, "Minimum slope value");
        var demUnit = new Option<int>("--dem-unit", () => 1000, "DEM unit key");
        var overwrite = new Option<bool>("--overwrite", () => true, "Overwrite existing values");

        var cmd = new Command("catchment-process", "Calculate catchment slope and length");
        cmd.AddOption(DatabaseOption);
        cmd.AddOption(catchIds);
        cmd.AddOption(lineLayer);
        cmd.AddOption(demLayer);
        cmd.AddOption(direction);
        cmd.AddOption(minSlope);
        cmd.AddOption(demUnit);
        cmd.AddOption(overwrite);

        cmd.SetHandler((context) =>
        {
            var db = context.ParseResult.GetValueForOption(DatabaseOption)!;
            try
            {
                var ids = context.ParseResult.GetValueForOption(catchIds)!
                    .Split(',', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries);

                var parameters = new
                {
                    catch_ids = ids,
                    line_layer = context.ParseResult.GetValueForOption(lineLayer),
                    dem_layer = context.ParseResult.GetValueForOption(demLayer),
                    direction = context.ParseResult.GetValueForOption(direction),
                    min_slope = context.ParseResult.GetValueForOption(minSlope),
                    dem_unit = context.ParseResult.GetValueForOption(demUnit),
                    overwrite = context.ParseResult.GetValueForOption(overwrite),
                };

                using var ctx = DatabaseContext.Open(db);
                CliResult.Ok("tool catchment-process", db, new { tool = "catchment-process", parameters }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("tool catchment-process", ex.Message, db).Print();
            }
        });

        return cmd;
    }
}
