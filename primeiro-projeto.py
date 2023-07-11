menu = """

[1] Sacar
[2] Depositar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "1":
        print("Opção escolhida: Saque\n")
        valor = float(input("informe o valor desejado para saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print(f"Saldo insuficiente! Seu saldo atual é R$ {saldo:.2f}")
        
        elif excedeu_limite:
            print("Seu saque excedeu o limite diário!")
        
        elif excedeu_saques:
            print("Número máximo de saques diários excedido!")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")
    
        #print(f"Você sacou R$ {valor:.2f}") --> pensar na implementação

    elif opcao == "2":
        print("Opção escolhida: Depósito\n")
        valor = float(input("informe o valor desejado para depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.\n")

        print(f"A sua quantia de R$ {valor:.2f} foi depositada com sucesso!")

    elif opcao == "3":
        print("Opção escolhida: Extrato\n")
        print("\n================EXTRATO================")
        print("Não houve movimentações!" if not extrato else extrato)
        print(f"\nSeu saldo atual é : {saldo:.2f}")
        print("=======================================")

    elif opcao == "0":
        print("Obrigado por escolher nosso banco!\n")
        break

    else:
        print("Operação inválida! Por favor, selecione uma opção válida.\n")