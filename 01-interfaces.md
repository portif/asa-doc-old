(rede)=

Configuração do ambiente de Rede
===================================

Objetivos de aprendizagem
-------------------------

* Configurar o nome de uma máquina Linux com Debian/Ubuntu
* Configurar interfaces de rede com endereço IP estático no Linux com Debian/Ubuntu
* Configurar interfaces de rede para obtenção de endereço IP dinâmico no Linux com Debian/Ubuntu
* Listar, ativar e desativar interfaces de rede no Linux com Debian/Ubuntu

Nome da máquina
-----------------

* Arquivo {file}`/etc/hostname`
* Arquivo {file}`/etc/hosts`
* Comando {command}`hostname`
* Comando {command}`hostnamectl`

```{literalinclude} host/amazonas/etc/hostname
:linenos:
```


```{literalinclude} host/amazonas/etc/hosts
:linenos:
```

Interfaces de rede
--------------------

* Arquivo: {file}`/etc/network/interfaces`
* Comando: {command}`ip link`
* Comando: {command}`ip addr`
* Comando: {command}`ifup <interface>`
* Comando: {command}`ifdown <interface>`

```{literalinclude} host/amazonas/etc/network/interfaces
:linenos:
```