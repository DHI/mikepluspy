using System.Text.Json.Nodes;
using System.Threading;
using DHI.Amelia.EPANETBridge;
using DHI.Amelia.SWMMBridge;

namespace MikePlusJsonCli.Handlers;

// ── import.epanet ────────────────────────────────────────────────────────────

/// <summary>
/// Imports a network from an EPANET .inp file via Amelia's INPBridge.
///
/// Command fields: database (required), file (required)
/// </summary>
public sealed class ImportEpanetHandler : ICommandHandler
{
    public string Command => "import.epanet";

    public Task<JsonObject> HandleAsync(JsonObject cmd, Session session)
    {
        var ctx      = session.GetOrOpen(HandlerHelper.Require(cmd, "database"));
        var filePath = HandlerHelper.Require(cmd, "file");

        var bridge = new INPBridge(ctx.DataTables, null);
        var cts    = new CancellationTokenSource();

        if (!bridge.Import(filePath, cts.Token))
        {
            var errors = string.Join("; ", bridge.ErrorMsgs.Cast<string>());
            throw new InvalidOperationException($"EPANET import failed: {errors}");
        }

        return Task.FromResult(new JsonObject());
    }
}

// ── import.swmm ──────────────────────────────────────────────────────────────

/// <summary>
/// Imports a network from a SWMM .inp file via Amelia's SWMMStorageBridge.
///
/// Command fields: database (required), file (required)
/// </summary>
public sealed class ImportSwmmHandler : ICommandHandler
{
    public string Command => "import.swmm";

    public Task<JsonObject> HandleAsync(JsonObject cmd, Session session)
    {
        var ctx      = session.GetOrOpen(HandlerHelper.Require(cmd, "database"));
        var filePath = HandlerHelper.Require(cmd, "file");

        var bridge = new SWMMStorageBridge(ctx.DataTables, null);
        var cts    = new CancellationTokenSource();

        if (!bridge.Import(filePath, cts.Token))
        {
            var errors = string.Join("; ", bridge.ErrorMsgs.Cast<string>());
            throw new InvalidOperationException($"SWMM import failed: {errors}");
        }

        return Task.FromResult(new JsonObject());
    }
}

// ── import.data ──────────────────────────────────────────────────────────────

/// <summary>
/// Runs a data import from an XML configuration file via Amelia's ImportToolBase.
///
/// Command fields: database (required), config (required path to XML import config)
/// </summary>
public sealed class ImportDataHandler : ICommandHandler
{
    public string Command => "import.data";

    public Task<JsonObject> HandleAsync(JsonObject cmd, Session session)
    {
        var ctx        = session.GetOrOpen(HandlerHelper.Require(cmd, "database"));
        var configPath = HandlerHelper.Require(cmd, "config");

        ctx.ImportData(configPath);
        return Task.FromResult(new JsonObject());
    }
}

