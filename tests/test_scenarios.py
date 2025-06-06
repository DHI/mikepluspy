"""
Tests for the scenario management API.
"""
import pytest
from pathlib import Path

import mikeplus as mp
from mikeplus.scenarios import Scenario, Alternative


def test_api_access_scenarios_and_alternatives(sirius_db):
    """
    Test the basic usage flow of the scenario API using an actual database.
    """
    # Open a database using a test-specific isolated copy
    db = mp.open(sirius_db)
    
    # Access scenarios
    active_scenario = db.scenarios.active
    base_scenario = db.scenarios.base
    
    # Verify scenario properties
    assert isinstance(active_scenario, Scenario)
    assert isinstance(base_scenario, Scenario)
    assert active_scenario.name is not None
    assert base_scenario.name is not None
    
    # Test accessing specific alternative groups we know exist in the sirius_db
    expected_groups = [
        "CS Network data",
        "River network data",
        "Loads and boundaries data",
        "Catchments and hydrology data",
        "Transport data",
        "Control rules data",
        "Long term statistics data",
        "Profiles and curves",
        "2D overland",
        "2D boundaries data"
    ]
    
    for group_name in expected_groups:
        # Verify we can access the group by name
        alt_group = db.alternative_groups[group_name]
        assert alt_group is not None
        assert alt_group.name == group_name
        assert len(alt_group.tables) > 0
        
        # Check base and active alternatives are available
        assert alt_group.base is not None
        assert alt_group.active is not None
    
    # Test getting alternative group by table name
    # Use the "Catchments and hydrology data" group which should have msm_Catchment table
    catchment_group = db.alternative_groups["Catchments and hydrology data"]
    if catchment_group.tables:  # Make sure there are tables in this group
        table_name = catchment_group.tables[0]  # Get the first table
        group_by_table = db.alternative_groups.by_table(table_name)
        assert group_by_table is not None
        assert table_name in group_by_table.tables


def test_api_create_and_activate_scenario(sirius_db):
    """
    Test a real workflow of creating alternatives and scenarios using the new API.
    """
    # Open a database using a test-specific isolated copy
    db = mp.open(sirius_db)
    
    # Simple scenario name - no need for uniqueness since the database is fresh
    scenario_name = "Test Scenario"
    
    # Step 1: Get catchment alternative group and its base alternative
    catchment_group = db.alternative_groups["Catchments and hydrology data"]
    base_alt = catchment_group.base
    
    # Step 2: Create a new alternative from the base alternative
    new_alt = catchment_group.create(name=scenario_name, parent=base_alt)
    
    # Step 3: Create a new scenario 
    new_scenario = db.scenarios.create(name=scenario_name, parent=db.scenarios.base)
    
    # Step 4: Set the new alternative for the new scenario
    new_scenario.set_alternative(new_alt)
    
    # Step 5: Activate the new scenario
    new_scenario.activate()
    
    # Verify the scenario is now active
    assert db.scenarios.active.id == new_scenario.id
    
    # Verify the alternative is set for the catchment group
    assert catchment_group.active.id == new_alt.id
    
    # Verify we can find our scenario by name
    found_scenario = db.scenarios.by_name(scenario_name)
    assert found_scenario is not None
    assert found_scenario.id == new_scenario.id
