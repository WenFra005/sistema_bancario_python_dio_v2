import textwrap
from datetime import date

class Banco:
    def __init__(self):
        self.usuarios = []
        self.contas = []
        self.numero_conta = 0
        self.saques_diarios = {"data": date.today(), "contador": 0}

    def validar_usuario_conta_cpf(self, cpf):
        return next((usuario for usuario in self.usuarios if usuario["cpf"] == cpf), None)

    def criar_usuario(self):
        cpf = input("Digite o CPF do usuário: ")
        usuario = self.validar_usuario_conta_cpf(cpf)

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

    def criar_conta(self):
        cpf = input("Digite o CPF do usuário: ")
        usuario = self.validar_usuario_conta_cpf(cpf)

        if not usuario:
            print("Usuário não cadastrado")
            return

        conta = {
            "agencia": "0001",
            "numero_conta": self.numero_conta,
            "usuario": usuario,
            "saldo": 0,
            "extrato": {"depositos": [], "saques": []}

        }

        self.contas.append(conta)
        self.numero_conta += 1
        print("Conta criada com sucesso!")
        print("Dados da conta".center(25, "="))
        print(f"Agência: {conta['agencia']}")
        print(f"Número da conta: {conta['numero_conta']}\n")

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

    def obter_conta(self, numero_conta):
        return next((conta for conta in self.contas if conta["numero_conta"] == numero_conta), None)

    def depositar(self):
        numero_conta = int(input("Digite o número da conta: "))
        conta = self.obter_conta(numero_conta)
        if not conta:
            print("Conta não encontrada\n")
            return

        valor_deposito = int(input("Qual é o valor do depósito?: "))
        if valor_deposito < 0:
            print("Valor inválido\n")
        else:
            conta["saldo"] +=valor_deposito
            conta["extrato"]["depositos"].append(valor_deposito)
            print("Depósito efetuado com sucesso\n")

    def sacar(self):
        numero_conta = int(input("Digite o número da conta: "))
        conta = self.obter_conta(numero_conta)
        if not conta:
            print("Conta não encontrada\n")
            return

        if self.saques_diarios["data"] != date.today():
            self.saques_diarios = {"data": date.today(), "contador": 0}

        if self.saques_diarios["contador"] >= 3:
            print("Limite de saques diários atingido\n")
            return

        valor_saque = int(input("Qual é o valor do saque?: "))
        if valor_saque <= conta["saldo"]:
            conta["saldo"] -= valor_saque
            conta["extrato"]["saques"].append(valor_saque)
            self.saques_diarios["contador"] += 1
            print("Saque efetuado com sucesso\n")
        else:
            print("Saldo insuficiente\n")

    def exibir_extrato(self):
        numero_conta = int(input("Digite o número da conta: "))
        conta = self.obter_conta(numero_conta)
        if not conta:
            print("Conta não encontrada\n")
            return

        print("Extrato".center(25, "="))
        print("Depósito".center(25, "="))
        for i, valor in enumerate(conta["extrato"]["depositos"]):
            print(f"{i + 1}. R$ {valor:.2f}")
        print("Saques".center(25, "="))
        for i, valor in enumerate(conta["extrato"]["saques"]):
            print(f"{i + 1}. R$ {valor:.2f}")
        print("Saldo".center(25, "="))
        print(f"R$ {conta["saldo"]:.2f}")
        print("\n")

    def main(self):

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