# Sistema Bancário em Python
Este é um sistema bancário simples desenvolvido em Python. Ele permite a criação de usuários e contas bancárias, além de possibilitar depósitos, saques e a exibição de extratos bancários.

## Funcionalidades
O sistema oferece as seguintes funcionalidades:

* Criação de usuários: Cada usuário é identificado por um CPF único.
* Criação de contas bancárias: Cada conta é vinculada a um usuário já cadastrado e possui um número de conta exclusivo.
* Depósitos: Permite adicionar saldo à conta bancária.
* Saques: Permite realizar retiradas dentro do limite estabelecido de até 3 saques diários.
* Exibição de extrato: Apresenta o saldo atual e o histórico de transações da conta.

## Como Executar
Para rodar o sistema, siga os passos abaixo:

1. Certifique-se de ter o Python (versão 3.x) instalado. 
2. Baixe ou clone este repositório. 
3. No terminal, navegue até o diretório do projeto. 
4. Execute o arquivo principal com o comando:

```bash
python nome_do_arquivo.py
```  
5. Siga as instruções exibidas no terminal.

## Estrutura do Código
O código está estruturado na classe Banco, que contém os seguintes métodos principais:

* A partir da entrada do usuário:
    - Criar um usuário. 
    - Criar uma conta bancária. 
    - Realizar depósitos. 
    - Efetuar saques (limitados a 3 por dia). 
    - Exibir extrato bancário. 
    - ``main()``: Controla o fluxo principal do programa, mantendo-o em execução contínua.
