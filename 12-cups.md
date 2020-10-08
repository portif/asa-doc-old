# Servidor de impressão

## Objetivos de aprendizagem

- Habilitar servidor de impressão para escutar em todas as interfaces
- Compartilhar impressoras via protocolos IPP e SMB
- Acessar interface Web do servidor de impressão
- Listar fila de impressão

## Arquivos, diretórios e comandos

- /etc/cups/
- /etc/cups/cupsd.conf
- /etc/cups/printers.conf
- /var/spool/cups/
- lp
- lpq
- lprm
- lpstat
- cancel
- system-config-printer
- /var/log/cups/
- /var/log/cups/access.log

## API

- Testar [pycups](https://pypi.org/project/pycups/)

```python
>>> import cups                                                             
>>> conexao = cups.Connection()                                             
>>> impressoras = conexao.getPrinters()                                     
>>> for impressora in impressoras: 
...:    print(impressora, impressoras[impressora]['device-uri']) 
...:                                                                         
HP-LaserJet-M1536dnf-MFP hp:/usb/HP_LaserJet_M1536dnf_MFP?serial=00BRCFD4C9C2
HP-LaserJet-M1536dnf-MFP-Fax-2 hpfax:/usb/HP_LaserJet_M1536dnf_MFP?serial=00BRCFD4C9C2
PDF cups-pdf:/
```
