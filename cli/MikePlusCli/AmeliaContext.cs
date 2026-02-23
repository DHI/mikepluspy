using System.Reflection;
using DHI.Amelia.DataModule.Services.DataSource;
using DHI.Amelia.DataModule.Services.DataTables;
using DHI.Amelia.DataModule.Services.ImportExportPfsFile;
using DHI.Amelia.GlobalUtility.DataType;
using DHI.Mike.Install;

namespace MikePlusCli;

/// <summary>
/// Central wrapper around the DHI Amelia .NET assemblies.
///
/// Manages the full lifecycle of a MIKE+ model database through Amelia's
/// <see cref="BaseDataSource"/> and <see cref="DataTableContainer"/>,
/// ensuring the CLI operates through the same engine the MIKE+ GUI uses.
/// </summary>
public sealed class AmeliaContext : IDisposable
{
    private readonly BaseDataSource _dataSource;
    private readonly DataTableContainer _dataTables;
    private bool _isOpen;

    /// <summary>Absolute path to the .sqlite database file.</summary>
    public string DbPath { get; }

    /// <summary>The Amelia data-table container (used by tools and simulation).</summary>
    public DataTableContainer DataTables => _dataTables;

    /// <summary>The Amelia scenario manager.</summary>
    public IScenarioManager ScenarioManager =>
        _dataSource.ScenarioManager
        ?? throw new InvalidOperationException("Scenario manager is not available. Is the database open?");

    // ── Static bootstrap ──────────────────────────────────────────────

    /// <summary>
    /// One-time setup: register the MIKE+ assembly resolver so that all
    /// DHI.Amelia assemblies can be located at runtime.
    /// </summary>
    public static void Bootstrap()
    {
        var installRoot = Environment.GetEnvironmentVariable("MIKE_PLUS_INSTALL")
            ?? @"C:\Program Files (x86)\DHI\MIKE+\2026";

        var binDir = Path.Combine(installRoot, "bin");

        // Resolve assemblies from the MIKE+ install directory
        AppDomain.CurrentDomain.AssemblyResolve += (_, args) =>
        {
            var name = args.Name.Split(',')[0] + ".dll";
            var path = Path.Combine(binDir, name);
            return File.Exists(path) ? Assembly.LoadFrom(path) : null;
        };

        // Initialize the DHI MIKE product environment
        MikeImport.Setup(2026, MikeProducts.MikePlus);
    }

    // ── Construction ──────────────────────────────────────────────────

    private AmeliaContext(string dbPath, BaseDataSource dataSource, DataTableContainer dataTables)
    {
        DbPath = dbPath;
        _dataSource = dataSource;
        _dataTables = dataTables;
        _isOpen = false;
    }

    /// <summary>
    /// Create a new MIKE+ model database at <paramref name="dbPath"/>.
    /// </summary>
    public static AmeliaContext Create(string dbPath, string projectionString = "", int srid = -1)
    {
        var fullPath = Path.GetFullPath(dbPath);
        var ds = BaseDataSource.Create(fullPath);
        ds.CreateDatabase();
        ds.OpenDatabase();
        ds.CreateModelTables(srid, projectionString);
        ds.CloseDatabase();

        var dtc = new DataTableContainer(true) { DataSource = ds };
        return new AmeliaContext(fullPath, ds, dtc);
    }

    /// <summary>
    /// Open an existing MIKE+ model database at <paramref name="dbPath"/>.
    /// </summary>
    public static AmeliaContext Open(string dbPath)
    {
        var fullPath = Path.GetFullPath(dbPath);
        if (!File.Exists(fullPath))
            throw new FileNotFoundException($"Database not found: {fullPath}");

        var ds = BaseDataSource.Create(fullPath);
        var dtc = new DataTableContainer(true) { DataSource = ds };

        var ctx = new AmeliaContext(fullPath, ds, dtc);
        ctx.OpenInternal();
        return ctx;
    }

    private void OpenInternal()
    {
        _dataSource.OpenDatabase();
        _dataTables.SetActiveModel(_dataSource.ActiveModel);
        _dataTables.SetEumAppUnitSystem(_dataSource.UnitSystemOption);
        _dataTables.OnResetContainer(null, null);
        _dataTables.UndoRedoManager = new AmlUndoRedoManager();
        _dataTables.ImportExportPfsFile = new ImportExportPfsFile();
        _isOpen = true;
    }

