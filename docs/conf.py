"""Configuração do Sphinx para a documentação do projeto EasyOrder.

Define extensões, caminhos de import, tema HTML e opções do Napoleon para
processar docstrings no estilo Google e gerar a documentação.
"""

import os
import sys
from datetime import datetime

# -- Path setup: add ../src to import path
sys.path.insert(0, os.path.abspath(os.path.join(__file__, "..", "..", "src")))

# -- Project information
project = "EasyOrder"
author = "EasyOrder Team"
release = "0.1.0"
copyright = f"{datetime.now():%Y}, {author}"

# -- General configuration
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",  # Google/NumPy style docstrings
    "sphinx.ext.viewcode",
]

autosummary_generate = True
autodoc_typehints = "description"
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_use_rtype = True

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
