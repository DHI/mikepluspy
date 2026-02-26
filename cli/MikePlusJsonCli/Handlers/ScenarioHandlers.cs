using System.Text.Json.Nodes;

namespace MikePlusJsonCli.Handlers;

// ── scenario.list ────────────────────────────────────────────────────────────

/// <summary>
/// Lists all scenarios in the database via IScenarioManager.
///
/// Command fields: database (required)
/// </summary>
public sealed class ScenarioListHandler : ICommandHandler
{
    public string Command => "scenario.list";

    public Task<JsonObject> HandleAsync(JsonObject cmd, Session session)
    {
        var ctx       = session.GetOrOpen(HandlerHelper.Require(cmd, "database"));
        var scenarios = ctx.ScenarioManager.GetScenarios();
        var array     = new JsonArray();
        foreach (var s in scenarios)
            array.Add(new JsonObject { ["name"] = s.Name, ["parent"] = s.ParentName });

        return Task.FromResult(new JsonObject { ["data"] = array });
    }
}

// ── scenario.create ──────────────────────────────────────────────────────────

/// <summary>
/// Creates a new scenario.
///
/// Command fields: database (required), scenario (required), parent (optional)
/// </summary>
public sealed class ScenarioCreateHandler : ICommandHandler
{
    public string Command => "scenario.create";

    public Task<JsonObject> HandleAsync(JsonObject cmd, Session session)
    {
        var ctx    = session.GetOrOpen(HandlerHelper.Require(cmd, "database"));
        var name   = HandlerHelper.Require(cmd, "scenario");
        var parent = cmd["parent"]?.GetValue<string>() ?? "";

        ctx.ScenarioManager.CreateScenario(name, parent);
        return Task.FromResult(new JsonObject());
    }
}

// ── scenario.delete ──────────────────────────────────────────────────────────

/// <summary>
/// Deletes an existing scenario.
///
/// Command fields: database (required), scenario (required)
/// </summary>
public sealed class ScenarioDeleteHandler : ICommandHandler
{
    public string Command => "scenario.delete";

    public Task<JsonObject> HandleAsync(JsonObject cmd, Session session)
    {
        var ctx  = session.GetOrOpen(HandlerHelper.Require(cmd, "database"));
        var name = HandlerHelper.Require(cmd, "scenario");

        ctx.ScenarioManager.DeleteScenario(name);
        return Task.FromResult(new JsonObject());
    }
}

// ── scenario.activate ────────────────────────────────────────────────────────

/// <summary>
/// Activates a scenario so that all subsequent edit/tool/simulate commands
/// operate within its context.  The activated scenario persists in the open
/// AmeliaContext for the lifetime of the session — callers do not need to
/// repeat the scenario on every subsequent command.
///
/// Command fields: database (required), scenario (required)
/// </summary>
public sealed class ScenarioActivateHandler : ICommandHandler
{
    public string Command => "scenario.activate";

    public Task<JsonObject> HandleAsync(JsonObject cmd, Session session)
    {
        var ctx  = session.GetOrOpen(HandlerHelper.Require(cmd, "database"));
        var name = HandlerHelper.Require(cmd, "scenario");

        ctx.ScenarioManager.ActivateScenario(name);
        return Task.FromResult(new JsonObject());
    }
}

// ── scenario.alternative.list ────────────────────────────────────────────────

/// <summary>
/// Lists alternatives within a scenario alternative group.
///
/// Command fields: database (required), scenario (required), group (required)
/// </summary>
public sealed class ScenarioAlternativeListHandler : ICommandHandler
{
    public string Command => "scenario.alternative.list";

    public Task<JsonObject> HandleAsync(JsonObject cmd, Session session)
    {
        var ctx      = session.GetOrOpen(HandlerHelper.Require(cmd, "database"));
        var scenario = HandlerHelper.Require(cmd, "scenario");
        var group    = HandlerHelper.Require(cmd, "group");

        var alternatives = ctx.ScenarioManager.GetAlternatives(scenario, group);
        var array        = new JsonArray();
        foreach (var a in alternatives)
            array.Add(new JsonObject { ["name"] = a.Name });

        return Task.FromResult(new JsonObject { ["data"] = array });
    }
}

// ── scenario.alternative.set ─────────────────────────────────────────────────

/// <summary>
/// Sets the active alternative for a scenario/group pair.
///
/// Command fields: database (required), scenario (required), group (required), alternative (required)
/// </summary>
public sealed class ScenarioAlternativeSetHandler : ICommandHandler
{
    public string Command => "scenario.alternative.set";

    public Task<JsonObject> HandleAsync(JsonObject cmd, Session session)
    {
        var ctx         = session.GetOrOpen(HandlerHelper.Require(cmd, "database"));
        var scenario    = HandlerHelper.Require(cmd, "scenario");
        var group       = HandlerHelper.Require(cmd, "group");
        var alternative = HandlerHelper.Require(cmd, "alternative");

        ctx.ScenarioManager.SetAlternative(scenario, group, alternative);
        return Task.FromResult(new JsonObject());
    }
}

