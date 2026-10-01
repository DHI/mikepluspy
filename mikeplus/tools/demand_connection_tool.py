"""The connection tool from MIKE+, for demand allocations."""

from __future__ import annotations

import math
from collections.abc import Iterable
from typing import TYPE_CHECKING, Any, Literal

from DHI.Amelia.GlobalUtility.DataType import CommandStatus
from DHI.Amelia.Tools.GeoCodeTool import GeoCodeEngine
from System.Threading import CancellationTokenSource

from ..database import DatabaseError
from ..dotnet import as_dotnet_list

if TYPE_CHECKING:
    from ..database import Database

DemandConnectionMethod = Literal[
    "nearest_junction",
    "junction_by_nearest_pipe",
    "junction_by_pipe_id",
    "nearest_pipe",
]

_CONNECTION_TYPES: dict[str, int] = {
    "nearest_junction": 0,
    "junction_by_nearest_pipe": 2,
    "junction_by_pipe_id": 3,
    "nearest_pipe": 4,
}

# The methods each optional argument applies to; `where` applies to all.
_APPLIES_TO: dict[str, tuple[str, ...]] = {
    "max_distance": ("nearest_junction", "junction_by_nearest_pipe", "nearest_pipe"),
    "max_diameter": ("junction_by_nearest_pipe", "nearest_pipe"),
    "junction_ids": ("nearest_junction",),
    "pipe_ids": ("junction_by_nearest_pipe", "nearest_pipe"),
}

# Both limits are disabled with -1.
_NO_LIMIT = -1.0

_JUNCTION_CONNECTION = 1


