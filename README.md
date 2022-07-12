[![Latest Release](http://img.shields.io/github/release/SDM-TIB/S2Spy.svg?logo=github)](https://github.com/SDM-TIB/S2Spy/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[![Python Versions](https://img.shields.io/pypi/pyversions/S2S-py)](https://pypi.org/project/S2S-py)
[![Package Format](https://img.shields.io/pypi/format/S2S-py)](https://pypi.org/project/S2S-py)
[![Package Status](https://img.shields.io/pypi/status/S2S-py)](https://pypi.org/project/S2S-py)
[![Package Version](https://img.shields.io/pypi/v/S2S-py)](https://pypi.org/project/S2S-py)

# S2Spy

S2Spy is a Python-based reference implementation of [SHACL2SPARQL](https://github.com/rdfshapes/shacl-sparql).

First, install the required dependencies:
```bash
python3 -m pip install -r requirements.txt
```

Assuming you have a SPARQL endpoint running under http://localhost:14000/sparql, you can execute the tool with the following command:
```bash
python3 main.py -d path/to/your/shacl/shapes http://localhost:14000/sparql /path/where/to/store/output
```

# Note
The reference implementation was used in the WWW '21 paper of [Trav-SHACL](https://github.com/SDM-TIB/Trav-SHACL).
It is not a fully functional Python version of SHACL2SPARQL. For example, it assumes that all shapes have a target definition.
It merely served to make SHACL2SPARQL and Trav-SHACL comparable by getting rid of the performance difference in Python and Java.