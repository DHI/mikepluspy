using System.Text.Json;
using System.Text.Json.Nodes;

namespace MikePlusJsonCli.Handlers;

// ── edit.select ──────────────────────────────────────────────────────────────

/// <summary>
/// Queries rows from a table via Amelia's IMuTable.GetMuidAndFieldsWhereOrder.
///
/// Command fields:
///   database (required), table (required),
///   columns  (optional JSON array, defaults to all),
///   where    (optional SQL filter),
///   orderBy  (optional column name)
/// </summary>
public sealed class EditSelectHandler : ICommandHandler
{
    public string Command => "edit.select";

    public Task<JsonObject> HandleAsync(JsonObject cmd, Session session)
    {
        var ctx   = session.GetOrOpen(HandlerHelper.Require(cmd, "database"));
        var table = HandlerHelper.Require(cmd, "table");

        var columns = cmd["columns"] is JsonArray cols
            ? string.Join(",", cols.Select(c => c!.GetValue<string>()))
            : "*";
        var where   = cmd["where"]?.GetValue<string>() ?? "";
        var orderBy = cmd["orderBy"]?.GetValue<string>() ?? "";

        var rows = ctx.Select(table, columns, where, orderBy);

        // Serialize the result set as a JSON array of row objects.
        var data  = new JsonArray();
        foreach (var row in rows)
        {
            var obj = new JsonObject();
            foreach (var (k, v) in row)
                obj[k] = v is null ? null : JsonValue.Create(v);
            data.Add(obj);
        }

        return Task.FromResult(new JsonObject { ["data"] = data });
    }
}

// ── edit.insert ──────────────────────────────────────────────────────────────

/// <summary>
/// Inserts a single row via Amelia's IMuTable.InsertByCommand.
///
/// Because the process is long-lived, many edit.insert commands can be sent in
/// sequence and all share the same open AmeliaContext — there is no per-row
/// database open/close cost.  This is the natural bulk-insert pattern in the
/// streaming protocol (compare with PR #113's --input flag).
///
/// Command fields:
///   database (required), table (required), row (required JSON object of field→value)
/// </summary>
public sealed class EditInsertHandler : ICommandHandler
{
    public string Command => "edit.insert";

    public Task<JsonObject> HandleAsync(JsonObject cmd, Session session)
    {
        var ctx   = session.GetOrOpen(HandlerHelper.Require(cmd, "database"));
        var table = HandlerHelper.Require(cmd, "table");
        var row   = cmd["row"] as JsonObject
            ?? throw new InvalidOperationException("Missing required field 'row'.");

        var fields = row.ToDictionary(
            kv => kv.Key,
            kv => ExtractValue(kv.Value));

        ctx.Insert(table, fields);
        return Task.FromResult(new JsonObject());
    }
}

// ── edit.update ──────────────────────────────────────────────────────────────

/// <summary>
/// Updates rows matching a WHERE clause via Amelia's IMuTable.SetValuesByCommand.
/// Requires either "where" or "all":true to prevent accidental full-table updates.
///
/// Command fields:
///   database (required), table (required),
///   set      (required JSON object of field→value),
///   where    (required unless all:true)
///   all      (optional bool, must be true to update all rows)
/// </summary>
public sealed class EditUpdateHandler : ICommandHandler
{
    public string Command => "edit.update";

    public Task<JsonObject> HandleAsync(JsonObject cmd, Session session)
    {
        var ctx   = session.GetOrOpen(HandlerHelper.Require(cmd, "database"));
        var table = HandlerHelper.Require(cmd, "table");
        var set   = cmd["set"] as JsonObject
            ?? throw new InvalidOperationException("Missing required field 'set'.");

        var where = cmd["where"]?.GetValue<string>();
        var all   = cmd["all"]?.GetValue<bool>() ?? false;

        if (string.IsNullOrEmpty(where) && !all)
            throw new InvalidOperationException(
                "Provide 'where' or set 'all':true to update rows.");

        var fields = set.ToDictionary(
            kv => kv.Key,
            kv => ExtractValue(kv.Value));

        ctx.Update(table, fields, where ?? "");
        return Task.FromResult(new JsonObject());
    }
}

// ── edit.delete ──────────────────────────────────────────────────────────────

/// <summary>
/// Deletes rows matching a WHERE clause via Amelia's IMuTable.MultiDeleteByCommand.
/// Requires either "where" or "all":true to prevent accidental full-table deletes.
///
/// Command fields:
///   database (required), table (required),
///   where    (required unless all:true),
///   all      (optional bool, must be true to delete all rows)
/// </summary>
public sealed class EditDeleteHandler : ICommandHandler
{
    public string Command => "edit.delete";

    public Task<JsonObject> HandleAsync(JsonObject cmd, Session session)
    {
        var ctx   = session.GetOrOpen(HandlerHelper.Require(cmd, "database"));
        var table = HandlerHelper.Require(cmd, "table");

        var where = cmd["where"]?.GetValue<string>();
        var all   = cmd["all"]?.GetValue<bool>() ?? false;

        if (string.IsNullOrEmpty(where) && !all)
            throw new InvalidOperationException(
                "Provide 'where' or set 'all':true to delete rows.");

        ctx.Delete(table, where ?? "");
        return Task.FromResult(new JsonObject());
    }
}

// ── value extraction helper ──────────────────────────────────────────────────

file static class EditValueHelper
{
    /// <summary>
    /// Extracts a CLR value from a <see cref="JsonNode"/>, preserving the
    /// original JSON type (long, double, bool, string) rather than forcing
    /// everything to string.  This ensures numeric and boolean field values
    /// reach Amelia's IMuTable API with their correct types.
    /// </summary>
    internal static object? ExtractValue(JsonNode? node) => node switch
    {
        null                                                 => null,
        JsonValue v when v.TryGetValue<long>(out var i)    => i,
        JsonValue v when v.TryGetValue<double>(out var d)  => d,
        JsonValue v when v.TryGetValue<bool>(out var b)    => b,
        JsonValue v when v.TryGetValue<string>(out var s)  => s,
        _                                                    => node.ToString(),
    };
}

