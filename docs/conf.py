# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Aide en ligne'

release = '0.1'
version = '0.1.0'

# -- General configuration

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'material'