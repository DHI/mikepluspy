using System.CommandLine;
using DHI.Amelia.GlobalUtility.DataType;

namespace MikePlusCli.Commands;

/// <summary>
/// The "tool" command group — MIKE+ analysis and repair tools backed by
/// Amelia's tool engines.  Each sub-command wraps the same engine class
/// used by the corresponding MIKE+ GUI tool.
///
///   mikeplus tool topo-repair       -d model.sqlite --snap-distance 0.1
///   mikeplus tool connection-repair -d model.sqlite
///   mikeplus tool interpolate nearest -d model.sqlite --target-table msm_Node …
///   mikeplus tool interpolate dem     -d model.sqlite --target-table msm_Node …
///   mikeplus tool interpolate idw     -d model.sqlite …
///   mikeplus tool interpolate assign  -d model.sqlite …
///   mikeplus tool interpolate neighbour -d model.sqlite …
///   mikeplus tool catchment-process -d model.sqlite --catch-ids c1,c2 …
/// </summary>
public static class ToolCommand
{
    public static Command Build()
    {
        var cmd = new Command("tool", "Run MIKE+ analysis and repair tools (topology, interpolation, etc.)");
        cmd.AddCommand(BuildTopoRepair());
        cmd.AddCommand(BuildConnectionRepair());
        cmd.AddCommand(BuildInterpolate());
        cmd.AddCommand(BuildCatchmentProcess());
        return cmd;
    }

    // ── tool topo-repair ──────────────────────────────────────────────

    private static Command BuildTopoRepair()
    {
        var dbOpt = SharedOptions.Database();
        var deleteUnlinked = new Option<bool>("--delete-unlinked", () => true, "Delete unlinked nodes/links");
        var dissolveOverlap = new Option<bool>("--dissolve-overlap", () => true, "Dissolve overlapping nodes");
        var correctConnection = new Option<bool>("--correct-connection", () => true, "Correct link connections");
        var searchJunction = new Option<bool>("--search-junction", () => true, "Search for junction connections");
        var createJunction = new Option<bool>("--create-junction", () => true, "Create missing junction connections");
        var splitTJunction = new Option<bool>("--split-t-junction", () => true, "Split links on T-junctions");
        var addMissingZones = new Option<bool>("--add-missing-zones", () => true, "Add missing zones");
        var snapDistance = new Option<double>("--snap-distance", () => 0.1, "Snap distance tolerance");

        var cmd = new Command("topo-repair", "Run topology repair (CSTopologyRepairTool / WDTopologyRepairTool)");
        cmd.AddOption(dbOpt);
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
            var db = context.ParseResult.GetValueForOption(dbOpt)!;
            try
            {
                using var ctx = AmeliaContext.Open(db);

                var param = new DHI.Amelia.Tools.TopologyRepairTool.TopologyRepairParam
                {
                    DeleteUnLinkedNodeLink = context.ParseResult.GetValueForOption(deleteUnlinked),
                    DissolveOverlapNode = context.ParseResult.GetValueForOption(dissolveOverlap),
                    CorrectLinkConnection = context.ParseResult.GetValueForOption(correctConnection),
                    SearchJunctionConnection = context.ParseResult.GetValueForOption(searchJunction),
                    CreateJunctionConnection = context.ParseResult.GetValueForOption(createJunction),
                    SplitLinkOnTjunction = context.ParseResult.GetValueForOption(splitTJunction),
                    AddMissingZones = context.ParseResult.GetValueForOption(addMissingZones),
                    SnapDistance = context.ParseResult.GetValueForOption(snapDistance),
                };

                var cts = new CancellationTokenSource();

                // Choose CS or WD tool based on the active model
                if (ctx.ActiveModel == MUModelOption.CS)
                {
                    var tool = new DHI.Amelia.Tools.TopologyRepairTool.CSTopologyRepairTool(ctx.DataTables);
                    tool.Run(param, cts.Token, false);
                }
                else
                {
                    var tool = new DHI.Amelia.Tools.TopologyRepairTool.WDTopologyRepairTool(ctx.DataTables);
                    tool.Run(param, cts.Token, false);
                }

                CliResult.Ok("tool topo-repair", db, new { completed = true }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("tool topo-repair", ex.Message, db).Print();
            }
        });

