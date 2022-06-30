Serviços de autenticação
========================

Objetivos de aprendizagem
-------------------------

* Instalar servidor Samba4
* Configurar controlador de domínio do Active Directory no Samba4
* Gerenciar usuários no Samba4
* Ingressar estações Windows e Linux no domínio do Samba4
* Gerenciar usuários, grupos e unidades organizacionais

Arquivos, diretórios e comandos
--------------------------------

* systemctl status samba-ad-dc
* samba-tool
* samba-tool user
* samba-tool group
* samba-tool dns
* /etc/samba/smb.conf
* /etc/krb5.conf
* /var/log/samba/

## No Windows

* No CMD: `dsquery * "DC=ifrn,DC=local" -filter "(samaccountname=%USERNAME%)" -attr *`
* No PowerShell: `Get-ADUser $Env:USERNAME -Properties *`

Referências sugeridas
---------------------

- [Create an Active Directory Infrastructure with Samba4 on Ubuntu -- Part 1](https://www.tecmint.com/install-samba4-active-directory-ubuntu/)
- [How to Manage Samba4 AD Infrastructure from Linux Command Line -- Part 2](https://www.tecmint.com/manage-samba4-active-directory-linux-command-line/)
- [Manage Samba4 Active Directory Infrastructure from Windows10 via RSAT -- Part 3](https://www.tecmint.com/manage-samba4-dns-group-policy-from-windows/)
- [Integrate Ubuntu to Samba4 AD DC with SSSD and Realm -- Part 15](https://www.tecmint.com/integrate-ubuntu-to-samba4-ad-dc-with-sssd-and-realm/)

