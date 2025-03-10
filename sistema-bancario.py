import textwrap


def exibir_menu():
    menu = """
    1. Depositar
    2. Sacar
    3. Exibir extrato
    4. Criar usuário
    5. Criar conta
    6. Sair
    
    Escolha uma opção: """
    return input(textwrap.dedent(menu))

def depositar(saldo, extrato):

    valor_deposito = int(input("Qual é o valor do depósito?: "))
    if valor_deposito < 0:
        print("Valor inválido\n")
        return saldo
    else:
        saldo = saldo + valor_deposito
        extrato["depositos"].append(valor_deposito)
        print("Depósito efetuado com sucesso\n")
        return saldo

def sacar(saldo, extrato):

    valor_saque = int(input("Qual é o valor do saque?: "))
    if valor_saque <= saldo:
        saldo = saldo - valor_saque
        extrato["saques"].append(valor_saque)
    else:
        print("Saldo insuficiente\n")
    return saldo

def exibir_titulos_extrato():
    t_extrato = "Extrato"
    t_depositos = "Depósito"
    t_saques = "Saques"
    t_Saldo = "Saldo"

    return t_extrato, t_depositos, t_saques, t_Saldo

def exibir_extrato(saldo, extrato):

    print(exibir_titulos_extrato()[0].center(25, "="))
    print(exibir_titulos_extrato()[1].center(25, "="))
    for i, valor in enumerate(extrato["depositos"]):
        print(f"{i + 1}. R$ {valor:.2f}")
    print(exibir_titulos_extrato()[2].center(25, "="))
    for i, valor in enumerate(extrato["saques"]):
        print(f"{i + 1}. R$ {valor:.2f}")
    print(exibir_titulos_extrato()[3].center(25, "="))
    print(f"R$ {saldo:.2f}")
    print("\n")


def main():

    saldo = 0
    extrato = {
        "depositos": [],
        "saques": []
    }
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