        return cmd;
    }

    // ── tool connection-repair ────────────────────────────────────────

    private static Command BuildConnectionRepair()
    {
        var dbOpt = SharedOptions.Database();

        var cmd = new Command("connection-repair", "Repair network connections (ConnectionRepairEngine)");
        cmd.AddOption(dbOpt);

        cmd.SetHandler((string db) =>
        {
            try
            {
                using var ctx = AmeliaContext.Open(db);
                var engine = new DHI.Amelia.Tools.ConnectionRepairEngine.ConnectionRepairEngine(ctx.DataTables);
                engine.Run();
                CliResult.Ok("tool connection-repair", db, new { completed = true }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("tool connection-repair", ex.Message, db).Print();
            }
        }, dbOpt);

        return cmd;
    }

    // ── tool interpolate ──────────────────────────────────────────────

    private static Command BuildInterpolate()
    {
        var cmd = new Command("interpolate", "Spatial interpolation tools (InterpolationEngine)");
        cmd.AddCommand(BuildInterpolateNearest());
        cmd.AddCommand(BuildInterpolateDem());
        cmd.AddCommand(BuildInterpolateIdw());
        cmd.AddCommand(BuildInterpolateAssign());
        cmd.AddCommand(BuildInterpolateNeighbour());
        return cmd;
    }

    // Shared interpolation options
    private static Option<string> TargetTableOpt() =>
        new("--target-table", "Target model table name") { IsRequired = true };

    private static Option<string> TargetAttrOpt() =>
        new("--target-attr", "Target attribute/column name") { IsRequired = true };

    private static Option<bool> OnlyNullOpt() =>
        new("--only-null", () => true, "Only update NULL values");

    private static Option<bool> MissingFlagOpt() =>
        new("--assign-missing", () => false, "Assign a value as missing marker");

    private static Option<double?> MissingValueOpt() =>
        new("--missing-value", "Value to treat as missing");

    private static void RunInterpolation(AmeliaContext ctx,
        DHI.Amelia.Tools.InterpolationEngine.InterpolationToolParameters param)
    {
        var engine = new DHI.Amelia.Tools.InterpolationEngine.InterpolationEngine(ctx.DataTables);
        var messages = new List<string>();
        engine.Run(param, false, messages);
    }

    private static Command BuildInterpolateNearest()
    {
        var dbOpt = SharedOptions.Database();
        var targetTable = TargetTableOpt();
        var targetAttr = TargetAttrOpt();
        var sourceLayer = new Option<string>("--source-layer", "Source layer name") { IsRequired = true };
        var sourceAttr = new Option<string>("--source-attr", "Source attribute name") { IsRequired = true };
        var onlyNull = OnlyNullOpt();
        var assignMissing = MissingFlagOpt();
        var missingValue = MissingValueOpt();
        var searchRadius = new Option<double>("--search-radius", () => 300.0, "Search radius");

        var cmd = new Command("nearest", "Interpolate from nearest feature");
        cmd.AddOption(dbOpt);
        cmd.AddOption(targetTable); cmd.AddOption(targetAttr);
        cmd.AddOption(sourceLayer); cmd.AddOption(sourceAttr);
        cmd.AddOption(onlyNull); cmd.AddOption(assignMissing);
        cmd.AddOption(missingValue); cmd.AddOption(searchRadius);

        cmd.SetHandler((context) =>
        {
            var db = context.ParseResult.GetValueForOption(dbOpt)!;
            try
            {
                using var ctx = AmeliaContext.Open(db);

                var param = new DHI.Amelia.Tools.InterpolationEngine.InterpolationToolParameters
                {
                    TargetDbName = context.ParseResult.GetValueForOption(targetTable)!,
                    TargetAttribute = context.ParseResult.GetValueForOption(targetAttr)!,
                    SourceLayerName = context.ParseResult.GetValueForOption(sourceLayer)!,
                    SourceAttribute = context.ParseResult.GetValueForOption(sourceAttr)!,
                    OnlyNullValues = context.ParseResult.GetValueForOption(onlyNull),
                    AssignValAsMissing = context.ParseResult.GetValueForOption(assignMissing),
                    SearchRadius = context.ParseResult.GetValueForOption(searchRadius),
                    InterpolationMethod = 0, // Nearest feature
                };

                var mv = context.ParseResult.GetValueForOption(missingValue);
                if (mv.HasValue) param.ValueAsMissing = mv.Value;

                RunInterpolation(ctx, param);
                CliResult.Ok("tool interpolate nearest", db, new { completed = true }).Print();
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
        var dbOpt = SharedOptions.Database();
        var targetTable = TargetTableOpt();
        var targetAttr = TargetAttrOpt();
        var rasterFile = new Option<string>("--raster-file", "Path to DEM raster file") { IsRequired = true };
        var itemNumber = new Option<int>("--item-number", () => 1, "Raster item/band number");
        var onlyNull = OnlyNullOpt();
        var assignMissing = MissingFlagOpt();
        var missingValue = MissingValueOpt();

        var cmd = new Command("dem", "Interpolate from DEM raster");
        cmd.AddOption(dbOpt);
        cmd.AddOption(targetTable); cmd.AddOption(targetAttr);
        cmd.AddOption(rasterFile); cmd.AddOption(itemNumber);
        cmd.AddOption(onlyNull); cmd.AddOption(assignMissing);
        cmd.AddOption(missingValue);

        cmd.SetHandler((context) =>
        {
            var db = context.ParseResult.GetValueForOption(dbOpt)!;
            try
            {
                using var ctx = AmeliaContext.Open(db);

                var param = new DHI.Amelia.Tools.InterpolationEngine.InterpolationToolParameters
                {
                    TargetDbName = context.ParseResult.GetValueForOption(targetTable)!,
                    TargetAttribute = context.ParseResult.GetValueForOption(targetAttr)!,
                    RasterFile = context.ParseResult.GetValueForOption(rasterFile)!,
                    ItemNumber = context.ParseResult.GetValueForOption(itemNumber),
                    OnlyNullValues = context.ParseResult.GetValueForOption(onlyNull),
                    AssignValAsMissing = context.ParseResult.GetValueForOption(assignMissing),
                    InterpolationMethod = 1, // DEM
                };

                var mv = context.ParseResult.GetValueForOption(missingValue);
                if (mv.HasValue) param.ValueAsMissing = mv.Value;

                RunInterpolation(ctx, param);
                CliResult.Ok("tool interpolate dem", db, new { completed = true }).Print();
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
        var dbOpt = SharedOptions.Database();
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
        cmd.AddOption(dbOpt);
        cmd.AddOption(targetTable); cmd.AddOption(targetAttr);
        cmd.AddOption(sourceLayer); cmd.AddOption(sourceAttr);
        cmd.AddOption(onlyNull); cmd.AddOption(assignMissing);
        cmd.AddOption(missingValue);
        cmd.AddOption(maxPoints); cmd.AddOption(searchRadius);

        cmd.SetHandler((context) =>
        {
            var db = context.ParseResult.GetValueForOption(dbOpt)!;
            try
            {
                using var ctx = AmeliaContext.Open(db);

                var param = new DHI.Amelia.Tools.InterpolationEngine.InterpolationToolParameters
                {
                    TargetDbName = context.ParseResult.GetValueForOption(targetTable)!,
                    TargetAttribute = context.ParseResult.GetValueForOption(targetAttr)!,
                    SourceLayerName = context.ParseResult.GetValueForOption(sourceLayer)!,
                    SourceAttribute = context.ParseResult.GetValueForOption(sourceAttr)!,
                    OnlyNullValues = context.ParseResult.GetValueForOption(onlyNull),
                    AssignValAsMissing = context.ParseResult.GetValueForOption(assignMissing),
                    MaxIdwPoints = context.ParseResult.GetValueForOption(maxPoints),
                    SearchRadius = context.ParseResult.GetValueForOption(searchRadius),
                    InterpolationMethod = 2, // IDW
                };

                var mv = context.ParseResult.GetValueForOption(missingValue);
                if (mv.HasValue) param.ValueAsMissing = mv.Value;

                RunInterpolation(ctx, param);
                CliResult.Ok("tool interpolate idw", db, new { completed = true }).Print();
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
        var dbOpt = SharedOptions.Database();
        var targetTable = TargetTableOpt();
        var targetAttr = TargetAttrOpt();
        var value = new Option<double>("--value", "Fixed value to assign") { IsRequired = true };
        var onlyNull = OnlyNullOpt();
        var assignMissing = MissingFlagOpt();
        var missingValue = MissingValueOpt();

        var cmd = new Command("assign", "Directly assign a fixed value to a column");
        cmd.AddOption(dbOpt);
        cmd.AddOption(targetTable); cmd.AddOption(targetAttr);
        cmd.AddOption(value);
        cmd.AddOption(onlyNull); cmd.AddOption(assignMissing);
        cmd.AddOption(missingValue);

        cmd.SetHandler((context) =>
        {
            var db = context.ParseResult.GetValueForOption(dbOpt)!;
            try
            {
                using var ctx = AmeliaContext.Open(db);

                var param = new DHI.Amelia.Tools.InterpolationEngine.InterpolationToolParameters
                {
                    TargetDbName = context.ParseResult.GetValueForOption(targetTable)!,
                    TargetAttribute = context.ParseResult.GetValueForOption(targetAttr)!,
                    FixedValue = context.ParseResult.GetValueForOption(value),
                    OnlyNullValues = context.ParseResult.GetValueForOption(onlyNull),
                    AssignValAsMissing = context.ParseResult.GetValueForOption(assignMissing),
                    InterpolationMethod = 3, // Direct assign
                };

                var mv = context.ParseResult.GetValueForOption(missingValue);
                if (mv.HasValue) param.ValueAsMissing = mv.Value;

                RunInterpolation(ctx, param);
                CliResult.Ok("tool interpolate assign", db, new { completed = true }).Print();
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
        var dbOpt = SharedOptions.Database();
        var targetTable = TargetTableOpt();
        var targetAttr = TargetAttrOpt();
        var sourceLayer = new Option<string>("--source-layer", "Source layer name") { IsRequired = true };
        var sourceAttr = new Option<string>("--source-attr", "Source attribute name") { IsRequired = true };
        var onlyNull = OnlyNullOpt();
        var assignMissing = MissingFlagOpt();
        var missingValue = MissingValueOpt();
        var assignOption = new Option<int>("--assign-option", () => 0, "Assignment strategy (0=default)");
        var alongPath = new Option<bool>("--along-path", () => false, "Interpolate along flow path");
        var maxNeighbours = new Option<int>("--max-neighbours", () => 3, "Maximum number of neighbours");

        var cmd = new Command("neighbour", "Interpolate from neighbouring features");
        cmd.AddOption(dbOpt);
        cmd.AddOption(targetTable); cmd.AddOption(targetAttr);
        cmd.AddOption(sourceLayer); cmd.AddOption(sourceAttr);
        cmd.AddOption(onlyNull); cmd.AddOption(assignMissing);
        cmd.AddOption(missingValue);
        cmd.AddOption(assignOption); cmd.AddOption(alongPath);
        cmd.AddOption(maxNeighbours);

        cmd.SetHandler((context) =>
        {
            var db = context.ParseResult.GetValueForOption(dbOpt)!;
            try
            {
                using var ctx = AmeliaContext.Open(db);

                var param = new DHI.Amelia.Tools.InterpolationEngine.InterpolationToolParameters
                {
                    TargetDbName = context.ParseResult.GetValueForOption(targetTable)!,
                    TargetAttribute = context.ParseResult.GetValueForOption(targetAttr)!,
                    SourceLayerName = context.ParseResult.GetValueForOption(sourceLayer)!,
                    SourceAttribute = context.ParseResult.GetValueForOption(sourceAttr)!,
                    OnlyNullValues = context.ParseResult.GetValueForOption(onlyNull),
                    AssignValAsMissing = context.ParseResult.GetValueForOption(assignMissing),
                    AssignOption = context.ParseResult.GetValueForOption(assignOption),
                    AlongPath = context.ParseResult.GetValueForOption(alongPath),
                    MaxNeighbours = context.ParseResult.GetValueForOption(maxNeighbours),
                    InterpolationMethod = 4, // Neighbour
                };

                var mv = context.ParseResult.GetValueForOption(missingValue);
                if (mv.HasValue) param.ValueAsMissing = mv.Value;

                RunInterpolation(ctx, param);
                CliResult.Ok("tool interpolate neighbour", db, new { completed = true }).Print();
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
        var dbOpt = SharedOptions.Database();
        var catchIds = new Option<string>("--catch-ids", "Comma-separated catchment MUIDs") { IsRequired = true };
        var lineLayer = new Option<string>("--line-layer", "Path to slope line layer (shapefile)") { IsRequired = true };
        var demLayer = new Option<string>("--dem-layer", "Path to DEM layer (dfs2 file)") { IsRequired = true };
        var direction = new Option<int>("--direction", () => 0, "Flow direction: 0=Downstream, 1=Upstream");
        var minSlope = new Option<double>("--min-slope", () => 0.002, "Minimum slope value");
        var demUnit = new Option<int>("--dem-unit", () => 1000, "DEM unit key (eumUnit code)");
        var overwrite = new Option<bool>("--overwrite", () => true, "Overwrite existing values");

        var cmd = new Command("catchment-process", "Calculate catchment slope and length (CatchmentSlope engine)");
        cmd.AddOption(dbOpt);
        cmd.AddOption(catchIds); cmd.AddOption(lineLayer);
        cmd.AddOption(demLayer); cmd.AddOption(direction);
        cmd.AddOption(minSlope); cmd.AddOption(demUnit);
        cmd.AddOption(overwrite);

        cmd.SetHandler((context) =>
        {
            var db = context.ParseResult.GetValueForOption(dbOpt)!;
            try
            {
                using var ctx = AmeliaContext.Open(db);

                var ids = context.ParseResult.GetValueForOption(catchIds)!
                    .Split(',', StringSplitOptions.RemoveEmptyEntries | StringSplitOptions.TrimEntries);

                var catchList = new List<string>(ids);
                var warnings = new List<string>();

                var unit = new DHI.Generic.MikeZero.eumUnit(
                    context.ParseResult.GetValueForOption(demUnit));

                var tool = new DHI.Amelia.Tools.CatchmentProcessing.CatchmentSlope(ctx.DataTables);
                tool.CalculateSlopeLength(
                    catchList,
                    context.ParseResult.GetValueForOption(overwrite),
                    context.ParseResult.GetValueForOption(minSlope),
                    context.ParseResult.GetValueForOption(direction),
                    context.ParseResult.GetValueForOption(lineLayer)!,
                    context.ParseResult.GetValueForOption(demLayer)!,
                    0, // method
                    unit,
                    warnings);

                CliResult.Ok("tool catchment-process", db, new
                {
                    completed = true,
                    catchment_count = ids.Length,
                    warnings,
                }).Print();
            }
            catch (Exception ex)
            {
                CliResult.Fail("tool catchment-process", ex.Message, db).Print();
            }
        });

        return cmd;
    }
}
