using System.Text.Json.Nodes;

namespace MikePlusJsonCli.Handlers;

/// <summary>
/// Contract for a command handler in the JSON streaming protocol.
///
/// Each handler is responsible for exactly one command name (e.g. "edit.insert").
/// It receives the full, parsed command object so it can extract whatever fields
/// it needs, and returns a <see cref="JsonObject"/> that becomes the body of the
/// response (the dispatcher adds "id", "status", and "command" before writing).
///
/// Handlers should throw a descriptive <see cref="Exception"/> on failure; the
/// main loop in Program.cs catches it and emits a {"status":"error"} response.
/// </summary>
public interface ICommandHandler
{
    /// <summary>
    /// The command name this handler responds to, e.g. <c>"edit.insert"</c>.
    /// Names follow the convention <c>"&lt;domain&gt;.&lt;verb&gt;"</c>.
    /// </summary>
    string Command { get; }

    /// <summary>
    /// Executes the command and returns the result payload.
    /// </summary>
    /// <param name="cmd">The full command JSON object from stdin.</param>
    /// <param name="session">The current session (open Amelia contexts, etc.).</param>
    /// <returns>A JSON object whose fields are merged into the response envelope.</returns>
    Task<JsonObject> HandleAsync(JsonObject cmd, Session session);
}
