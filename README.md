![logo](https://raw.githubusercontent.com/DHI/mikepluspy/main/images/logo/mikeplus-py.svg)
# MIKE+Py: automate your workflows.
 ![Python version](https://img.shields.io/pypi/pyversions/mikeplus.svg)
 [![Full test](https://github.com/DHI/mikepluspy/actions/workflows/full_test.yml/badge.svg)](https://github.com/DHI/mikepluspy/actions/workflows/full_test.yml)
[![PyPI version](https://badge.fury.io/py/mikeplus.svg)](https://badge.fury.io/py/mikeplus)
![OS](https://img.shields.io/badge/OS-Windows-blue)
![Downloads](https://img.shields.io/pypi/dm/mikeplus)

MIKE+Py is a python interface for MIKE+. Its main features include:
* Modifying the MIKE+ database in a way that is consistent with the GUI.
* Run different kinds of simulations (e.g. MIKE 1D, EPANET, SWMM)
* Access certain GUI tools pythonically (e.g. import/export tool).

> [!CAUTION]
> MIKE+Py is experimental and under development.
> * Be aware that there may be bugs or unexpected behavior - use with caution.
> * Always make copies of your MIKE+ databases and verify the outcome of scripts.
> * If you encounter any issues or have any feedback, please report them on [GitHub Issues](https://github.com/DHI/mikepluspy/issues).

## Requirements
* MIKE+ 2024 (or greater) with valid license
* Python x64 3.9 to 3.12
* Windows

## Installation

The version of MIKE+Py you install must match the version of MIKE+ installed on your desktop. 

| MIKE+ Version | Install command|
|:--------------|:---------------|
| MIKE+ 2025 | `pip install mikeplus` |
| MIKE+ 2024 Update 1 | `pip install mikeplus==2024.1.*` |
| MIKE+ 2024 | `pip install mikeplus==2024.0.*` |


## Examples
Please check out our [collection of jupyter notebooks] (https://github.com/DHI/mikepluspy/tree/main/notebooks) to get started with MIKE+Py.

## Known issues

There's currently a known issue of using MIKE+Py together with MIKE IO and MIKE IO 1D.  We are working on fixing this and appreciate your patience.

Workarounds:
* Importing MIKE IO 1D *after* MIKE+Py will work.
* Using Python's multiprocessing library to split imports (and workflows) into separate processes.
* Split MIKE IO  and MIKE+Py / MIKE IO 1D workflows into separate scripts.

## Where can I get help?
* Bugs - [GitHub Issues](https://github.com/DHI/mikepluspy/issues)
* Feature requests - [GitHub Issues](https://github.com/DHI/mikepluspy/issues) 
* Other - [GitHub Discussions](http://github.com/DHI/mikepluspy/discussions)