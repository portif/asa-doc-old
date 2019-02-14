from recommonmark.parser import CommonMarkParser
templates_path = ['_templates']
source_suffix = ['.rst', '.md']
source_parsers = {'.md': CommonMarkParser}
master_doc = 'index'
project = 'Administração de Sistemas Abertos'
copyright = '2019, AUTOR'
author = 'AUTOR'
version = '2019.1'
release = '2019.1'
language = 'pt_BR'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = True
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
        }
html_static_path = ['_static']
html_sidebars = {
    '**': [
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
    ]
}
htmlhelp_basename = 'AdministracaoSistemasAbertosdoc'
latex_elements = {
}
latex_documents = [
    (master_doc, 'AdministracaoSistemasAbertos.tex', u'Administração de Sistemas Abertos Documentation',
     u'AUTOR', 'manual'),
]
man_pages = [
    (master_doc, 'AdministracaoSistemasabertos', u'Administração de Sistemas Abertos Documentation',
     [author], 1)
]
texinfo_documents = [
    (master_doc, 'AdministracaoSistemasAbertos', u'Administração de Sistemas Abertos Documentation',
     author, 'AdministracaoSistemasAbertos', 'One line description of project.',
     'Miscellaneous'),
]
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright
epub_exclude_files = ['search.html']
