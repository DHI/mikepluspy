using System.Text.Json.Nodes;

namespace MikePlusJsonCli.Handlers;

// ── tool.topo-repair ─────────────────────────────────────────────────────────

/// <summary>
/// Runs the topology repair tool (CSTopologyRepairTool / WDTopologyRepairTool)
/// to fix network connectivity issues.
///
/// Command fields:
///   database       (required),
///   snapDistance   (optional float, default 0.1),
///   deleteUnlinked (optional bool, default false)
/// </summary>
public sealed class ToolTopoRepairHandler : ICommandHandler
{
    public string Command => "tool.topo-repair";

    public Task<JsonObject> HandleAsync(JsonObject cmd, Session session)
    {
        var ctx            = session.GetOrOpen(HandlerHelper.Require(cmd, "database"));
        var snapDistance   = cmd["snapDistance"]?.GetValue<double>() ?? 0.1;
        var deleteUnlinked = cmd["deleteUnlinked"]?.GetValue<bool>() ?? false;

        ctx.RunTopoRepair(snapDistance, deleteUnlinked);
        return Task.FromResult(new JsonObject());
    }
}

// ── tool.connection-repair ───────────────────────────────────────────────────

/// <summary>
/// Runs the connection repair engine to fix broken node/link connections.
///
/// Command fields: database (required)
/// </summary>
public sealed class ToolConnectionRepairHandler : ICommandHandler
{
    public string Command => "tool.connection-repair";

    public Task<JsonObject> HandleAsync(JsonObject cmd, Session session)
    {
        var ctx = session.GetOrOpen(HandlerHelper.Require(cmd, "database"));
        ctx.RunConnectionRepair();
        return Task.FromResult(new JsonObject());
    }
}

// ── tool.interpolate ─────────────────────────────────────────────────────────

/// <summary>
/// Runs the interpolation engine to assign elevation or attribute values to
/// network elements from an external source (DEM, point layer, etc.).
///
/// Command fields:
///   database     (required),
///   method       (required — "nearest" | "dem" | "idw" | "assign" | "neighbour"),
///   targetTable  (required),
///   targetAttr   (required),
///   sourceLayer  (required for non-DEM methods),
///   sourceAttr   (required for non-DEM methods),
///   demFile      (required for "dem" method)
/// </summary>
public sealed class ToolInterpolateHandler : ICommandHandler
{
    public string Command => "tool.interpolate";

    public Task<JsonObject> HandleAsync(JsonObject cmd, Session session)
    {
        var ctx         = session.GetOrOpen(HandlerHelper.Require(cmd, "database"));
        var method      = HandlerHelper.Require(cmd, "method");
        var targetTable = HandlerHelper.Require(cmd, "targetTable");
        var targetAttr  = HandlerHelper.Require(cmd, "targetAttr");
        var sourceLayer = cmd["sourceLayer"]?.GetValue<string>() ?? "";
        var sourceAttr  = cmd["sourceAttr"]?.GetValue<string>() ?? "";
        var demFile     = cmd["demFile"]?.GetValue<string>() ?? "";

        ctx.RunInterpolation(method, targetTable, targetAttr, sourceLayer, sourceAttr, demFile);
        return Task.FromResult(new JsonObject());
    }
}

// ── tool.catchment-process ───────────────────────────────────────────────────

/// <summary>
/// Runs the catchment slope/length processing tool (CatchmentSlope).
///
/// Command fields: database (required)
/// </summary>
public sealed class ToolCatchmentProcessHandler : ICommandHandler
{
    public string Command => "tool.catchment-process";

    public Task<JsonObject> HandleAsync(JsonObject cmd, Session session)
    {
        var ctx = session.GetOrOpen(HandlerHelper.Require(cmd, "database"));
        ctx.RunCatchmentProcess();
        return Task.FromResult(new JsonObject());
    }
}

