# Configuration file for the Sphinx documentation builder.
import os, sys

# sys.path.insert(0, os.path.abspath('.'))
# sys.path.insert(0, os.path.abspath('./docs'))

project = 'cryptographyComplements'
copyright = '2023, Forzo'
author = 'Forzo'
release = 'latest'

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

master_doc = 'index'