    /// <summary>Close the database and release Amelia resources.</summary>
    public void Close()
    {
        if (!_isOpen) return;
        _dataTables.UndoRedoManager?.ClearUndoRedoBuffer();
        _dataSource.CloseDatabase();
        _isOpen = false;
    }

    // ── Model metadata ────────────────────────────────────────────────

    /// <summary>Projection string (WKT) of the model.</summary>
    public string ProjectionString => _dataSource.ProjectionString ?? "";

    /// <summary>Spatial Reference ID.</summary>
    public int Srid => _dataSource.Srid;

    /// <summary>Active model identifier (CS, WD, etc.).</summary>
    public MUModelOption ActiveModel => _dataSource.ActiveModel;

    /// <summary>Currently selected simulation MUID.</summary>
    public string ActiveSimulation => _dataSource.ActiveSimulation ?? "";

    /// <summary>Database version (major.minor).</summary>
    public string Version => $"{_dataSource.DbMajorVersion}.{_dataSource.DbMinorVersion}";

    // ── Table access ──────────────────────────────────────────────────

    /// <summary>Get a model table by name (e.g. "msm_Node", "mw_Pipe").</summary>
    public IMuTable GetTable(string tableName)
    {
        var table = _dataTables.GetTable(tableName);
        return table ?? throw new ArgumentException($"Table '{tableName}' not found.");
    }

    /// <summary>List all table names registered in the container.</summary>
    public List<string> GetTableNames()
    {
        var names = new List<string>();
        foreach (var table in _dataTables.Tables)
            names.Add(table.TableName);
        names.Sort();
        return names;
    }

    // ── Query helpers (delegate to IMuTable) ──────────────────────────

    /// <summary>
    /// Select rows from a table via Amelia's query engine.
    /// Returns rows keyed by MUID, each containing a column→value dictionary.
    /// </summary>
    public IDictionary<string, IDictionary<string, object?>>? SelectRows(
        string tableName, string[]? columns, string? where, string? orderBy, bool descending)
    {
        var table = GetTable(tableName);
        var colList = columns is { Length: > 0 }
            ? new List<string>(columns)
            : null;

        return table.GetMuidAndFieldsWhereOrder(colList, where, orderBy, !descending);
    }

    /// <summary>Insert a row. Returns the MUID of the new row.</summary>
    public string InsertRow(string tableName, Dictionary<string, object> values)
    {
        var table = GetTable(tableName);

        // Generate or use provided MUID
        string muid;
        if (values.TryGetValue("MUID", out var muidObj) && muidObj is string provided && !string.IsNullOrEmpty(provided))
            muid = provided;
        else
            muid = table.CreateUniqueMuid();

        // Separate geometry from regular values
        values.Remove("MUID");
        table.InsertByCommand(muid, null, values);
        return muid;
    }

    /// <summary>Update matching rows. Returns MUIDs of updated rows.</summary>
    public List<string> UpdateRows(string tableName, Dictionary<string, object> values, string? where, bool all)
    {
        if (string.IsNullOrWhiteSpace(where) && !all)
            throw new InvalidOperationException("Update requires a --where condition or the --all flag.");

        var table = GetTable(tableName);
        var muids = string.IsNullOrWhiteSpace(where)
            ? table.GetMuids(null, false)
            : table.GetMuidsWhere(where);

        var updated = new List<string>();
        foreach (var muid in muids)
        {
            table.SetValuesByCommand(muid, values);
            updated.Add(muid);
        }
        return updated;
    }

    /// <summary>Delete matching rows. Returns MUIDs of deleted rows.</summary>
    public List<string> DeleteRows(string tableName, string? where, bool all)
    {
        if (string.IsNullOrWhiteSpace(where) && !all)
            throw new InvalidOperationException("Delete requires a --where condition or the --all flag.");

        var table = GetTable(tableName);
        var muids = string.IsNullOrWhiteSpace(where)
            ? table.GetMuids(null, false)
            : table.GetMuidsWhere(where);

        var muidList = new List<string>(muids);
        table.MultiDeleteByCommand(muidList);
        return muidList;
    }

    // ── IDisposable ───────────────────────────────────────────────────

    public void Dispose() => Close();
}
