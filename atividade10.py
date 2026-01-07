# Crie uma calculadora simples com +, -, * e /

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

print("Escolha uma opção: +  -  *  /")
op = input('Informe a opção desejada: ')

if op == "+":
    resultado = num1 + num2
    print(f"Resultado: {resultado}")
elif op == "-":
    resultado = num1 - num2
    print(f"Resultado: {resultado}")
elif op == "*":
    resultado = num1 * num2
    print(f"Resultado: {resultado}")
elif op == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado: {resultado}")
    else:
        print("Erro: Divisão por zero")
else:
    print("Opção inválida!!")

'''
print(f"Resultado: {resultado}")
'''