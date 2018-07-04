.. _http:

Servidor Web (HTTP)
===================

Objetivos de aprendizagem
-------------------------

* Instalar um servidor Web (`lighttpd`, `apache2` ou `ngnix`)  no Linux 
* Editar configurações de um servidor Web
* Navegar nos diretórios de configuração do servidor Web
* Publicar páginas na raiz de documentos (`DocumentRoot`)
* Analisar registros de acesso e de erro de um servidor Web
* Gerenciar o serviço (:ref:`serviço`)
* Habilitar e desabiliar configuração (conf), módulo (mod) e site no Apache2
* Subir um servidor HTTPS (módulo ``ssl`` e site ``default-ssl``)
* Criação de um certificado autoassinado com ``openssl``
* Instalar um servidor LAMP
* Implantar uma aplicação LAMP (Ex.: Moodle)
* Configurar servidor Web multihost
* Registar nome do servidor Web no servidor DNS (:ref:`dns`)

Arquivos, diretórios e comandos
--------------------------------

* /etc/apache2/
* /etc/apache2/mods-available
* /etc/apache2/sites-enabled
* /etc/apache2/sites-available
* /etc/apache2/conf-available
* /etc/apache2/conf-enabled
* /etc/apache2/mods-enabled
* a2disconf
* a2dismod
* a2dissite
* a2enconf
* a2enmod
* a2ensite
* a2query
* tail -f /var/log/apache2/access.log
* tail -f /var/log/apache2/access.log | ccze -A
* tail -f /var/log/apache2/error.log

Referências sugeridas
---------------------

* `10 melhores sites para criar um Favicon <http://www.des1gnon.com/2017/10/criar-um-favicon/>`_
