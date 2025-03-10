import textwrap
from datetime import date


class Banco:
    def __init__(self):
        self.usuarios = []
        self.contas = []
        self.numero_conta = 0
        self.saldo = 0
        self.extrato = {"depositos": [], "saques": []}
        self.saques_diarios = {"data:": date.today(), "contador": 0}

    def validar_usuario_cpf(self, cpf):
        next((usuario for usuario in self.usuarios if usuario.cpf == cpf), None)

    def criar_usuario(self):
        cpf = input("Digite o CPF do usuário: ")
        usuario = self.validar_usuario_cpf(cpf)

        if usuario:
            print("Usuário já cadastrado")
        return

        nome = input("Digite o nome do usuário: ")
        data_nascimento = input("Digite a data de nascimento do usuário: ")
        email = input("Digite o email do usuário: ")
        endereco = input("Digite o endereço do usuário (Logradouro, nº - Bairro - Cidade/Sigla do Estado): ")

        self.usuarios.append({
            "cpf": cpf,
            "nome": nome,
            "data_nascimento": data_nascimento,
            "email": email,
            "endereco": endereco
        })
        print("Usuário cadastrado com sucesso")

    def exibir_menu(self):
        menu = """
        1. Depositar
        2. Sacar
        3. Exibir extrato
        4. Criar usuário
        5. Criar conta
        6. Sair
        
        Escolha uma opção: """

        return input(textwrap.dedent(menu))

    def depositar(self):

        valor_deposito = int(input("Qual é o valor do depósito?: "))
        if valor_deposito < 0:
            print("Valor inválido\n")
        else:
            self.saldo +=valor_deposito
            self.extrato["depositos"].append(valor_deposito)
            print("Depósito efetuado com sucesso\n")

    def sacar(self):
        if self.saques_diarios["data"] != date.today():
            self.saques_diarios = {"data": date.today(), "contador": 0}

        if self.saques_diarios["contador"] >= 3:
            print("Limite de saques diários atingido\n")
            return

        valor_saque = int(input("Qual é o valor do saque?: "))
        if valor_saque <= self.saldo:
            self.saldo -= valor_saque
            self.extrato["saques"].append(valor_saque)
        else:
            print("Saldo insuficiente\n")

    def exibir_extrato(self):

        print("Extrato".center(25, "="))
        print("Depósito".center(25, "="))
        for i, valor in enumerate(self.extrato["depositos"]):
            print(f"{i + 1}. R$ {valor:.2f}")
        print("Saques".center(25, "="))
        for i, valor in enumerate(self.extrato["saques"]):
            print(f"{i + 1}. R$ {valor:.2f}")
        print("Saldo".center(25, "="))
        print(f"R$ {self.saldo:.2f}")
        print("\n")

    def main(self):

        while True:

            opcao = exibir_menu()
            if opcao == "1":
                saldo = depositar(saldo, extrato)
            elif opcao == "2":
                saldo = sacar(saldo, extrato)
            elif opcao == "3":
                exibir_extrato(saldo, extrato)
            elif opcao == "4":
                break
            else:
                print("Opção inválida")

    main()