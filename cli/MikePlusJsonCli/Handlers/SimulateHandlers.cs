using System.Text.Json.Nodes;
using DHI.Amelia.GlobalUtility.DataType;
using DHI.Amelia.Tools.EngineTool;
using DHI.Amelia.DomainServices.Interface.SharedEntity;
using System.Collections.Generic;

namespace MikePlusJsonCli.Handlers;

/// <summary>
/// Runs a MIKE+ simulation via Amelia's EngineTool and DhiEngineSimpleLauncher.
///
/// Command fields:
///   database (required),
///   engine   (required — "CS_MIKE_1D" | "CS_SWMM" | "WD_EPANET" | "CS_MIKE_1D_JobList"),
///   muid     (optional, defaults to the active simulation in the database)
///
/// The handler dispatches to EngineTool.RunEngine_CS, RunEngine_AllSWMM,
/// RunEngine_AllEpanet, or RunEngine_LTS_JobList exactly as the MIKE+ GUI does.
/// Because the AmeliaContext is already open for the session, there is no extra
/// database lifecycle cost — simulation follows naturally from any preceding
/// edit or scenario commands.
/// </summary>
public sealed class SimulateRunHandler : ICommandHandler
{
    public string Command => "simulate.run";

    public Task<JsonObject> HandleAsync(JsonObject cmd, Session session)
    {
        var ctx    = session.GetOrOpen(HandlerHelper.Require(cmd, "database"));
        var engine = HandlerHelper.Require(cmd, "engine");
        var muid   = cmd["muid"]?.GetValue<string>() ?? ctx.ActiveSimulation;

        var simOption = Enum.Parse<MUSimulationOption>(engine);
        var tool      = new EngineTool { DataTables = ctx.DataTables };
        var launcher  = new DhiEngineSimpleLauncher();
        var messages  = new List<string>();

        bool success;
        switch (simOption)
        {
            case MUSimulationOption.CS_MIKE_1D:
                (success, launcher, _) = tool.RunEngine_CS(launcher, messages, muid);
                break;
            case MUSimulationOption.CS_SWMM:
                (success, _) = tool.RunEngine_AllSWMM(default, messages, launcher, muid);
                break;
            case MUSimulationOption.WD_EPANET:
                (success, _) = tool.RunEngine_AllEpanet(simOption, default, messages, launcher, muid);
                break;
            case MUSimulationOption.CS_MIKE_1D_JobList:
                (success, launcher, _) = tool.RunEngine_LTS_JobList(launcher, messages, muid);
                break;
            default:
                throw new InvalidOperationException($"Unsupported engine '{engine}'.");
        }

        if (!success || launcher is null)
            throw new InvalidOperationException(
                $"Simulation failed to start: {string.Join("; ", messages)}");

        launcher.Start();

        // Wait for completion (mirrors SimulationRunner in the Python package).
        var timeout = DateTime.UtcNow.AddSeconds(30);
        while (!launcher.IsEngineRunning && DateTime.UtcNow < timeout)
            Thread.Sleep(100);
        while (launcher.IsEngineRunning)
            Thread.Sleep(100);

        return Task.FromResult(new JsonObject());
    }
}

