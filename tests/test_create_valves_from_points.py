from __future__ import annotations

import shutil
import struct
from pathlib import Path

import pytest
from shapely import wkt
from shapely.geometry import Point

import mikeplus as mp
from mikeplus.tools import CreateValvesFromPointsTool

pytestmark = pytest.mark.license_required


def write_point_shapefile(
    path: Path, points: list[tuple[float, float]], columns: dict[str, list[str]]
) -> Path:
    """Write a minimal point shapefile with text columns, so the tests need no GIS library."""
    n = len(points)
    xs, ys = zip(*points)

    def header(file_length_words: int) -> bytes:
        return struct.pack(">7i", 9994, 0, 0, 0, 0, 0, file_length_words) + struct.pack(
            "<2i8d", 1000, 1, min(xs), min(ys), max(xs), max(ys), 0, 0, 0, 0
        )

    # A point record is a 4-word header plus 10 words of content.
    path.with_suffix(".shp").write_bytes(
        header(50 + 14 * n)
        + b"".join(
            struct.pack(">2i", i + 1, 10) + struct.pack("<i2d", 1, x, y)
            for i, (x, y) in enumerate(points)
        )
    )
    path.with_suffix(".shx").write_bytes(
        header(50 + 4 * n)
        + b"".join(struct.pack(">2i", 50 + 14 * i, 10) for i in range(n))
    )

    width = 32
    names = list(columns)
    dbf = struct.pack(
        "<4BIHH20x", 3, 126, 1, 1, n, 33 + 32 * len(names), 1 + width * len(names)
    )
    dbf += b"".join(
        struct.pack("<11sc4xBB14x", name.encode(), b"C", width, 0) for name in names
    )
    dbf += b"\r"
    for i in range(n):
        dbf += b" " + b"".join(columns[name][i].encode().ljust(width) for name in names)
    path.with_suffix(".dbf").write_bytes(dbf + b"\x1a")
    return path.with_suffix(".shp")


def geometry(table, muid):
    return wkt.loads(table._net_table.GetGeometry(muid).AsText())


EPANET_DEMO_DIR = Path(__file__).parent / "testdata" / "Db" / "Epanet_Demo"
PIPE_3_POINT = (-2486.67, 1640.0)
JUNCTION_4_POINT = (-1702.0, 815.0)
FAR_POINT = (0.0, 10000.0)


@pytest.fixture
def points_file(tmp_path):
    return write_point_shapefile(
        tmp_path / "valves.shp", [PIPE_3_POINT, FAR_POINT], {"ID": ["V1", "V2"]}
    )


@pytest.fixture(scope="module")
def created(tmp_path_factory):
    """Run the tool once on a private copy; the tests below only read the result."""
    tmp_path = tmp_path_factory.mktemp("create_valves")
    shutil.copytree(EPANET_DEMO_DIR, tmp_path / "db")
    points_file = write_point_shapefile(
        tmp_path / "valves.shp",
        [PIPE_3_POINT, JUNCTION_4_POINT, FAR_POINT],
        {
            "ID": ["V_pipe", "V_junction", "V_far"],
            "VTYPE": ["FCV", "3", "PRV"],
            "STATUS": ["1", "0", "2"],
            "DIAM": ["0.3", "not a number", "0.2"],
            "SETTING": ["12.5", "4", "1"],
            "DESCR": ["on a pipe", "at a junction", "too far"],
        },
    )
    with mp.open(tmp_path / "db" / "Epanet_Demo.sqlite") as db:
        pipe_3 = geometry(db.tables.mw_Pipe, "Pipe_3")
        messages = CreateValvesFromPointsTool(db).run(
            points_file,
            search_radius=50.0,
            valve_length=2.0,
            muid_field="ID",
            type_field="VTYPE",
            status_field="STATUS",
            diameter_field="DIAM",
            setting_field="SETTING",
            description_field="DESCR",
        )
        yield db, messages, pipe_3


def test_reports_created_and_skipped_points(created):
    _, messages, _ = created

    assert len(messages) == 3
    assert "2" in messages[0] and "3" in messages[0]
    assert any("V_junction" in m for m in messages[1:])
    assert any("10000" in m for m in messages[1:])


