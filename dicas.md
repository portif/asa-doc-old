:orphan:

Dicas
=====

Geração de documentos
---------------------

O formato de documentação `Sphinx <http://www.sphinx-doc.org>`_ permite gerar a documentação em difentes formatos. Listamos abaixo os que devem ser mais úteis:

    * HTML: digite o comando {command}`make html`;
    * PDF: digite o comando {command}`make latexpdf`;
    * HTML página única: digite o comando {command}`make singlehtml`;
    * EPUB: digite o comando {command}`make epub`.

.. note::

    Tenha em mente que os comandos acima devem ser digitados no diretório onde se encontra o arquivo {file}`Makefile`. 

Linhas em branco e comentários
-------------------------------

Para não exibir as linhas em branco e comentários de em um arquivo, utilize o comando:

    * {command}`egrep -v (^$|^#) <arquivo>`

Para remover as linhas em branco e comentários de um arquivo, utilize um dos comando abaixo:

    * {command}`sed -e '/^$/d' -e '/^#/d' -i <arquivo>`
    * {command}`sed '/^$/d;/^#/d' -i <arquivo>`

Alterar o autor da documentação
-------------------------------

Edite o arquivo {file}`conf.py` e substitua todas as ocorrências de AUTOR por seu nome completo. Se preferir fazer isso via linha de comando, experimente o comando: 

    * {command}`sed -i 's/AUTOR/Fulano Pereira da Silva/' conf.py`
