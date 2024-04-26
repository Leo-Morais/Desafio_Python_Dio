menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:
        valor_depositado = float(input("Digite o valor que deseja depositar: "))
        saldo += valor_depositado
        extrato += f"Valor de R$ {valor_depositado} foi depositado\n"

        print("Deposito realizado com sucesso")
    
    elif opcao == 2:

        valor_de_saque = float(input("Digite o valor que deseja sacar: "))

        if valor_de_saque <= 500 and valor_de_saque <= saldo and numero_saques < 3:
            saldo -= valor_de_saque
            numero_saques += 1
            extrato += f"Saque de R$ {valor_de_saque} realizado.\n"
            print("Saque realizado com sucesso!")

        elif valor_de_saque > 500:
            print("Saque maior que o limite de R$500.")

        elif numero_saques == 3:
            print("Limite de saque diário atingido.")

        else:
            print("Valor de saque maior que valor do saldo.")
    
    elif opcao == 3:
        if extrato != "":
            print(extrato)
            print(f"saldo total de: R${saldo:.2f}")
        else:
            print("Não foram realizadas movimentações")
    
    elif opcao == 0:
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")