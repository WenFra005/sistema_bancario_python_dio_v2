""""Programa que simula um sistema bancário com funcionalidades de criação de usuários e contas,
depósitos, saques e exibição de extratos."""

import textwrap
from datetime import date

class Banco:
    """Classe que representa um banco com funcionalidades de criação de usuários e contas,
    depósitos, saques e exibição de extratos."""

    def __init__(self):
        """Inicializa a classe Banco com listas de usuários, contas e um contador de
        número de conta."""
        self.usuarios = []
        self.contas = []
        self.numero_conta = 0

    def validar_usuario_conta_cpf(self, cpf):
        """Valida se um usuário com o CPF fornecido já está cadastrado.

        Args:
            cpf (str): CPF do usuário.

        Returns:
            dict: usuário correspondente ao CPF, se encontrado. Caso contrário, None.
        """
        return next((usuario for usuario in self.usuarios if usuario["cpf"] == cpf), None)

    def criar_usuario(self):
        """Cria um usuário com os dados fornecidos pelo input."""
        cpf = input("Digite o CPF do usuário: ")
        usuario = self.validar_usuario_conta_cpf(cpf)

        if usuario:
            print("Usuário já cadastrado")
            return

        nome = input("Digite o nome do usuário: ")
        data_nascimento = input("Digite a data de nascimento do usuário: ")
        email = input("Digite o email do usuário: ")
        endereco = input(
            "Digite o endereço do usuário (Logradouro, nº - Bairro - Cidade/Sigla do Estado): "
        )

        self.usuarios.append({
            "cpf": cpf,
            "nome": nome,
            "data_nascimento": data_nascimento,
            "email": email,
            "endereco": endereco
        })
        print("Usuário cadastrado com sucesso")

    def criar_conta(self):
        """Cria uma nova conta para um usuário existente com o CPF fornecido pelo input."""
        cpf = input("Digite o CPF do usuário: ")
        usuario = self.validar_usuario_conta_cpf(cpf)

        if not usuario:
            print("Usuário não cadastrado")
            return

        self.numero_conta += 1
        conta = {
            "agencia": "0001",
            "numero_conta": self.numero_conta,
            "usuario": usuario,
            "saldo": 0,
            "extrato": {"depositos": [], "saques": []},
            "saques_diarios": {"data": date.today(), "contador": 0}
        }

        self.contas.append(conta)
        print("Conta criada com sucesso!")
        print("Dados da conta".center(25, "="))
        print(f"Agência: {conta['agencia']}")
        print(f"Número da conta: {conta['numero_conta']}\n")

    @staticmethod
    def exibir_menu():
        """Exibe o menu de opções e retorna a escolha do usuário.

        Returns:
            str: opção escolhida pelo usuário.
        """
        menu = """
        1. Depositar
        2. Sacar
        3. Exibir extrato
        4. Criar usuário
        5. Criar conta
        6. Sair
        
        Escolha uma opção: """
        return input(textwrap.dedent(menu))

    def obter_conta(self, numero_conta):
        """Obtém uma conta pelo número da conta.

        Args:
            numero_conta (int): Número da conta.

        Returns:
            dict: conta correspondente ao número, se encontrada. Caso contrário, None.
        """
        return next((conta for conta in self.contas if conta["numero_conta"] == numero_conta), None)

    def depositar(self):
        """Realiza um depósito numa conta existente."""
        numero_conta = int(input("Digite o número da conta: "))
        conta = self.obter_conta(numero_conta)
        if not conta:
            print("Conta não encontrada\n")
            return

        valor_deposito = int(input("Qual é o valor do depósito?: "))
        if valor_deposito <= 0:
            print("Valor inválido\n")
        else:
            conta["saldo"] +=valor_deposito
            conta["extrato"]["depositos"].append(valor_deposito)
            print("Depósito efetuado com sucesso\n")

    def sacar(self):
        """Realiza o saque numa conta existente, respeitando o limite de 3 saques diários."""
        numero_conta = int(input("Digite o número da conta: "))
        conta = self.obter_conta(numero_conta)
        if not conta:
            print("Conta não encontrada\n")
            return

        if conta["saques_diarios"]["data"] != date.today():
            conta["saques_diarios"] = {"data": date.today(), "contador": 0}

        if conta["saques_diarios"]["contador"] >= 3:
            print("Limite de saques diários atingido\n")
            return

        valor_saque = int(input("Qual é o valor do saque?: "))
        if valor_saque <= conta["saldo"]:
            conta["saldo"] -= valor_saque
            conta["extrato"]["saques"].append(valor_saque)
            conta["saques_diarios"]["contador"] += 1
            print("Saque efetuado com sucesso\n")
        elif valor_saque > conta["saldo"]:
            print("Saldo insuficiente\n")
        elif valor_saque == 0:
            print("Valor inválido\n")
        else:
            print("Inválido\n")

    def exibir_extrato(self):
        """Exibe o extrato de uma conta existente, incluindo dados do usuário e transações."""
        numero_conta = int(input("Digite o número da conta: "))
        conta = self.obter_conta(numero_conta)
        if not conta:
            print("Conta não encontrada\n")
            return

        print("Extrato".center(25, "="))
        print("Dados Pessoais".center(25, "="))
        print(f"Nome: {conta['usuario']['nome']}")
        print(f"CPF: {conta['usuario']['cpf']}")
        print(f"Agência: {conta['agencia']}")
        print(f"Número da conta: {conta['numero_conta']}")
        print("Depósitos".center(25, "="))
        for i, valor in enumerate(conta["extrato"]["depositos"]):
            print(f"{i + 1}. R$ {valor:.2f}")
        print("Saques".center(25, "="))
        for i, valor in enumerate(conta["extrato"]["saques"]):
            print(f"{i + 1}. R$ {valor:.2f}")
        print("Saldo".center(25, "="))
        print(f"R$ {conta["saldo"]:.2f}")
        print("\n")

    def main(self):
        """Método principal que exibe o menu de opções e executa as funcionalidades escolhidas
        pelo usuário."""
        while True:

            opcao = self.exibir_menu()
            if opcao == "1":
                self.depositar()
            elif opcao == "2":
                self.sacar()
            elif opcao == "3":
                self.exibir_extrato()
            elif opcao == "4":
                self.criar_usuario()
            elif opcao == "5":
                self.criar_conta()
            elif opcao == "6":
                break
            else:
                print("Opção inválida")

if __name__ == "__main__":
    banco = Banco()
    banco.main()