def test_maps_attributes_from_columns(created):
    db, _, _ = created
    fields = ["TypeNo", "StatusNo", "Diameter", "Setting", "Description"]
    valves = db.tables.mw_Valve.select(fields).execute()

    assert sorted(valves) == ["V_junction", "V_pipe"]
    assert valves["V_pipe"] == [4, 1, 0.3, 12.5, "on a pipe"]
    # The unreadable diameter keeps the MIKE+ default.
    assert valves["V_junction"][:2] == [3, 0]
    assert valves["V_junction"][3:] == [4.0, "at a junction"]


def test_valve_on_pipe_splits_it_around_the_point(created):
    db, _, pipe_3 = created
    from_node, to_node = (
        db.tables.mw_Valve.select(["FromNodeID", "ToNodeID"]).by_muid("V_pipe")
    ).execute()["V_pipe"]
    valve = geometry(db.tables.mw_Valve, "V_pipe")
    pipes = db.tables.mw_Pipe.select(["FromNodeID", "ToNodeID"]).execute()

    assert "Pipe_3" not in pipes
    assert ["Junction_2", from_node] in pipes.values()
    assert [to_node, "Junction_3"] in pipes.values()
    assert valve.length == pytest.approx(2.0, rel=1e-3)
    centre = valve.interpolate(0.5, normalized=True)
    snapped = pipe_3.interpolate(pipe_3.project(Point(PIPE_3_POINT)))
    assert centre.distance(snapped) == pytest.approx(0.0, abs=1e-3)


def test_valve_at_junction_shortens_a_pipe(created):
    db, _, _ = created
    nodes = db.tables.mw_Valve.select(["FromNodeID", "ToNodeID"]).execute()
    valve = geometry(db.tables.mw_Valve, "V_junction")
    junction_4 = geometry(db.tables.mw_Junction, "Junction_4")
    pipes = db.tables.mw_Pipe.select(["FromNodeID", "ToNodeID"]).execute()

    assert "Junction_4" in nodes["V_junction"]
    (new_junction,) = set(nodes["V_junction"]) - {"Junction_4"}
    assert any(new_junction in ends for ends in pipes.values())
    assert valve.length == pytest.approx(2.0, rel=1e-3)
    assert junction_4.distance(valve.boundary) == pytest.approx(0.0, abs=1e-6)


def test_without_field_mapping_generates_ids(epanet_demo_db, tmp_path):
    points_file = write_point_shapefile(
        tmp_path / "points.shp", [PIPE_3_POINT, FAR_POINT], {"ID": ["V1", "V2"]}
    )
    with mp.open(epanet_demo_db) as db:
        messages = CreateValvesFromPointsTool(db).run(str(points_file), 50.0, 2.0)
        muids = db.tables.mw_Valve.get_muids()

    assert len(messages) == 2
    assert len(muids) == 1
    assert muids[0] not in ("V1", "V2")


@pytest.mark.parametrize(
    ("search_radius", "valve_length"), [(0.0, 2.0), (50.0, 0.0), (-1.0, 2.0)]
)
def test_rejects_non_positive_distances(
    session_epanet_demo_db, points_file, search_radius, valve_length
):
    with mp.open(session_epanet_demo_db) as db:
        tool = CreateValvesFromPointsTool(db)
        with pytest.raises(ValueError, match="must be positive"):
            tool.run(points_file, search_radius, valve_length)


def test_rejects_missing_file(session_epanet_demo_db, tmp_path):
    with mp.open(session_epanet_demo_db) as db:
        tool = CreateValvesFromPointsTool(db)
        with pytest.raises(FileNotFoundError):
            tool.run(tmp_path / "missing.shp", 50.0, 2.0)


def test_rejects_collection_system_model(session_sirius_db, points_file):
    with mp.open(session_sirius_db) as db:
        tool = CreateValvesFromPointsTool(db)
        with pytest.raises(ValueError, match="water distribution"):
            tool.run(points_file, 50.0, 2.0)
