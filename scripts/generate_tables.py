"""
Generate Table Classes Script

A script that generates Python table classes from MIKE+ database tables.
This uses the AutoTableClassGenerator from the mikeplus.tables module.

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
2. A table_collection.py file containing a TableCollection class for accessing all tables
3. An __init__.py file to make the generated code importable as a package

Note: This script requires the mikeplus package to be installed (typically in editable mode
for developers with: pip install -e .).
"""

import argparse
from pathlib import Path

from mikeplus.tables.auto_table_class_generator import AutoTableClassGenerator
from mikeplus.database import Database


def main():
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
