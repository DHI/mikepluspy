"""The Create Valves from Point Locations tool from MIKE+."""

from __future__ import annotations

import os
from typing import TYPE_CHECKING

from DHI.Amelia.DomainServices.Services import AmeliaMapService
from DHI.Amelia.GlobalUtility.DataType import MUModelOption
from DHI.Amelia.Tools.CreateValveFromPntToolEngine import (
    CreateValveFromPntToolEngine,
)

from ..dotnet import DotNetConverter

if TYPE_CHECKING:
    from ..database import Database


class CreateValvesFromPointsTool:
    """The Create Valves from Point Locations tool from MIKE+ (water distribution only).

    Reads a point shapefile and adds one valve to `mw_Valve` per point. A point
    within the search radius of a junction with one or two pipes gets a valve
    at that junction: the valve takes the first `valve_length` of a pipe and a
    new junction joins the two. Otherwise the nearest pipe within the search
    radius is split where the point projects onto it, and the valve takes
    `valve_length` centred there. Points that can't be placed are skipped with
    a message.

    The points must be in the model's coordinate system.

    Examples
    --------
    ```python
    >>> import mikeplus as mp
    >>> from mikeplus.tools import CreateValvesFromPointsTool
    >>> db = mp.open("path/to/model.sqlite")
    >>> tool = CreateValvesFromPointsTool(db)
    >>> messages = tool.run(
    ...     "path/to/valves.shp",
    ...     search_radius=5.0,
    ...     valve_length=1.0,
    ...     muid_field="ID",
    ...     type_field="VTYPE",
    ... )
    >>> print(messages[0])
    2 valves have been created out of 3 points in the input file
    >>> db.close()
    ```

    """

    def __init__(self, database: Database) -> None:
        """Initialize the CreateValvesFromPointsTool with the given Database.

        Parameters
        ----------
        database : Database
            A Database object for a MIKE+ water distribution model.

        """
        if not database.is_open:
            database.open()
        self._dataTables = database._data_table_container

    def run(
        self,
        points_file: str | os.PathLike[str],
        search_radius: float,
        valve_length: float,
        *,
        muid_field: str | None = None,
        type_field: str | None = None,
        status_field: str | None = None,
        diameter_field: str | None = None,
        setting_field: str | None = None,
        description_field: str | None = None,
    ) -> list[str]:
        """Create valves at the points in a shapefile.

        The `*_field` arguments name the shapefile column to read each valve
        attribute from. Attributes without a column keep the MIKE+ defaults.
        Values that can't be read fall back to a default and add a message.

        Parameters
        ----------
        points_file : str or os.PathLike
            Path to a point shapefile (`.shp`).
        search_radius : float
            How far from each point to look for a junction or pipe, in model
            units.
        valve_length : float
            Length of each new valve, in model units.
        muid_field : str, optional
            Column with the valve ID. Missing or already used IDs get a
            generated one.
        type_field : str, optional
            Column with the valve type: a number from 1 to 6 or one of `PRV`,
            `PSV`, `PBV`, `FCV`, `TCV` and `GPV`. Other values become `PRV`.
        status_field : str, optional
            Column with the valve status: 0 (regulating), 1 (open) or
            2 (closed). Other values become regulating.
        diameter_field : str, optional
            Column with the valve diameter.
        setting_field : str, optional
            Column with the valve setting.
        description_field : str, optional
            Column with the valve description.

        Returns
        -------
        list[str]
            Messages from MIKE+. The first summarises how many valves were
            created out of how many points; the rest explain each point that
            was skipped and each value that couldn't be imported.

        Raises
        ------
        ValueError
            If the model is not a water distribution model, or if
            `search_radius` or `valve_length` is not positive.
        FileNotFoundError
            If `points_file` does not exist.
        RuntimeError
            If MIKE+ reports that the tool failed.

        """
        if self._dataTables.ActiveModel != MUModelOption.WD_EPANET:
            raise ValueError(
                "Creating valves from points needs a water distribution model, "
                f"but the active model is {self._dataTables.ActiveModel}."
            )
        if search_radius <= 0:
            raise ValueError(f"search_radius must be positive, got {search_radius}.")
        if valve_length <= 0:
            raise ValueError(f"valve_length must be positive, got {valve_length}.")
        points_file = os.fspath(points_file)
        if not os.path.isfile(points_file):
            raise FileNotFoundError(points_file)

        mapped_fields = {
            "MUID": muid_field,
            "TypeNo": type_field,
            "StatusNo": status_field,
            "Diameter": diameter_field,
            "Setting": setting_field,
            "Description": description_field,
        }
        field_infos = DotNetConverter.to_dotnet_string_dictionary(
            {key: col for key, col in mapped_fields.items() if col is not None}
        )

        # The map service is only used to split pipes, which needs nothing but the tables.
        map_service = AmeliaMapService()
        map_service.DataTables = self._dataTables
        engine = CreateValveFromPntToolEngine(self._dataTables, map_service)
        succeeded, messages = engine.CreateValve(
            os.path.abspath(points_file),
            float(search_radius),
            float(valve_length),
            field_infos,
            None,
        )
        messages = DotNetConverter.from_dotnet_list(messages)
        if not succeeded:
            raise RuntimeError(
                "MIKE+ failed to create valves from points: " + "; ".join(messages)
            )
        return messages