class DemandConnectionTool:
    """The connection tool from MIKE+ for demand allocations.

    Connects the points of the demand allocations table (`mw_DemAlloc`) in a
    water distribution model to junctions or pipes. Each connected demand
    allocation gets its `ConnectionTypeNo` and its `JunctionID` or `PipeID`
    set, and a line in the demand allocation connections table
    (`mw_DemAllocConn`).

    Examples
    --------
    Connect every demand allocation to the nearest junction within 50 m.

    ```python
    >>> from mikeplus import Database
    >>> from mikeplus.tools import DemandConnectionTool
    >>> db = Database("path/to/model.sqlite")
    >>> DemandConnectionTool(db).run("nearest_junction", max_distance=50.0)
    >>> db.close()
    ```

    """

    def __init__(self, database: Database) -> None:
        """Initialize the DemandConnectionTool with the given Database.

        Parameters
        ----------
        database : Database
            A Database object for a MIKE+ water distribution model.

        """
        if not database.is_open:
            database.open()
        self._database = database
        self._dataTables = database._data_table_container

    def run(
        self,
        method: DemandConnectionMethod = "nearest_junction",
        *,
        demand_ids: Iterable[str] | None = None,
        max_distance: float | None = None,
        max_diameter: float | None = None,
        junction_ids: Iterable[str] | None = None,
        pipe_ids: Iterable[str] | None = None,
        where: str | None = None,
    ) -> None:
        """Connect demand allocations to the network.

        A demand allocation connected to a junction afterwards has
        `ConnectionTypeNo` 1 and no `PipeID`; one connected to a pipe has
        `ConnectionTypeNo` 2 and no `JunctionID`. A demand allocation for
        which no target is found loses any connection it had: it gets
        `ConnectionTypeNo` 1, no `JunctionID`, no `PipeID` and no connection
        line.

        Parameters
        ----------
        method : str, optional
            How to choose the target, by default "nearest_junction":

            - "nearest_junction": the junction nearest to the demand allocation.
            - "junction_by_nearest_pipe": the end junction, nearest to the
              demand allocation, of the nearest pipe.
            - "junction_by_pipe_id": the end junction, nearest to the demand
              allocation, of the pipe whose MUID equals the demand
              allocation's MUID. Demand allocations without such a pipe, or
              whose pipe does not meet `where`, are skipped and left as they
              are.
            - "nearest_pipe": the pipe nearest to the demand allocation.
        demand_ids : Iterable[str], optional
            MUIDs of the demand allocations to connect. By default all of them;
            an empty iterable connects none.
        max_distance : float, optional
            Search distance, in the model's length unit, for
            "nearest_junction", "junction_by_nearest_pipe" and "nearest_pipe".
            By default the search is not limited.
        max_diameter : float, optional
            Only pipes with at most this diameter, in the model's diameter
            unit, are candidates for "junction_by_nearest_pipe" and
            "nearest_pipe". By default all pipes are.
        junction_ids : Iterable[str], optional
            MUIDs of the junctions that "nearest_junction" may connect to. By
            default all junctions.
        pipe_ids : Iterable[str], optional
            MUIDs of the pipes that "junction_by_nearest_pipe" and
            "nearest_pipe" may connect to. By default all pipes.
        where : str, optional
            SQL condition the targets must meet: on `mw_Junction` for
            "nearest_junction", otherwise on `mw_Pipe`. For
            "junction_by_pipe_id" it is a .NET format string: `{0}` is
            replaced by the pipe's MUID, and literal braces must be doubled.

        Raises
        ------
        TypeError
            If `demand_ids`, `junction_ids` or `pipe_ids` is a single string
            instead of an iterable of MUIDs.
        ValueError
            If `method` is not one of the values above, an argument is given
            that does not apply to `method`, a distance or diameter limit is
            not a positive finite number, `junction_ids` or `pipe_ids` is
            empty, or `demand_ids`, `junction_ids` or `pipe_ids` names a
            feature that does not exist.
        DatabaseError
            If MIKE+ fails to connect the demand allocations. If it fails
            partway through, the demand allocations it had already processed
            keep their new connections, possibly alongside a stale
            `JunctionID` or `PipeID`.

        """
        if method not in _CONNECTION_TYPES:
            raise ValueError(
                f"Unknown method {method!r}. Use one of {list(_CONNECTION_TYPES)}."
            )
        given = {
            "max_distance": max_distance,
            "max_diameter": max_diameter,
            "junction_ids": junction_ids,
            "pipe_ids": pipe_ids,
        }
        for name, value in given.items():
            if value is not None and method not in _APPLIES_TO[name]:
                raise ValueError(f"{name} does not apply to method {method!r}.")
        distance = _limit("max_distance", max_distance)
        diameter = _limit("max_diameter", max_diameter)
        demands = _muids("demand_ids", demand_ids)
        junctions = _non_empty("junction_ids", _muids("junction_ids", junction_ids))
        pipes = _non_empty("pipe_ids", _muids("pipe_ids", pipe_ids))
        if demands is not None and not demands:
            return
        tables = self._database.tables
        for name, muids, table in (
            ("demand allocations", demands, tables.mw_DemAlloc),
            ("junctions", junctions, tables.mw_Junction),
            ("pipes", pipes, tables.mw_Pipe),
        ):
            if muids is None:
                continue
            # MIKE+ raises at an unknown demand allocation, partway through the
            # run, and treats an unknown junction or pipe as no target at all.
            unknown = set(muids) - set(table.get_muids())
            if unknown:
                raise ValueError(f"Unknown {name}: {sorted(unknown)}")

        args = (
            _optional_list(demands),
            _optional_list(junctions),
            _optional_list(pipes),
            -1,  # not limited to the GUI selection
            distance,
            _CONNECTION_TYPES[method],
            diameter,
            where,
            CancellationTokenSource().Token,
        )
        try:
            result = GeoCodeEngine(self._dataTables).GeocodeDemand(*args)
        except Exception as error:
            raise DatabaseError(
                f"Failed to connect the demand allocations: {error}"
            ) from None
        if result is None:
            raise DatabaseError("Failed to connect the demand allocations.")
        if result.Status == CommandStatus.Failure:
            raise DatabaseError(
                f"Failed to connect the demand allocations: {result.Msg}"
            )
        self._clear_stale_connections(method, demands)

    def _clear_stale_connections(self, method: str, demands: list[str] | None) -> None:
        # MIKE+ writes only the field of the target it found, or JunctionID
        # when it found none, so the other field keeps an earlier connection.
        table = self._database.tables.mw_DemAlloc
        stale: list[tuple[str, str | None]] = [
            ("PipeID", f"ConnectionTypeNo = {_JUNCTION_CONNECTION}")
        ]
        if method == "nearest_pipe":
            stale.append(("JunctionID", None))
        for field, condition in stale:
            query = table.update({field: None}).where(
                f"{field} IS NOT NULL AND {field} <> ''"
            )
            if condition is not None:
                query.where(condition)
            if demands is not None:
                query.by_muid(demands)
            query.execute()


def _limit(name: str, value: float | None) -> float:
    if value is None:
        return _NO_LIMIT
    value = float(value)
    if not (math.isfinite(value) and value > 0):
        raise ValueError(f"{name} must be a positive finite number, got {value}.")
    return value


def _muids(name: str, items: Iterable[str] | None) -> list[str] | None:
    if items is None:
        return None
    if isinstance(items, str):
        raise TypeError(f"{name} must be an iterable of MUIDs, not a string.")
    return list(items)


def _non_empty(name: str, items: list[str] | None) -> list[str] | None:
    # MIKE+ treats an empty list like None, as no restriction at all.
    if items is not None and not items:
        raise ValueError(f"{name} is empty. Pass None to allow all.")
    return items


def _optional_list(items: list[str] | None) -> Any:
    return None if items is None else as_dotnet_list(items)
