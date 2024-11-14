![logo](https://raw.githubusercontent.com/DHI/mikepluspy/main/images/logo/mikeplus-py.svg)
# MIKE+Py: automate your workflows.

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
| MIKE+ 2024 Update 1 | `pip install mikeplus==2024.1` |
| MIKE+ 2024 | `pip install mikeplus==2024.0` |


## Examples
Please check out our [collection of jupyter notebooks] (https://github.com/DHI/mikepluspy/tree/main/notebooks) to get started with MIKE+Py.

## Where can I get help?
* Bugs - [GitHub Issues](https://github.com/DHI/mikepluspy/issues)
* Feature requests - [GitHub Issues](https://github.com/DHI/mikepluspy/issues) 
* Other - [GitHub Discussions](http://github.com/DHI/mikepluspy/discussions)