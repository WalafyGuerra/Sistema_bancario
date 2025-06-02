menu = """

[1] = Depositar
[2] = Sacar
[3] = Extrato
[0] = Sair

=> """

Saldo = 3000
Limite = 3000
Extrato = ""
LIMITE_DE_SAQUES_POR_DIA = 3
numero_saques = 0

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Digite o valor do seu deposito: "))

        if valor > 0:
            Saldo += valor
            Extrato += f"Deposito: R$ {valor:.2f}\n"
            print(f"Depsosito de R$ {valor:.2f} realizado com sucesso!")

        else:
            print("Operacao invalida! O valor do deposito deve ser positivo.")

    elif opcao == "2":
        valor = float(input("Digite o valor que do seu saque: "))

        if valor <= 0:
            print("Operacao invalida! O valor do saque deve ser positivo.")
        else:
            excedeu_saldo = valor > Saldo
            excedeu_limite = valor > Limite
            excedeu_saque = numero_saques >= LIMITE_DE_SAQUES_POR_DIA

            if excedeu_saldo:
                print("Saque nao autorizado. Saldo insuficciente!")
            elif excedeu_limite:
                print("Saque nao autorizado. Limite atingido!")
            elif excedeu_saque:
                print("Limite de saques excedido!")
            else:
                Saldo -= valor
                Extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    elif opcao == "3":
        print("\n===================== EXTRATO ======================")

        if not Extrato:
            print("Nao foram realizadas movimentacoes.")
        else:
            print(Extrato)

        print(f"\nSaldo: R$ {Saldo:.2f}")
        print("======================================================")

    elif opcao == "0":
        print("Obrigado por utlizar o Banco XYZ!")
        break

    else:
     print("Opcao invalida. Retorne o menu principal.")





