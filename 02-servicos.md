(serviço)=

Administração de serviços de rede
=================================

Objetivos de aprendizagem
-------------------------

* Listar serviços disponíveis no sistema
* Iniciar um serviço
* Parar um serviço
* Reiniciar um serviço
* Recarregar os arquivos de configuração de um serviço
* Verificar o estado de um serviço
* Verificar se um serviço está ativo
* Habilitar um serviço
* Verificar se um serviço está habilitado
* Desabilitar um serviço
* Geração e análise de grafo de dependência entre serviços
* Geração e análise de gráfico de tempo de inicialização de cada serviço

Arquivos, diretórios e comandos
--------------------------------
* systemctl list-units
* systemctl <start|stop|restart|reload|status|is-active|enable|disable|is-enabled> <serviço>
* systemctl start <serviço>
* systemctl stop <serviço>
* systemctl restart <serviço>
* systemctl reload <serviço>
* systemctl status <serviço>
* systemctl is-active <serviço>
* systemctl enable <serviço>
* systemctl disable <serviço>
* systemctl is-enabled <serviço>
* systemd-analyze dot | dot -Tsvg > systemd.svg
* systemd-analyze plot > /tmp/systemd-grafico.svg

Referências sugeridas
---------------------

* [systemd (Português) - ArchWiki](https://wiki.archlinux.org/index.php/Systemd_(Portugu%C3%AAs))
* [systemd – Wikipédia, a enciclopédia livre](https://pt.wikipedia.org/wiki/Systemd)

