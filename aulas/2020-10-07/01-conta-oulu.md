# Criação de conta na Oulu

## Material necessário

- Android: [Termux](https://play.google.com/store/apps/details?id=com.termux&hl=pt_BR)
- iPhone: [Termius](https://apps.apple.com/br/app/termius-ssh-client/id549039908)
- Linux:  Terminal (No Ubuntu, <kbd>CTRL</kbd>+<kbd>ALT</kbd>+<kbd>T</kbd>)
- Windows: Instalar o [Git for Windows](https://git-scm.com/download/win)


## Roteiro

1. Abrir um terminal:
   - Android: Termux
   - iPhone: Termius
   - Linux: Terminal
   - Windows: Git Bash

2. Acessar a Oulu via SSH com a conta estudante:

   - `ssh estudante@oulu.ifrn.edu.br`

Se esta for a primeira vez que você acessa o servidor Oulu, será solicitado que você aceite a {term}`chave pública` do servidor. Digite <kbd>yes</kbd> para aceitá-la. Essa chave ficará salva no arquivo {ref}`known_ssh` e, como o próprio nome diz, será utilizada para reconhecimento do servidor nos próximos acessos.

A senha do usuário *estudante* é **estudante**. Observe que, ao digitar, a senha não aparece. Isto é uma característica da entrada da senha via terminal, pois evita que alguém próximo descubra quantos caracteres tem sua senha. Após digitar a senha, pressione a tecla <kbd>Enter</kbd>.

3. Solicitar a criação da conta

   - `sudo cria-meu-usuario`

Serão solicitados:

   1. A senha do usuário *estudante*;
   2. Sua matrícula no [SUAP](https://suap.ifrn.edu.br);
   3. Sua senha do SUAP.

Após a entrada correta dos dados acima, será 

Observe que será criada uma senha 

4. Seguir as instruções que aparecem na tela.
  




