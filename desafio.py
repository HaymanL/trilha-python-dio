menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

= >> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Opção selecionada >> Depósito")
        dep = float(input("Informe o valor do depósito: "))
        if dep > 0:
                saldo += dep
                extrato += f"Depósito: R$ {dep:.2f}\n"

        else:
            print("Valor informado inválido, tente novamente!.")


    elif opcao == "s":
        print("Opção selecionada >> Saque")
        saq = float(input("Informe o valor do saque: "))

        excedeu_saldo = saq > saldo

        excedeu_limite = saq > limite

        excedeu_saques = numero_saque >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif saq > 0:
            saldo -= saq
            extrato += f"Saque: R$ {saq:.2f}\n"
            numero_saque += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    
    elif opcao == "e":
        print("Opção selecionada >> Extrato")
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        print("Obrigado, volte sempre!!")
        break

    else:
        print("Opção inválida, por favor selecione novamente a operação desejada!.")