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
* Python x64 3.8 to 3.12
* Windows operating system

## Installation

The version of MIKE+Py you install must match the version of MIKE+ installed on your desktop. 

> [!NOTE]
> MIKE+Py is not yet available on PyPI since it is in the initial development stages.

| MIKE+ Version | Install command|
|:--------------|:---------------|
| MIKE+ 2024    | `pip install https://github.com/DHI/mikepluspy/archive/refs/tags/v2024.0-latest.zip` |


## Examples
Please check out the jupyter notebooks here: https://github.com/DHI/mikepluspy/tree/main/notebooks

## Where can I get help?
* General help, new ideas and feature requests - [GitHub Discussions](http://github.com/DHI/mikepluspy/discussions) 
* Bugs - [GitHub Issues](https://github.com/DHI/mikepluspy/issues) 


## Getting started
```
import mikeplus as mp
```


## Data table
See the [Data table access guide](datatableaccess.md)


## Engines
See the [Engines guide](engines.md)


## Tools
See the [Tools guide](tools.md)
