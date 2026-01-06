# Leia dois números e mostre o maior

numero1 = int(input('Informe o primeiro número: '))
numero2 = int(input('Informe o segundo número: '))

if numero1 == numero2:
    print("Números iguais!")
elif numero1 > numero2:
    print(f"O número {numero1} é maior que {numero2}")
else:
    print(f"O número {numero2} é maior que {numero1}")