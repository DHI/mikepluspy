"""
Tests for the table code generation functionality.
"""
import importlib
import sys
from pathlib import Path
import tempfile
import pytest
import shutil

from scripts.generate_tables import AutoTableClassGenerator

class TestTableGeneration:
    """Tests for the table code generation functionality."""
    
    @pytest.fixture
    def temp_output_dir(self):
        """Fixture providing a temporary directory for generated code."""
        temp_dir = tempfile.mkdtemp()
        yield Path(temp_dir)
        # Clean up
        shutil.rmtree(temp_dir)
    
    @pytest.fixture
    def real_table_name(self):
        """Fixture providing a real table name that exists in the database."""
        return "msm_Project"
    
    @pytest.fixture
    def generator(self, temp_output_dir):
        """Fixture providing an initialized table generator."""
        generator = AutoTableClassGenerator(
            output_dir=temp_output_dir,
        )
        return generator
    
    def test_generate_single_table_class(self, generator, real_table_name, temp_output_dir):
        """Test generating a single table class from a table name."""
        # Get the table from the database
        table = generator.data_table_container.GetTable(real_table_name)
        
        # Generate the table class
        generator.generate_table_class(table)
        
        # Check that the file was created
        expected_file = temp_output_dir / f"{real_table_name}.py"
        assert expected_file.exists(), f"Expected file {expected_file} was not created"
        
        # Check that the file contains the expected class name
        expected_class_name = f"{real_table_name}Table"
        with open(expected_file, "r") as f:
            content = f.read()
            assert f"class {expected_class_name}" in content
    
    def test_generate_all_tables(self, generator, temp_output_dir):
        """Test generating all table classes."""
        # Generate all tables
        generator.generate()
        
        # Check that the directory contains generated files
        assert len(list(temp_output_dir.glob("*.py"))) > 0
        
        # Check that all expected tables were generated
        expected_tables = {t.TableName for t in generator.data_table_container.AllTables}
        generated_tables = {t.stem for t in temp_output_dir.glob("*.py")}
        generated_tables.discard("__init__")
        generated_tables.discard("table_collection")
        
        # Check that all expected tables were generated
        assert expected_tables == generated_tables
        
        # Check that table_collection.py was created
        assert (temp_output_dir / "table_collection.py").exists()
        
        # Check that __init__.py was created
        assert (temp_output_dir / "__init__.py").exists()
        
        # Check specific known tables
        known_tables = ["msm_Node", "msm_Link", "msm_Catchment"]
        for table in known_tables:
            table_file = temp_output_dir / f"{table}.py"
            assert table_file.exists(), f"Expected table file {table_file} not found"
    
    def test_generated_code_can_be_imported_and_used(self, generator, temp_output_dir):
        """Test that generated code can be imported and used."""
        # Generate all tables
        generator.generate()
        
        # Add temp directory to sys.path to allow imports
        sys.path.insert(0, str(temp_output_dir.parent))
        
        try:
            # Import the generated package
            package_name = temp_output_dir.name
            module = importlib.import_module(package_name)
            
            # Check that TableCollection is available
            assert hasattr(module, "TableCollection")
            
            # Create a TableCollection instance
            table_collection = module.TableCollection(generator.data_table_container)
            
            # Check that we can access tables
            assert hasattr(table_collection, "msm_Node")
            
            # Test accessing table data
            node_table = table_collection.msm_Node
            assert node_table is not None
            
            # Test field access
            assert hasattr(node_table.Fields, "MUID")
            
            # Import a specific table class as well
            table_name = next(iter(generator.generated_tables.keys()))
            table_class_name = f"{table_name}Table"
            
            # Check that the table class is available
            assert hasattr(module, table_class_name)
        finally:
            # Clean up sys.path
            if str(temp_output_dir.parent) in sys.path:
                sys.path.remove(str(temp_output_dir.parent))
