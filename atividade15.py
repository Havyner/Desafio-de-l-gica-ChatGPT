# Peça números até o usuário digitar um valor prositivo

while True:
    numero = int(input('Informe um número: '))

    if numero % 2 == 0:
        print(f"Você digitou uma número positivo: {numero}")
        break
    else:
        print(f"O número {numero} não é positivo, tente novamente!")