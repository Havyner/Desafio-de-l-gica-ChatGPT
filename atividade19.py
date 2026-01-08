# Verifique se um número esta presente na lista

lista = [3, 1, 5, 2, 6, 7, 55, 21, 12, 45, 23, 33, 56, 90]

n = int(input('Informe o número que gostaria de verificar se esta na lista: '))

if n in lista:
    print(f"O número {n} esta na lista!")
else:
    print(f"O número {n} não esta na lista!")

