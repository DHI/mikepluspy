using Microsoft.Data.Sqlite;

namespace MikePlusCli;

/// <summary>
/// Thin wrapper around a SQLite connection to a MIKE+ model database.
/// Provides helpers that mirror the Python Database class operations.
/// </summary>
public sealed class DatabaseContext : IDisposable
{
    public string DbPath { get; }
    public SqliteConnection Connection { get; }

    private DatabaseContext(string dbPath, SqliteConnection connection)
    {
        DbPath = dbPath;
        Connection = connection;
    }

    /// <summary>Open an existing MIKE+ SQLite database.</summary>
    public static DatabaseContext Open(string dbPath)
    {
        if (!File.Exists(dbPath))
            throw new FileNotFoundException($"Database file not found: {dbPath}");

        var connStr = new SqliteConnectionStringBuilder
        {
            DataSource = dbPath,
            Mode = SqliteOpenMode.ReadWriteCreate,
        }.ToString();

        var conn = new SqliteConnection(connStr);
        conn.Open();
        return new DatabaseContext(dbPath, conn);
    }

    /// <summary>
    /// Create a new MIKE+ SQLite database with the minimal required schema.
    /// </summary>
    public static DatabaseContext Create(string dbPath, string projectionString = "", int srid = -1, bool overwrite = false)
    {
        if (File.Exists(dbPath) && !overwrite)
            throw new InvalidOperationException($"Database already exists: {dbPath}. Use --overwrite to replace it.");

        if (File.Exists(dbPath) && overwrite)
            File.Delete(dbPath);

        var connStr = new SqliteConnectionStringBuilder
        {
            DataSource = dbPath,
            Mode = SqliteOpenMode.ReadWriteCreate,
        }.ToString();

        var conn = new SqliteConnection(connStr);
        conn.Open();

        // Create the minimal MIKE+ metadata tables
        using var cmd = conn.CreateCommand();
        cmd.CommandText = @"
            CREATE TABLE IF NOT EXISTS msm_Project (
                MUID TEXT PRIMARY KEY,
                ProjectionString TEXT,
                SRID INTEGER,
                UnitSystem TEXT DEFAULT 'MU_CS_SI',
                Version TEXT
            );

            CREATE TABLE IF NOT EXISTS msm_Scenario (
                ScenarioId TEXT PRIMARY KEY,
                ScenarioName TEXT NOT NULL,
                ParentScenarioId TEXT,
                IsBase INTEGER DEFAULT 0,
                Comment TEXT
            );

            CREATE TABLE IF NOT EXISTS msm_AlternativeGroup (
                GroupId TEXT PRIMARY KEY,
                GroupName TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS msm_Alternative (
                AlternativeId INTEGER PRIMARY KEY AUTOINCREMENT,
                AlternativeName TEXT NOT NULL,
                GroupId TEXT,
                ParentAlternativeId INTEGER,
                IsBase INTEGER DEFAULT 0,
                Comment TEXT,
                FOREIGN KEY (GroupId) REFERENCES msm_AlternativeGroup(GroupId)
            );

            CREATE TABLE IF NOT EXISTS msm_ScenarioAlternative (
                ScenarioId TEXT,
                AlternativeId INTEGER,
                GroupId TEXT,
                PRIMARY KEY (ScenarioId, GroupId),
                FOREIGN KEY (ScenarioId) REFERENCES msm_Scenario(ScenarioId),
                FOREIGN KEY (AlternativeId) REFERENCES msm_Alternative(AlternativeId)
            );
        ";
        cmd.ExecuteNonQuery();

        // Insert default project metadata
        using var meta = conn.CreateCommand();
        meta.CommandText = @"
            INSERT OR IGNORE INTO msm_Project (MUID, ProjectionString, SRID)
            VALUES ('project', @proj, @srid);
        ";
        meta.Parameters.AddWithValue("@proj", projectionString);
        meta.Parameters.AddWithValue("@srid", srid);
        meta.ExecuteNonQuery();

        return new DatabaseContext(dbPath, conn);
    }

    /// <summary>List all user-visible tables in the database.</summary>
    public List<string> GetTableNames()
    {
        var tables = new List<string>();
        using var cmd = Connection.CreateCommand();
        cmd.CommandText = "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name;";
        using var reader = cmd.ExecuteReader();
        while (reader.Read())
            tables.Add(reader.GetString(0));
        return tables;
    }

    /// <summary>Return column names and types for a table.</summary>
    public List<Dictionary<string, object?>> GetTableColumns(string tableName)
    {
        var columns = new List<Dictionary<string, object?>>();
        using var cmd = Connection.CreateCommand();
        // Use PRAGMA to avoid SQL injection — table_info is safe with parameterised table name via quoting
        cmd.CommandText = $"PRAGMA table_info(\"{EscapeIdentifier(tableName)}\");";
        using var reader = cmd.ExecuteReader();
        while (reader.Read())
        {
            columns.Add(new Dictionary<string, object?>
            {
                ["name"] = reader["name"],
                ["type"] = reader["type"],
                ["notnull"] = Convert.ToInt32(reader["notnull"]) == 1,
                ["default_value"] = reader["dflt_value"] is DBNull ? null : reader["dflt_value"],
                ["primary_key"] = Convert.ToInt32(reader["pk"]) == 1,
            });
        }
        return columns;
    }

    /// <summary>Run a SELECT query and return rows as list of dictionaries.</summary>
    public List<Dictionary<string, object?>> Select(string tableName, string[]? columns, string? where, string? orderBy, bool descending)
    {
        var cols = columns is { Length: > 0 } ? string.Join(", ", columns.Select(QuoteIdentifier)) : "*";
        var sql = $"SELECT {cols} FROM {QuoteIdentifier(tableName)}";
        if (!string.IsNullOrWhiteSpace(where))
            sql += $" WHERE {where}";
        if (!string.IsNullOrWhiteSpace(orderBy))
            sql += $" ORDER BY {QuoteIdentifier(orderBy)}" + (descending ? " DESC" : " ASC");

        var rows = new List<Dictionary<string, object?>>();
        using var cmd = Connection.CreateCommand();
        cmd.CommandText = sql;
        using var reader = cmd.ExecuteReader();
        while (reader.Read())
        {
            var row = new Dictionary<string, object?>();
            for (int i = 0; i < reader.FieldCount; i++)
                row[reader.GetName(i)] = reader.IsDBNull(i) ? null : reader.GetValue(i);
            rows.Add(row);
        }
        return rows;
    }

    /// <summary>Insert a row and return its MUID (or rowid).</summary>
    public string Insert(string tableName, Dictionary<string, string> values)
    {
        var colNames = string.Join(", ", values.Keys.Select(QuoteIdentifier));
        var paramNames = string.Join(", ", values.Keys.Select((_, i) => $"@p{i}"));

        using var cmd = Connection.CreateCommand();
        cmd.CommandText = $"INSERT INTO {QuoteIdentifier(tableName)} ({colNames}) VALUES ({paramNames});";

        int i = 0;
        foreach (var kv in values)
            cmd.Parameters.AddWithValue($"@p{i++}", ParseValue(kv.Value));

        cmd.ExecuteNonQuery();

        // Return the MUID if present, otherwise the rowid
        if (values.TryGetValue("MUID", out var muid))
            return muid;

        using var idCmd = Connection.CreateCommand();
        idCmd.CommandText = "SELECT last_insert_rowid();";
        return idCmd.ExecuteScalar()?.ToString() ?? "";
    }

    /// <summary>Update rows matching a condition. Returns count of affected rows.</summary>
    public int Update(string tableName, Dictionary<string, string> values, string? where, bool all)
    {
        if (string.IsNullOrWhiteSpace(where) && !all)
            throw new InvalidOperationException("UPDATE requires --where or --all flag for safety.");

        int idx = 0;
        var setClauses = values.Select(kv => $"{QuoteIdentifier(kv.Key)} = @p{idx++}");
        var sql = $"UPDATE {QuoteIdentifier(tableName)} SET {string.Join(", ", setClauses)}";
        if (!string.IsNullOrWhiteSpace(where))
            sql += $" WHERE {where}";

        using var cmd = Connection.CreateCommand();
        cmd.CommandText = sql;
        idx = 0;
        foreach (var kv in values)
            cmd.Parameters.AddWithValue($"@p{idx++}", ParseValue(kv.Value));

        return cmd.ExecuteNonQuery();
    }

    /// <summary>Delete rows matching a condition. Returns count of affected rows.</summary>
    public int Delete(string tableName, string? where, bool all)
    {
        if (string.IsNullOrWhiteSpace(where) && !all)
            throw new InvalidOperationException("DELETE requires --where or --all flag for safety.");

        var sql = $"DELETE FROM {QuoteIdentifier(tableName)}";
        if (!string.IsNullOrWhiteSpace(where))
            sql += $" WHERE {where}";

        using var cmd = Connection.CreateCommand();
        cmd.CommandText = sql;
        return cmd.ExecuteNonQuery();
    }

    /// <summary>Retrieve project-level metadata from msm_Project.</summary>
    public Dictionary<string, object?> GetProjectInfo()
    {
        var info = new Dictionary<string, object?> { ["db_path"] = DbPath };

        try
        {
            using var cmd = Connection.CreateCommand();
            cmd.CommandText = "SELECT * FROM msm_Project LIMIT 1;";
            using var reader = cmd.ExecuteReader();
            if (reader.Read())
            {
                for (int i = 0; i < reader.FieldCount; i++)
                    info[reader.GetName(i)] = reader.IsDBNull(i) ? null : reader.GetValue(i);
            }
        }
        catch (SqliteException)
        {
            // msm_Project may not exist in all databases
        }

        info["tables"] = GetTableNames();
        return info;
    }

    // ── Scenario helpers ──────────────────────────────────────────────

    public List<Dictionary<string, object?>> ListScenarios()
        => Select("msm_Scenario", null, null, "ScenarioName", descending: false);

    public string CreateScenario(string name, string? parentId, string? comment)
    {
        var id = Guid.NewGuid().ToString();
        var vals = new Dictionary<string, string>
        {
            ["ScenarioId"] = id,
            ["ScenarioName"] = name,
        };
        if (parentId != null) vals["ParentScenarioId"] = parentId;
        if (comment != null) vals["Comment"] = comment;
        Insert("msm_Scenario", vals);
        return id;
    }

    public int DeleteScenario(string scenarioId)
    {
        using var cmd = Connection.CreateCommand();
        cmd.CommandText = "DELETE FROM msm_Scenario WHERE ScenarioId = @id;";
        cmd.Parameters.AddWithValue("@id", scenarioId);
        return cmd.ExecuteNonQuery();
    }

    public bool ScenarioExists(string scenarioId)
    {
        using var cmd = Connection.CreateCommand();
        cmd.CommandText = "SELECT COUNT(*) FROM msm_Scenario WHERE ScenarioId = @id;";
        cmd.Parameters.AddWithValue("@id", scenarioId);
        return Convert.ToInt32(cmd.ExecuteScalar()) > 0;
    }

    // ── Alternative helpers ───────────────────────────────────────────

    public List<Dictionary<string, object?>> ListAlternativeGroups()
        => Select("msm_AlternativeGroup", null, null, "GroupName", descending: false);

    public List<Dictionary<string, object?>> ListAlternatives(string? groupId)
    {
        if (groupId == null)
            return Select("msm_Alternative", null, null, "AlternativeName", descending: false);

        var rows = new List<Dictionary<string, object?>>();
        using var cmd = Connection.CreateCommand();
        cmd.CommandText = "SELECT * FROM \"msm_Alternative\" WHERE GroupId = @gid ORDER BY \"AlternativeName\" ASC;";
        cmd.Parameters.AddWithValue("@gid", groupId);
        using var reader = cmd.ExecuteReader();
        while (reader.Read())
        {
            var row = new Dictionary<string, object?>();
            for (int i = 0; i < reader.FieldCount; i++)
                row[reader.GetName(i)] = reader.IsDBNull(i) ? null : reader.GetValue(i);
            rows.Add(row);
        }
        return rows;
    }

    public int CreateAlternative(string name, string groupId, int? parentId, string? comment)
    {
        var vals = new Dictionary<string, string>
        {
            ["AlternativeName"] = name,
            ["GroupId"] = groupId,
        };
        if (parentId.HasValue) vals["ParentAlternativeId"] = parentId.Value.ToString();
        if (comment != null) vals["Comment"] = comment;

        Insert("msm_Alternative", vals);

        using var cmd = Connection.CreateCommand();
        cmd.CommandText = "SELECT last_insert_rowid();";
        return Convert.ToInt32(cmd.ExecuteScalar());
    }

    public int SetScenarioAlternative(string scenarioId, int alternativeId, string groupId)
    {
        using var cmd = Connection.CreateCommand();
        cmd.CommandText = @"
            INSERT OR REPLACE INTO msm_ScenarioAlternative (ScenarioId, AlternativeId, GroupId)
            VALUES (@sid, @aid, @gid);
        ";
        cmd.Parameters.AddWithValue("@sid", scenarioId);
        cmd.Parameters.AddWithValue("@aid", alternativeId);
        cmd.Parameters.AddWithValue("@gid", groupId);
        return cmd.ExecuteNonQuery();
    }

    // ── SQL safety helpers ────────────────────────────────────────────

    private static string QuoteIdentifier(string id) => $"\"{EscapeIdentifier(id)}\"";
    private static string EscapeIdentifier(string id) => id.Replace("\"", "\"\"");
    private static string EscapeValue(string v) => v.Replace("'", "''");

    private static object ParseValue(string raw)
    {
        if (string.Equals(raw, "NULL", StringComparison.OrdinalIgnoreCase))
            return DBNull.Value;
        if (long.TryParse(raw, out var l))
            return l;
        if (double.TryParse(raw, System.Globalization.NumberStyles.Float, System.Globalization.CultureInfo.InvariantCulture, out var d))
            return d;
        return raw;
    }

    public void Dispose() => Connection.Dispose();
}
