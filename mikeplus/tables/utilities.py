"""
Utility functions for working with tables and generating code.
"""
from typing import Any
from pathlib import Path


def generate_table_classes(auto_generate_dir: str | Path):
    """Generate table class code for all tables in the database.
    
    Args:
        auto_generate_dir: Directory where generated code will be saved
    """
    pass

def generate_table_class_code(net_table: Any) -> str:
    """Generate Python code for a table class based on table metadata.
    
    Args:   
        net_table: The .NET table to generate code for
        
    Returns:
        A string containing the Python code for the table class
    """
    pass
