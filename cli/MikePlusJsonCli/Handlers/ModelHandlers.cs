using System.Text.Json.Nodes;

namespace MikePlusJsonCli.Handlers;

// ── model.open ──────────────────────────────────────────────────────────────

/// <summary>
/// Opens an existing MIKE+ database and registers it in the session.
/// Subsequent commands that reference the same path reuse this context.
///
/// Command fields: database (required)
/// </summary>
public sealed class ModelOpenHandler : ICommandHandler
{
    public string Command => "model.open";

    public Task<JsonObject> HandleAsync(JsonObject cmd, Session session)
    {
        var db = HandlerHelper.Require(cmd, "database");
        if (!session.IsOpen(db))
            session.Register(AmeliaContext.Open(db));

        return Task.FromResult(new JsonObject());
    }
}

// ── model.close ─────────────────────────────────────────────────────────────

/// <summary>
/// Closes the Amelia context for the specified database, flushing the undo
/// buffer and releasing the SQLite file handle.
///
/// Command fields: database (required)
/// </summary>
public sealed class ModelCloseHandler : ICommandHandler
{
    public string Command => "model.close";

    public Task<JsonObject> HandleAsync(JsonObject cmd, Session session)
    {
        session.Close(HandlerHelper.Require(cmd, "database"));
        return Task.FromResult(new JsonObject());
    }
}

// ── model.create ────────────────────────────────────────────────────────────

/// <summary>
/// Creates a new MIKE+ model database and opens it in the session.
///
/// Command fields: database (required), projection (optional), srid (optional)
/// </summary>
public sealed class ModelCreateHandler : ICommandHandler
{
    public string Command => "model.create";

    public Task<JsonObject> HandleAsync(JsonObject cmd, Session session)
    {
        var db         = HandlerHelper.Require(cmd, "database");
        var projection = cmd["projection"]?.GetValue<string>() ?? "";
        var srid       = cmd["srid"]?.GetValue<int>() ?? -1;

        var ctx = AmeliaContext.Create(db, projection, srid);
        session.Register(ctx);

        return Task.FromResult(new JsonObject());
    }
}

// ── model.info ──────────────────────────────────────────────────────────────

/// <summary>
/// Returns metadata about the open database: path, version, projection, SRID,
/// active model, and active simulation.
///
/// Command fields: database (required)
/// </summary>
public sealed class ModelInfoHandler : ICommandHandler
{
    public string Command => "model.info";

    public Task<JsonObject> HandleAsync(JsonObject cmd, Session session)
    {
        var ctx = session.GetOrOpen(HandlerHelper.Require(cmd, "database"));

        return Task.FromResult(new JsonObject
        {
            ["data"] = new JsonObject
            {
                ["database"]         = ctx.DbPath,
                ["version"]          = ctx.Version,
                ["projection"]       = ctx.ProjectionString,
                ["srid"]             = ctx.Srid,
                ["activeModel"]      = ctx.ActiveModel,
                ["activeSimulation"] = ctx.ActiveSimulation,
            },
        });
    }
}

// ── model.tables ────────────────────────────────────────────────────────────

/// <summary>
/// Returns the list of table names available in the open database.
///
/// Command fields: database (required)
/// </summary>
public sealed class ModelTablesHandler : ICommandHandler
{
    public string Command => "model.tables";

    public Task<JsonObject> HandleAsync(JsonObject cmd, Session session)
    {
        var ctx    = session.GetOrOpen(HandlerHelper.Require(cmd, "database"));
        var tables = ctx.GetTableNames();
        var array  = new JsonArray();
        foreach (var t in tables) array.Add(t);

        return Task.FromResult(new JsonObject { ["data"] = array });
    }
}

