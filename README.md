![logo](https://raw.githubusercontent.com/DHI/mikepluspy/main/images/logo/mikeplus-py.svg)
# MIKE+Py: Streamline your MIKE+ workflows
 ![Python version](https://img.shields.io/pypi/pyversions/mikeplus.svg)
 [![Full test](https://github.com/DHI/mikepluspy/actions/workflows/full_test.yml/badge.svg)](https://github.com/DHI/mikepluspy/actions/workflows/full_test.yml)
[![PyPI version](https://badge.fury.io/py/mikeplus.svg)](https://badge.fury.io/py/mikeplus)
![OS](https://img.shields.io/badge/OS-Windows-blue)
![Downloads](https://img.shields.io/pypi/dm/mikeplus)

MIKE+Py is an open-source Python package for interacting with MIKE+ model databases (`.sqlite` files). It enables automation of modelling tasks, programmatic data manipulation, scenario management, and simulation execution, enhancing the reproducibility and efficiency of MIKE+ workflows.

## Installation

MIKE+Py can be installed from PyPI using `uv` (or `pip`):

```bash
uv pip install mikeplus
```

> **Note**  
> Use of MIKE+Py requires a valid MIKE+ license.

To install a version compatible with a specific MIKE+ release year (e.g., MIKE+ 2025):

```bash
uv pip install mikeplus==2025.*
```

## Quick Start

Here are a couple of quick examples to get you started:

**Open a database and read table data into a Pandas DataFrame:**

```python
import mikeplus as mp

with mp.open("your_model.sqlite") as db:
    db.tables.msm_Node.to_dataframe()
```

**Open a database and run the active simulation setup:**

```python
import mikeplus as mp

with mp.open("your_model.sqlite") as db:
    db.run() 
```

## Key Features

*   **Database Interaction**: Programmatically open, create, and manage MIKE+ `.sqlite` databases.
*   **Data Manipulation**: Read and modify model data stored in various tables using a fluent API that supports Pandas DataFrames.
*   **Scenario Management**: Access, create, activate, and delete scenarios and alternatives.
*   **Simulation Execution**: Run MIKE+ simulations for different modules (CS, EPANET, SWMM) directly from Python.
*   **Automation**: Automate repetitive tasks such as parameter updates, scenario comparisons, and batch simulations.
*   **Tools Integration**: Programmatic access to some MIKE+ GUI tools.

## Documentation

Comprehensive documentation is available at: [https://dhi.github.io/mikepluspy/](https://dhi.github.io/mikepluspy/)

## Caution: Work with Database Copies

MIKE+Py directly modifies the `.sqlite` database file. There is **no undo** functionality within MIKE+Py for changes made to the database.

**It is strongly recommended to always work on a copy of your MIKE+ database, not the original, to prevent accidental data loss or corruption.**

## Compatibility Issues

There are known compatibility issues when using MIKE+Py alongside other DHI libraries (e.g. MIKE IO, MIKE IO 1D, ModelSkill).

- Importing MIKE IO *after* MIKE+Py is not supported and will cause errors.
- Importing MIKE IO 1D *before* MIKE+Py is not supported and will cause errors.

The following is the suggest import order which works for most use cases, but could still run into issues:

```python
import mikecore
import mikeio
import modelskill as ms
import mikeplus as mp
import mikeio1d
```

