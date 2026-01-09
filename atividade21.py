# Simule um caixa eletrônico com opções de saque

def caixa_eletronico():

    saldo = 10000

    print("Bem-vindo ao Banco de Gothan")
    print(f"Seu saldo atual é: {saldo}")

    while True:

        print("\nEscolha uma Opção de saque:")
        print("1 - R$ 20,00")
        print("2 - R$ 50,00")
        print("3 - R$ 100,00")
        print("4 - R$ 200,00")
        print("5 - Outro valor")
        print("0 - Sair")

        op = input("Informe a opção desejada: ")

        if op == "0":
            print("Obrigado por usar o Banco de Gothan")
            break

        elif op in ["1", "2", "3", "4"]:
            valores = {"1": 20, "2": 50, "3": 100, "4": 200}
            saque = valores[op]
        
        elif op == "5":
            saque = int(input("Digite o valor desejado (múltiplo de 10): "))
            if saque % 10 != 0:
                print("O valor deve ser múltiplo de 10!")
                continue
        
        else:
            print("Opção inválida, tente novamente!")
            continue

        if saque > saldo:
            print("Saldo insuficiente!")

        else:
            saldo -= saque
            print(f"Saque de R$ {saque} realizado com sucesso!")
            print(f"Saldo restante: R$ {saldo}")

caixa_eletronico()