# Atribuição dinâmica de endereços IP (DHCP)

## Objetivos de aprendizagem

- Definir o que é e para que serve o protocolo DHCP
- Configurar um intervalo de endereços IP a distribuir em uma rede
- Reservar endereços IP a partir do endereço MAC
- Analisar mensagens do servidor DHCP enviadas para o servidor de log

## Instalação

{command}`sudo apt install isc-dhcp-server`

## Arquivos de configuração
```{literalinclude} host/nilo/etc/default/isc-dhcp-server
:linenos:
```

```{literalinclude} host/nilo/etc/dhcp/dhcpd.conf
:linenos:
```

## Acompanhamento de logs

Explique qual o comando para acompanhar os logs do servidor DHCP.

## Registro das concessões

Arquivo {file}`/var/lib/dhcp/dhcpd.leases`

Inclua um arquivo de exemplo, preferencialmente exibindo o número das
linhas, e comente brevemente os atributos de uma concessão (Ex.: *starts*, 
*ends*, *hardware ethernet*)

## Reserva de endereço IP

Demostre como fazer reserva de endereço IP. Preferencialmente, inclua
arquivos de configuração, destacando as linhas de configuração da(s) reserva(s).

## Arquivos, diretórios e comandos

- /etc/default/isc-dhcp-server
- /etc/dhcp/dhcpd.conf
- /var/lib/dhcp/dhcpd.leases
- tail -f /var/log/syslog \| grep dhcpd \| ccze
