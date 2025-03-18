#!/usr/bin/env python
"""
Generate Table Classes Script

A script that generates Python table classes from MIKE+ database tables.
This tool is used during development to automatically generate table class files.

Usage:
    python scripts/generate_tables.py [options]

Options:
    --output-dir, -o    Directory where generated code will be saved 
                        (default: ./mikeplus/tables/auto_generated)
    --database, -d      Path to MIKE+ database file (optional)

Examples:
    # Generate table classes using default settings
    python scripts/generate_tables.py

    # Generate table classes to a custom directory
    python scripts/generate_tables.py --output-dir ./custom/output/directory

    # Generate table classes from a specific database
    python scripts/generate_tables.py --database ./path/to/database.sqlite

The script generates:
1. A Python class file for each table in the database
2. a table_collection.py file containing a TableCollection class for accessing all tables
3. an __init__.py file to make the generated code importable as a package

Notes:
- This script is a development tool and requires Jinja2 to be installed
  (install with: pip install -e ".[dev]")
- All generated files have a warning in their docstrings that they should not
  be manually modified.
"""

import argparse
from pathlib import Path
from typing import Type
from jinja2 import Environment, FileSystemLoader
import tempfile
import uuid


from mikeplus.database import Database
from mikeplus.tables.base_table import BaseTable
from mikeplus.tables.base_table_collection import BaseTableCollection


class AutoTableClassGenerator:
    """
    Automatically generate tables classes and TableCollection from MIKE+ database.
    
    Table classes are light-weight wrappers of IMuTable. TableCollection is a dict-like
    accessor for the generated table classes.
    
    Args:
        output_dir: Directory where generated code will be saved. Parent directories will be created if needed.
        data_table_container: .NET IDataTableContainer object
        base_table: Base class that all generated table classes will inherit from.
        base_table_collection: Base class that the table collection will inherit from.
    """
    
    def __init__(
        self,
        *,
        output_dir: Path = Path(__file__).parent.parent / "mikeplus/tables/auto_generated",
        data_table_container = None,
        base_table: Type = BaseTable,
        base_table_collection: Type = BaseTableCollection,
    ):
        """
        Initialize the AutoTableGenerator.
        
        Args:
            output_dir: Directory where generated code will be saved. Parent directories will be created if needed.
            data_table_container: .NET IDataTableContainer object
            base_table: Base class that all generated table classes will inherit from.
            base_table_collection: Base class that the table collection will inherit from.
        """
        self.output_dir = Path(output_dir)

        self.data_table_container = data_table_container
        if data_table_container is None:
            self.data_table_container = self.create_data_table_container()
        
        self.base_table = base_table
        self.base_table_collection = base_table_collection
        
        # Setup Jinja2 environment
        template_dir = Path(__file__).parent / "table_templates"
        self.jinja_env = Environment(loader=FileSystemLoader(template_dir))
        
        # Load templates from files
        self.table_template = self.jinja_env.get_template("table_class.j2")
        self.table_collection_template = self.jinja_env.get_template("table_collection.j2")
        self.init_template = self.jinja_env.get_template("init.j2")
        
        self.generated_tables = {}

    def create_data_table_container(self):
        """
        Create an empty data table container.
        """
        # Create a path to a temporary sqlite database without creating the file
        temp_dir = tempfile.TemporaryDirectory(delete=False)
        temp_db_path = Path(temp_dir.name) / f"{uuid.uuid4()}.sqlite"

        db = Database.create(temp_db_path)
        db.close()
        return db._data_table_container

    def generate(self) -> None:
        """
        Generate all table classes, the table collection, and the init file.
        """
        # Ensure output directory exists and clear previous files
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.clear_generated_files()
        
        # Generate table class files for all tables
        for table in self.data_table_container.AllTables:
            self.generate_table_class(table)
        
        # Generate table collection and __init__.py
        self.generate_table_collection_file()
        self.generate_init_file()

    def clear_generated_files(self) -> None:
        """
        Clear all auto-generated files from the output directory.
        """
        py_files = list(self.output_dir.glob("**/*.py"))
        for file_path in py_files:
            file_path.unlink()
        
        self.generated_tables = {}

    def generate_table_class(self, table) -> None:
        """
        Generate a table class file for a specific table.
        """
        # Generate names
        module_name = table.TableName
        class_name = table.TableName + 'Table'
        
        # Build template context
        field_constants = [
            {"name": column.Field, "value": column.Field}
            for column in table.Columns
        ]
        
        context = {
            'table_name': table.TableName,
            'table_display_name': table.TableDisplayName,
            'class_name': class_name,
            'field_constants': field_constants,
            'base_table_module': self.base_table.__module__,
            'base_table_name': self.base_table.__name__,
        }
        
        # Generate and write code
        code = self.table_template.render(**context)
        file_path = self.output_dir / f"{module_name}.py"
        with open(file_path, "w") as f:
            f.write(code)
        
        # Store metadata for table collection generation
        self.generated_tables[module_name] = {
            'path': str(file_path),
            'class_name': class_name,
            'table_name': module_name,
            'table_display_name': table.TableDisplayName
        }

    def generate_table_collection_file(self) -> None:
        """
        Generate the table_collection.py file in the output directory.
        """
        # Build template context
        context = {
            'base_table_collection_module': self.base_table_collection.__module__,
            'base_table_collection': self.base_table_collection.__name__,
            'base_table_module': self.base_table.__module__,
            'base_table_name': self.base_table.__name__,
            'tables': list(self.generated_tables.values()),
        }
        
        # Generate and write code
        code = self.table_collection_template.render(**context)
        file_path = self.output_dir / "table_collection.py"
        with open(file_path, "w") as f:
            f.write(code)
    
    def generate_init_file(self) -> None:
        """
        Generate the __init__.py file for the generated package.
        """
        init_path = self.output_dir / "__init__.py"
        
        # Build template context
        context = {
            'tables': list(self.generated_tables.values()),
        }
        
        # Generate and write code
        code = self.init_template.render(**context)
        with open(init_path, "w") as f:
            f.write(code)


def main():
    """
    Main entry point for the generate_tables script.
    """
    parser = argparse.ArgumentParser(description='Generate table classes from MIKE+ database')
    parser.add_argument('--output-dir', '-o', type=str, default='./mikeplus/tables/auto_generated',
                        help='Output directory for generated files')
    parser.add_argument('--database', '-d', type=str,
                        help='Path to MIKE+ database file (optional)')
    
    args = parser.parse_args()
    
    # Setup basic generator options
    kwargs = {'output_dir': Path(args.output_dir)}
    
    # Add database if provided
    if args.database:
        print(f"Using database: {args.database}")
        db = Database(args.database)
        kwargs['data_table_container'] = db._data_table_container
    
    print(f"Generating table classes to {args.output_dir}...")
    generator = AutoTableClassGenerator(**kwargs)
    generator.generate()
    print(f"Generated {len(generator.generated_tables)} table classes.")


if __name__ == "__main__":
    main()

__all__ = ['AutoTableClassGenerator']