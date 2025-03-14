"""
Entry point for MIKE+ model database operations.
"""
from __future__ import annotations

from typing import Optional, Union
from pathlib import Path

from .tables.auto_generated import TableCollection


def open(model_path: str | Path, create_if_not_exists: bool = False) -> ModelDatabase:
    """Open an existing MIKE+ model database.
    
    Args:
        model_path: Path to the model database file (e.g. "model.sqlite" or "model.mupp")
        create_if_not_exists: If True, create the database if it doesn't exist
        
    Returns:
        A ModelDatabase object for the opened database
        
    Raises:
        FileNotFoundError: If the database doesn't exist and create_if_not_exists is False
        FileExistsError: If the database already exists and create_if_not_exists is True
    """
    pass


def create(model_path: str | Path) -> ModelDatabase:
    """Create a new MIKE+ model database.
    
    Args:
        model_path: Path where the new database will be created        
    Returns:
        A ModelDatabase object for the newly created database
        
    Raises:
        FileExistsError: If the database already exists
    """
    pass


class ModelDatabase:
    """Represents a MIKE+ model database."""
    
    def __init__(self):
        """Initialize a new ModelDatabase."""
        self._db_path = None
        self._mupp_path = None
        self._data_table_container = None
        self._scenario_manager = None
        self._tables = None
        self._is_open = False

    def open(self):
        """Open the model database."""
        pass
    
    def close(self):
        """Close the model database."""
        pass
    
    @property
    def tables(self) -> TableCollection:
        """A collection of tables in the database.

        This property provides access to all tables in the database, and is
        the primary entry point for working with tables.

        Returns:
            TableCollection object
        """
        pass
    
    @property
    def is_open(self) -> bool:
        """Check if the database is open.
        
        Returns:
            True if the database is open, False otherwise
        """
        pass
    
    @property
    def unit_system(self) -> str:
        """Get the unit system of the database.
        
        Returns:
            Unit system string
        """
        pass
    
    @property
    def version(self) -> str:
        """Get the version of the database.
        
        Returns:
            Version string
        """
        pass
    
    @property
    def active_scenario(self) -> str:
        """Get the name of the active scenario.
        
        Returns:
            Name of the active scenario
        """
        pass
    
    @property
    def active_simulation(self) -> str:
        """Get the name of the active simulation.
        
        Returns:
            Name of the active simulation
        """
        pass
    
    @property
    def activate_model(self) -> str:
        """Get the name of the active model.
        
        Returns:
            Name of the active model
        """
        pass
        
    def set_active_scenario(self, scenario_name: str):
        """Set the active scenario.
        
        Args:
            scenario_name: Name of the scenario to activate
        """
        pass
    
    def set_active_simulation(self, simulation_name: str):
        """Set the active simulation.
        
        Args:
            simulation_name: Name of the simulation to activate
        """
        pass
    
    def create_scenario(self, name: str, base_scenario: str):
        """Create a new scenario based on an existing one.
        
        Args:
            name: Name of the new scenario
            base_scenario: Name of the scenario to base the new one on
        """
        pass
