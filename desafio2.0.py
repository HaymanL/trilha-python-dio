import textwrap


def menu():
    menu = """
    MENU 
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [cc] Criar conta
    [lc] Listar contas
    [nu] Novo usuário
    [ss] Sair
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, vlr, ext, /):
    if vlr > 0:
        saldo += vlr
        ext += f"Depósito R$ {vlr:.2f}"
        print("Depósito realizado com êxito!")
    else:
        print("Operação invalida! Revise o processo !")

    return saldo, ext


def sacar(*, saldo, vlr, extrato, lim, numero_saques, limite_saques):
    excedeu_saldo = vlr > saldo
    excedeu_limite = vlr > lim
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Erro devido saldo suficiente.")
    elif excedeu_limite:
        print("Erro o valor do saque excede o seu limite.")
    elif excedeu_saques:
        print("Erro atingido o número máximo de saques.")
    elif vlr > 0:
        saldo -= vlr
        extrato += f"Saque: R$ {vlr:.2f}"
        numero_saques += 1
        print("Saque realizado com êxito!")
    else:
        print("Erro valor informado é inválido.")
    return saldo, extrato


def exibir_extrato(saldo,extrato):
    print(f"Saldo: R$ {saldo:.2f}")


def criar_usuario(usuarios):
    cpf = input("Digite o seu cpf : ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Erro cpf já cadastrado e vinculado ")
        return

    nome = input("Digite o seu nome completo: ")
    data_nascimento = input("Digite a data de nascimento: ")
    endereco = input("Digite o  seu endereço : ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário cadastrado com êxito")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o seu CPF do cadastro ")

    if cpf:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": cpf}

    print("Não localizado")


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "6666"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "cc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "ss":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
