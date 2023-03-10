# Configuration file for the Sphinx documentation builder.
import furo

project = 'cryptographyComplements'
copyright = '2023, Forzo'
author = 'Forzo'
release = 'latest'

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'furo'
html_static_path = ['_static']

master_doc = 'index'