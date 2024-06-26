# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


project = 'RAICo1 Documentation'
copyright = '2024, Mohammad Hossein Bamorovat Abadi'
author = 'Mohammad Hossein Bamorovat Abadi'
release = '1.0.0'

extensions = ['sphinx.ext.todo', 'sphinx.ext.mathjax']

templates_path = ['_templates']
exclude_patterns = []


# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
# version = '1.0'

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ["_static"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'
highlight_language = 'console'


# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# Enable numref
numfig = True
