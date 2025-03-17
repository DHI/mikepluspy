"""
AutoTableClassGenerator - Automatically generate tables classes and TableCollection from MIKE+ database.
"""
from typing import Dict, Type
from pathlib import Path
from string import Template
import tempfile
import uuid


from ..database import Database
from .base_table import BaseTable
from .base_table_collection import BaseTableCollection

class AutoTableClassGenerator:
    """
    Automatically generate tables classes and TableCollection from MIKE+ database.
    
    Table classes are light-weight wrappers of IMuTable. TableCollection is a dict-like
    accessor for the generated table classes.
    
    Args:
        output_dir: Directory where generated code will be saved. Parent directories will be created if needed.
        data_table_container: .NET IDataTableContainer object
        table_template_file: Path to a file containing the template for generated classes.
        table_collection_template_file: Path to a file containing the template for the table collection.
        base_table: Base class that all generated table classes will inherit from.
        base_table_collection: Base class that the table collection will inherit from.
    """
    
    def __init__(
        self,
        *,
        output_dir: Path = Path(__file__).parent / "auto_generated",
        data_table_container = None,
        table_template_file: Path = Path(__file__).parent / "auto_generated_table_template.txt",
        table_collection_template_file: Path = Path(__file__).parent / "table_collection_template.txt",
        base_table: Type = BaseTable,
        base_table_collection: Type = BaseTableCollection,
    ):
        """
        Initialize the AutoTableGenerator.
        
        Args:
            output_dir: Directory where generated code will be saved. Parent directories will be created if needed.
            data_table_container: .NET IDataTableContainer object
            table_template_file: Path to a file containing the template for generated classes.
            table_collection_template_file: Path to a file containing the template for the table collection.
            base_table: Base class that all generated table classes will inherit from.
            base_table_collection: Base class that the table collection will inherit from.
        """
        self.output_dir = Path(output_dir)

        self.data_table_container = data_table_container
        if data_table_container is None:
            self.data_table_container = self.create_data_table_container()
        
        self.base_table = base_table
        self.base_table_collection = base_table_collection
        
        with open(table_template_file, 'r') as f:
            template_content = f.read()
        self.table_template = Template(template_content)
        
        with open(table_collection_template_file, 'r') as f:
            template_content = f.read()
        self.table_collection_template = Template(template_content)
        
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
        self.clear_generated_files()
        self.generate_table_class_files()
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

    def get_table_template_vars(self, table) -> Dict[str, str]:
        """
        Get the variables to be used in the table template.
        """
        vars = {}

        vars['table_name'] = table.TableName
        vars['table_display_name'] = table.TableDisplayName
        vars['class_name'] = table.TableName + 'Table'
        
        field_constants = []
        for column in table.Columns:
            field_name = column.Field
            field_constants.append(f"        {field_name} = \"{field_name}\"")
        field_constants_str = '\n'.join(field_constants)
        vars['field_constants'] = field_constants_str

        vars['base_class_module'] = self.base_table.__module__
        vars['base_class_name'] = self.base_table.__name__
        
        return vars
    
    def generate_table_class_code(self, table) -> str:
        """
        Generate Python class code for a given IMuTable.
        """
        vars = self.get_table_template_vars(table)
        return self.table_template.substitute(**vars)
    
    def generate_table_class_files(self) -> None:
        """
        Generate table classes for all tables in the database.
        """
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        for table in self.data_table_container.AllTables:
            module_name = self.generate_table_module_name(table)
            class_name = self.generate_table_class_name(table)
            code = self.generate_table_class_code(table)
            file_path = self.output_dir / f"{module_name}.py"
            with open(file_path, "w") as f:
                f.write(code)
            
            self.generated_tables[module_name] = {
                'path': str(file_path),
                'class_name': class_name,
                'table_name': module_name,
                'table_display_name': table.TableDisplayName
            }

    def generate_table_module_name(self, table) -> str:
        """
        Generate the module name for a given table.
        """
        return table.TableName

    def generate_table_class_name(self, table) -> str:
        """
        Generate the class name for a given table.
        """
        return table.TableName + 'Table'

    def generate_table_collection_vars(self) -> Dict[str, str]:
        """
        Get the variables to be used in the table collection template.
        """
        vars = {}

        vars['base_table_collection_module'] = self.base_table_collection.__module__
        vars['base_table_collection'] = self.base_table_collection.__name__
        vars['table_imports'] = self.generate_table_imports()

        table_property_template = "    @property\n"
        table_property_template += "    def $table_name(self) -> $table_class_name:\n"
        table_property_template += '        """Table \'$table_name\' ($table_display_name)"""\n'
        #table_property_template += "        return self._tables['$table_name']\n"
        table_property_template += "        return None\n"
        table_property_template = Template(table_property_template)
        
        table_properties = []
        for table in self.generated_tables.values():
            table_property = table_property_template.substitute(
                table_name=table['table_name'],
                table_class_name=table['class_name'],
                table_display_name=table['table_display_name'],
            )
            table_properties.append(table_property)
        
        vars['table_properties'] = '\n'.join(table_properties)
        return vars

    def generate_table_collection_code(self) -> str:
        """
        Generate Python code for the table collection.
        """
        vars = self.generate_table_collection_vars()
        return self.table_collection_template.substitute(**vars)

    def generate_table_collection_file(self) -> None:
        """
        Generate the table_collection.py file in the output directory.
        """
        code = self.generate_table_collection_code()
        file_path = self.output_dir / "table_collection.py"
        with open(file_path, "w") as f:
            f.write(code)

    def generate_table_imports(self) -> str:
        """
        Generate the table imports for the table collection.
        """
        table_imports = "\n".join(f"from .{table['table_name']} import {table['class_name']}" for table in self.generated_tables.values())
        return table_imports
    
    def generate_init_file(self) -> None:
        """
        Generate the __init__.py file for the generated package.
        """
        init_path = self.output_dir / "__init__.py"
        
        with open(init_path, "w") as f:
            f.write('"""Auto-generated table classes for MIKE+ database.\n\n')
            f.write('DO NOT MANUALLY MODIFY THIS PACKAGE! Use AutoTableClassGenerator to regenerate.\n\n"""\n\n')
            
            table_imports = self.generate_table_imports()
            f.write(table_imports)
            
            f.write('\nfrom .table_collection import TableCollection\n\n')
            
            all_classes = [table_info['class_name'] for table_info in self.generated_tables.values()]
            all_classes.append('TableCollection')
            all_str = repr(all_classes).replace("'", '"')
            f.write(f'__all__ = {all_str}\n')
