#!/usr/bin/env python3
"""
Generate quartodoc sections for auto-generated table classes.

This script scans the mikeplus.tables.auto_generated module for table classes
and creates a YAML file with quartodoc sections for inclusion in _quarto.yml.
"""

import os
from pathlib import Path
import yaml

# Configuration
AUTO_GENERATED_PATH = Path(__file__).parent.parent / "mikeplus" / "tables" / "auto_generated"
OUTPUT_FILE = Path(__file__).parent / "_table_generated_sections.yml"
BASE_PACKAGE = "mikeplus.tables.auto_generated"


def scan_modules():
    """Scan the auto_generated directory for table modules."""
    modules = []
    
    # Get all python modules that don't start with _ (skip __init__.py, etc.)
    py_files = [f for f in AUTO_GENERATED_PATH.glob("*.py") 
                if not f.name.startswith("_")]
    
    for py_file in py_files:
        module_name = py_file.stem
        if module_name != "table_collection":  # Skip table_collection as it's special
            modules.append(module_name)
    
    return sorted(modules)


def generate_quartodoc_sections():
    """Generate quartodoc sections for table classes and column classes."""
    modules = scan_modules()
    print(f"Found {len(modules)} table modules")
    
    # Create sections
    sections = []
    
    # First add a section for TableCollection
    sections.append({
        "title": "Table Collection",
        "desc": "Main collection of tables",
        "package": BASE_PACKAGE,
        "contents": ["TableCollection"]
    })
    
    # Add a section for all tables and columns
    all_entries = []
    
    # Add an entry for each table class and column class
    for module in modules:
        # Add the table class (ModuleNameTable)
        table_class = f"{module}Table"
        all_entries.append(table_class)
        
        # Add the column class (ModuleNameTableColumns)
        #column_class = f"{module}TableColumns"
        #all_entries.append(column_class)
    
    sections.append({
        "title": "Tables",
        "desc": "Auto-generated table classes and columns",
        "package": BASE_PACKAGE,
        "contents": all_entries
    })
    
    # Write to YAML file
    with open(OUTPUT_FILE, "w") as f:
        yaml.dump({"sections": sections}, f, sort_keys=False)
    
    print(f"Generated quartodoc sections in {OUTPUT_FILE}")
    print(f"Created {len(sections)} sections with {len(all_entries)} entries")
    
    # Provide instructions
    print("\nTo use these sections, manually copy them into _quarto.yml")


if __name__ == "__main__":
    generate_quartodoc_sections()