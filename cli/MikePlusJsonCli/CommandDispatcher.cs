using System.Text.Json.Nodes;
using MikePlusJsonCli.Handlers;

namespace MikePlusJsonCli;

/// <summary>
/// Routes incoming command objects to the correct <see cref="ICommandHandler"/>.
///
/// Handlers are registered by their <see cref="ICommandHandler.Command"/> name
/// (e.g. "edit.insert").  The dispatcher is intentionally simple: a dictionary
/// lookup followed by a handler invocation.  Adding a new command requires only
/// (a) an <see cref="ICommandHandler"/> implementation and (b) a single
/// <see cref="Register"/> call in Program.cs — no argument-parsing infrastructure
/// needs to change.
/// </summary>
public sealed class CommandDispatcher
{
    private readonly Dictionary<string, ICommandHandler> _handlers =
        new(StringComparer.OrdinalIgnoreCase);

    /// <summary>Registers a handler and returns <c>this</c> for fluent chaining.</summary>
    public CommandDispatcher Register(ICommandHandler handler)
    {
        _handlers[handler.Command] = handler;
        return this;
    }

    /// <summary>
    /// Dispatches <paramref name="cmd"/> to the matching handler.
    /// </summary>
    /// <exception cref="InvalidOperationException">
    /// Thrown when no handler is registered for the requested command name.
    /// </exception>
    public Task<JsonObject> DispatchAsync(JsonObject cmd, Session session)
    {
        var commandName = cmd["command"]?.GetValue<string>()
            ?? throw new InvalidOperationException("Missing required field 'command'.");

        if (!_handlers.TryGetValue(commandName, out var handler))
            throw new InvalidOperationException($"Unknown command '{commandName}'.");

        return handler.HandleAsync(cmd, session);
    }
}
