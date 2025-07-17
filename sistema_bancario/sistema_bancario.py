from time import sleep
from datetime import datetime

menu = """

Bem-vindo ao Sistema Bancário!

Escolha uma das opções abaixo:
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
ultimo_reset = datetime.now().date()

while True:
    data_atual = datetime.now().date()
    if data_atual != ultimo_reset:
        numero_saques = 0
        ultimo_reset = data_atual

    opcao = input(menu)

    if opcao == "d":
        print("\nOpção selecionada: Depósito")
        print(f"Saldo atual: R$ {saldo:.2f}")
        valor = float(input("Informe o valor de depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!\n"
            f"Saldo atual: R$ {saldo:.2f}")
        else:
            print("Erro: O valor do depósito deve ser positivo.")
        sleep(2)

    elif opcao == "s":
        print("\nOpção selecionada: Saque")
        print(f"Saldo atual: R$ {saldo:.2f}")

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saques:
            print("Erro: Número de saques diários excedido.")
        else:
            valor = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite

            if excedeu_saldo:
                print(f"Erro: Saldo insuficiente. Seu saldo é de R$ {saldo:.2f}.")
            
            elif excedeu_limite:
                print(f"Erro: Valor excede o limite de saque de R$ {limite:.2f}.")

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print("Saque realizado com sucesso!\n"
                    f"Saldo atual: R$ {saldo:.2f}")

            else:
                print("Erro: Valor inválido para saque.")
        sleep(2)

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("=========================================")
        sleep(2)

    elif opcao == "q":
        print("\nSaindo do sistema bancário... Obrigado por usar nossos serviços!")
        break

    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.")
        sleep(2)
