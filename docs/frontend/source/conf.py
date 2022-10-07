# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PollCord'
copyright = '2022, Neeloy Gomes, Tyler Craine, Abhishek Gupta, Abhimanyu Bellam, Vishal Veera Reddy'
author = 'Neeloy Gomes, Tyler Craine, Abhishek Gupta, Abhimanyu Bellam, Vishal Veera Reddy'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['autoapi.extension']

autoapi_type = 'python'
autoapi_dirs = ['../../../frontend']

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
