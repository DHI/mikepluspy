namespace MikePlusJsonCli;

/// <summary>
/// Holds state that persists across commands in a single streaming session.
///
/// The most important piece of state is the dictionary of open
/// <see cref="AmeliaContext"/> objects, keyed by the resolved absolute database
/// path.  This lets a sequence of commands share one database lifecycle
/// (open → many operations → close) without paying the Amelia startup cost per
/// command.
///
/// A command that includes a "database" field and finds no matching open context
/// triggers a lazy-open so that callers can omit an explicit model.open.
/// </summary>
public sealed class Session : IDisposable
{
    private readonly Dictionary<string, AmeliaContext> _contexts = new(StringComparer.OrdinalIgnoreCase);

    // ── Context management ─────────────────────────────────────────────

    /// <summary>
    /// Returns the <see cref="AmeliaContext"/> for the given database path,
    /// opening it lazily if it is not yet open.
    /// </summary>
    public AmeliaContext GetOrOpen(string dbPath)
    {
        var key = Path.GetFullPath(dbPath);
        if (!_contexts.TryGetValue(key, out var ctx))
        {
            ctx = AmeliaContext.Open(key);
            _contexts[key] = ctx;
        }
        return ctx;
    }

    /// <summary>
    /// Registers an already-constructed context (used by model.create and
    /// model.open when the caller wants explicit lifecycle control).
    /// </summary>
    public void Register(AmeliaContext ctx) =>
        _contexts[ctx.DbPath] = ctx;

    /// <summary>
    /// Closes and removes the context for the given database path.
    /// </summary>
    public void Close(string dbPath)
    {
        var key = Path.GetFullPath(dbPath);
        if (_contexts.TryGetValue(key, out var ctx))
        {
            ctx.Close();
            ctx.Dispose();
            _contexts.Remove(key);
        }
    }

    /// <summary>
    /// Returns true if a context for the given path is already open.
    /// </summary>
    public bool IsOpen(string dbPath) =>
        _contexts.ContainsKey(Path.GetFullPath(dbPath));

    // ── IDisposable ────────────────────────────────────────────────────

    public void Dispose()
    {
        foreach (var ctx in _contexts.Values)
        {
            try { ctx.Close(); }
            catch (Exception ex)
            {
                Console.Error.WriteLine($"Warning: error closing '{ctx.DbPath}': {ex.Message}");
            }
            ctx.Dispose();
        }
        _contexts.Clear();
    }
}
