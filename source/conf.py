# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Repetition is the mother of memory'
copyright = '2025, chenxdszu'
author = 'chenxdszu'
release = '1.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
extensions = [
    # 已有的扩展...
    'nbsphinx',
    'sphinx_gallery.load_style',
    'IPython.sphinxext.ipython_console_highlighting',
]
# 设置主题为 readthedocs 风格
html_theme = 'sphinx_rtd_theme'
# 配置 Jupyter 笔记本相关设置
nbsphinx_execute = 'auto'  # 自动执行笔记本
nbsphinx_allow_errors = True  # 允许执行错误
