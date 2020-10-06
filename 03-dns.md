# Sistema de Nomes de Domínio (DNS)

## Objetivos de aprendizagem

- Compreender os principais tipos e funcionalidade dos RRs (Registros de Recurso) do DNS
- Efetuar consultas a registros de recurso
- Cadastrar RRs em um servidor DNS
- Configurar um servidor Samba4 com controlador de domínio do ActiveDirectory
- Gerenciar servidor DNS do Samba4 por meio do RSAT (Ferramentas de Administração de Servidor Remoto) de um clnte Windows Desktop
- Criação de zonas diretas e inversas
- Criação de exemplos de registros de recurso A, CNAME, MX e PTR em zonas

## Arquivos, diretórios e comandos

- /etc/network/interfaces (ver *dns-nameservers*)
- /etc/resolv.conf
- nslookup

    - set type=RR
    - consulta
    - PS: RR podendo ser A, CNAME, MX, PTR etc. *consulta* é o que se pretende consultar

- dig
