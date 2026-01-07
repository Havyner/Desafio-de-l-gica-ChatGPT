# Leia cinco números e calcule a soma

soma = 0

for i in range(5):
    numero = int(input(f'Digite o {i+1}º número: '))
    soma += numero

print(f"A soma dos números é: {soma}")