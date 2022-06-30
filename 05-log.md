(log)=

Servidor de Log (Syslog/Logrotate)
==================================

Objetivos de aprendizagem
-------------------------

* Definir o conceito de log
* Acompanhar os logs do sistema
* Compreender as facilidades e níveis de segurança do Syslog
* Configurar um servidor rsyslog para recebimento de mensagens de outras máquinas
* Configurar servidores rsyslog para enviar mensagem para um servidor central
* Configuração de um servidor de log integrado a um banco de dados relacional
* Rotação de registros

Arquivos, diretórios e comandos
--------------------------------

* /var/log/syslog
* /var/log/auth.log
* /etc/rsyslog.conf
* /etc/logrotate.conf
* /etc/logrotate.d/
* tail -f /var/log/syslog
* tail -f /var/log/syslog | ccze 
* colortail -f /var/log/syslog 
* journalctl -f
* journalctl -f | ccze
