# Gere a tabuada de um número

numero = int(input('Informe um número: '))
print(f"Tabuada do número: {numero}")

for i in range(1, 11):
    print(f"{i} * {numero} = {i * numero}")