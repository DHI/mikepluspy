"""Base table class for MIKE+ database tables with a node-based geometry."""
from __future__ import annotations

from .base_geometry_table import BaseGeometryTable
from .base_table_columns import BaseColumns # noqa: F401

class BaseNodeTable(BaseGeometryTable):
    """Base class representing a database table with node-based geometry."""

    def get_number_of_links(self, node_muid: str) -> int:
        """Get the number of links connected to a node.

        Parameters
        ----------
        node_muid : str
            MUID of the node

        Returns
        -------
        int
            Number of links connected to the node

        """
        return self._net_table.GetNumberofLinks(node_muid)

    def get_number_of_links_enabled(self, node_muid: str) -> int:
        """Get the number of enabled links connected to a node.

        Parameters
        ----------
        node_muid : str
            MUID of the node

        Returns
        -------
        int
            Number of enabled links connected to the node

        """
        return self._net_table.GetNumOfLinksEnabled(node_muid)

    def get_downstream_links(self, node_muid: str) -> list[str]:
        """Get links MUIDs where specified node MUID is the downstream node.

        Parameters
        ----------
        node_muid : str
            MUID of the node

        Returns
        -------
        list[str]
            List of link MUIDs.

        """
        return list(self._net_table.GetDownstreamLinks(node_muid))

    def get_upstream_links(self, node_muid: str) -> list[str]:
        """Get link MUIDs where specified node MUID is the upstream node.

        Parameters
        ----------
        node_muid : str
            MUID of the node

        Returns
        -------
        list[str]
            List of MUIDs of the upstream links connected to the node

        """
        return list(self._net_table.GetUpstreamLinks(node_muid))
