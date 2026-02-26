using System.Text.Json.Nodes;

namespace MikePlusJsonCli.Handlers;

/// <summary>
/// Shared helpers for command handlers.
/// </summary>
internal static class HandlerHelper
{
    /// <summary>
    /// Reads a required string field from a command JSON object, throwing a
    /// descriptive exception if the field is absent or null.
    /// </summary>
    internal static string Require(JsonObject cmd, string field) =>
        cmd[field]?.GetValue<string>()
        ?? throw new InvalidOperationException($"Missing required field '{field}'.");
}
