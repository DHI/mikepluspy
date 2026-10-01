"""The connection tool from MIKE+, for demand allocations."""

from __future__ import annotations

from collections.abc import Iterable
from typing import TYPE_CHECKING, Any, Literal

from DHI.Amelia.GlobalUtility.DataType import CommandStatus
from DHI.Amelia.Tools.GeoCodeTool import GeoCodeEngine
from System.Threading import CancellationTokenSource

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

# Both limits are disabled with -1.
_NO_LIMIT = -1.0


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

        Runs as one undoable command. A demand allocation for which no target
        is found loses any connection it had.

        Parameters
        ----------
        method : str, optional
            How to choose the target, by default "nearest_junction":

            - "nearest_junction": the junction nearest to the demand allocation.
            - "junction_by_nearest_pipe": the end junction, nearest to the
              demand allocation, of the nearest pipe.
            - "junction_by_pipe_id": the end junction, nearest to the demand
              allocation, of the pipe whose MUID equals the demand
              allocation's MUID. Demand allocations without such a pipe are
              skipped.
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
            "nearest_junction", otherwise on `mw_Pipe`.

        Raises
        ------
        ValueError
            If `method` is not one of the values above, a distance or diameter
            limit is not positive, `junction_ids` or `pipe_ids` is empty, or
            `demand_ids` names a demand allocation that does not exist.
        RuntimeError
            If MIKE+ reports that the connection failed.

        """
        if method not in _CONNECTION_TYPES:
            raise ValueError(
                f"Unknown method {method!r}. Use one of {list(_CONNECTION_TYPES)}."
            )
        for name, limit in (
            ("max_distance", max_distance),
            ("max_diameter", max_diameter),
        ):
            if limit is not None and limit <= 0:
                raise ValueError(f"{name} must be positive, got {limit}.")
        demands = None if demand_ids is None else list(demand_ids)
        junctions = _non_empty("junction_ids", junction_ids)
        pipes = _non_empty("pipe_ids", pipe_ids)
        if demands is not None:
            if not demands:
                return
            # MIKE+ would raise at the first unknown MUID, partway through the run.
            unknown = set(demands) - set(self._database.tables.mw_DemAlloc.get_muids())
            if unknown:
                raise ValueError(f"Unknown demand allocations: {sorted(unknown)}")

        tool = GeoCodeEngine(self._dataTables)
        tool.RuningProgress += self._on_tool_runing_progress
        result = tool.GeocodeDemand(
            _optional_list(demands),
            _optional_list(junctions),
            _optional_list(pipes),
            -1,  # not limited to the GUI selection
            _NO_LIMIT if max_distance is None else float(max_distance),
            _CONNECTION_TYPES[method],
            _NO_LIMIT if max_diameter is None else float(max_diameter),
            where,
            CancellationTokenSource().Token,
        )
        if result is not None and result.Status == CommandStatus.Failure:
            raise RuntimeError(
                result.Msg or "MIKE+ failed to connect the demand allocations."
            )

    def _on_tool_runing_progress(self, source: Any, args: Any) -> None:
        print(args.Msg)


def _non_empty(name: str, items: Iterable[str] | None) -> list[str] | None:
    # MIKE+ treats an empty list like None, as no restriction at all.
    if items is None:
        return None
    items = list(items)
    if not items:
        raise ValueError(f"{name} is empty. Pass None to allow all.")
    return items


def _optional_list(items: list[str] | None) -> Any:
    return None if items is None else as_dotnet_list(items)
