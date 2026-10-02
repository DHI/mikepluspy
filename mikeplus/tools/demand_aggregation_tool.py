"""The demand Aggregation tool from MIKE+ water distribution."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from DHI.Amelia.DomainServices.Services import AmeliaWdEditorService
from DHI.Amelia.GlobalUtility.DataType import CommandStatus
from System.Threading import CancellationTokenSource

from ..database import DatabaseError
from ..dotnet import as_dotnet_list

if TYPE_CHECKING:
    from collections.abc import Callable, Sequence

    from ..database import Database

_PIPE_COEFFICIENTS = (1, 2, 3, 4)


class DemandAggregationTool:
    """The demand Aggregation tool from MIKE+ water distribution.

    Aggregates demand allocations (`mw_DemAlloc`) to junction demands
    (`mw_MDemand`) or to pipe demand coefficients (`mw_Pipe.Coeff1` to
    `Coeff4`). Rows the tool writes to `mw_MDemand` have `GenerateTypeNo` 3
    (allocation); `reset_existing` deletes only those rows, never demands
    entered any other way.

    Every method takes an optional list of demand allocation MUIDs to
    aggregate. Leave it out to aggregate all demand allocations; an empty
    list does nothing, not even `reset_existing`.

    Examples
    --------
    ```python
    >>> from mikeplus import Database
    >>> from mikeplus.tools import DemandAggregationTool
    >>> db = Database("path/to/model.sqlite")
    >>> tool = DemandAggregationTool(db)
    >>> tool.aggregate_to_node_demands(reset_existing=True)
    >>> tool.aggregate_to_pipe_coefficients(["Alloc_1", "Alloc_2"], coefficient=2)
    >>> db.close()
    ```

    """

    def __init__(self, database: Database) -> None:
        """Initialize the DemandAggregationTool with the given Database.

        Parameters
        ----------
        database : Database
            A Database object for the MIKE+ model.

        """
        if not database.is_open:
            database.open()
        self._database = database
        self._service = AmeliaWdEditorService()
        self._service.DataTables = database._data_table_container

    def aggregate_to_node_demands(
        self,
        demand_allocations: Sequence[str] | None = None,
        *,
        reset_existing: bool = False,
        keep_categories: bool = True,
        category: str | None = None,
        pattern: str | None = None,
    ) -> None:
        """Sum the demand allocations of each junction into junction demands.

        As in MIKE+, a sum with any allocation whose `Demand` is NULL is NULL.

        Parameters
        ----------
        demand_allocations : Sequence[str], optional
            MUIDs of the demand allocations to aggregate. By default all;
            an empty list does nothing. Allocations without a junction are
            skipped.
        reset_existing : bool, optional
            If true, first delete the junction demands that earlier
            aggregations wrote. By default False.
        keep_categories : bool, optional
            If true, write one demand per junction for each combination of
            demand category and pattern found in its allocations. If false,
            write a single demand per junction with `category` and `pattern`.
            By default True.
        category : str, optional
            Demand category for the aggregated demands. Only allowed when
            `keep_categories` is false.
        pattern : str, optional
            Demand pattern for the aggregated demands. Only allowed when
            `keep_categories` is false.

        Raises
        ------
        TypeError
            If `demand_allocations` is a str or contains anything but str.
        ValueError
            If `category` or `pattern` is given while `keep_categories` is
            true, or if `demand_allocations` contains MUIDs not in
            `mw_DemAlloc`.

        """
        if keep_categories and (category is not None or pattern is not None):
            raise ValueError(
                "category and pattern apply only when keep_categories is False."
            )
        self._run(
            "aggregate demands to junctions",
            lambda token, ids: self._service.DemAllocEditor_AggregateToNodeDemands(
                reset_existing, keep_categories, category, pattern, token, ids
            ),
            demand_allocations,
        )

    def assign_to_multiple_demands(
        self,
        demand_allocations: Sequence[str] | None = None,
        *,
        reset_existing: bool = False,
    ) -> None:
        """Copy each demand allocation to its junction as a separate demand.

        Unlike `aggregate_to_node_demands`, nothing is summed: every
        allocation becomes one junction demand, keeping its demand, category,
        pattern and meter.

        Parameters
        ----------
        demand_allocations : Sequence[str], optional
            MUIDs of the demand allocations to assign. By default all;
            an empty list does nothing. Allocations without a junction are
            skipped.
        reset_existing : bool, optional
            If true, first delete the junction demands that earlier
            aggregations wrote. By default False.

        Raises
        ------
        TypeError
            If `demand_allocations` is a str or contains anything but str.
        ValueError
            If `demand_allocations` contains MUIDs not in `mw_DemAlloc`.

        """
        self._run(
            "assign demands to junctions",
            lambda token, ids: self._service.DemAllocEditor_AssignToMultipleDemands(
                reset_existing, token, ids
            ),
            demand_allocations,
        )

    def aggregate_to_pipe_coefficients(
        self,
        demand_allocations: Sequence[str] | None = None,
        *,
        coefficient: int = 1,
        reset_existing: bool = False,
    ) -> None:
        """Sum the demand allocations of each pipe into a pipe demand coefficient.

        As in MIKE+, a sum with any allocation whose `Demand` is NULL is NULL.

        Parameters
        ----------
        demand_allocations : Sequence[str], optional
            MUIDs of the demand allocations to aggregate. By default all;
            an empty list does nothing. Allocations without a pipe are
            skipped.
        coefficient : int, optional
            Which pipe demand coefficient to write, 1 to 4 for `Coeff1` to
            `Coeff4`. By default 1.
        reset_existing : bool, optional
            If true, set the coefficient to 0 on pipes with no aggregated
            allocation. If false, leave those pipes unchanged. By default False.

        Raises
        ------
        TypeError
            If `demand_allocations` is a str or contains anything but str.
        ValueError
            If `coefficient` is not 1, 2, 3 or 4, or if `demand_allocations`
            contains MUIDs not in `mw_DemAlloc`.

        """
        if coefficient not in _PIPE_COEFFICIENTS:
            raise ValueError(f"coefficient must be 1, 2, 3 or 4, got {coefficient!r}.")
        field = f"Coeff{coefficient}"
        self._run(
            "aggregate demands to pipe coefficients",
            lambda token, ids: (
                self._service.DemAllocEditor_AggregateToPipeDemandCoefficients(
                    "Demand", reset_existing, field, token, ids
                )
            ),
            demand_allocations,
        )

    def _run(
        self,
        action: str,
        call: Callable[[Any, Any], Any],
        demand_allocations: Sequence[str] | None,
    ) -> None:
        ids = None
        if demand_allocations is not None:
            muids = self._validated_muids(demand_allocations)
            # MIKE+ would still apply reset_existing to an empty list.
            if not muids:
                return
            ids = as_dotnet_list(muids)
        try:
            result = call(CancellationTokenSource().Token, ids)
        except Exception as error:
            raise DatabaseError(f"Failed to {action}: {error}") from None
        # MIKE+ rolls back and returns null on failure, without the error.
        if result is None:
            raise DatabaseError(f"Failed to {action}; no changes were saved.")
        if result.Status == CommandStatus.Failure:
            raise DatabaseError(f"Failed to {action}: {result.Msg}")

    def _validated_muids(self, demand_allocations: Sequence[str]) -> list[str]:
        if isinstance(demand_allocations, str):
            raise TypeError(
                "demand_allocations must be a sequence of MUIDs, not a str; "
                f"use [{demand_allocations!r}]."
            )
        ids = list(demand_allocations)
        not_str = [muid for muid in ids if not isinstance(muid, str)]
        if not_str:
            raise TypeError(
                f"demand_allocations must contain str MUIDs, got {not_str!r}."
            )
        known = set(self._database.tables.mw_DemAlloc.get_muids())
        unknown = [muid for muid in ids if muid not in known]
        if unknown:
            raise ValueError(f"Unknown demand allocation MUIDs: {unknown!r}.")
        return ids
