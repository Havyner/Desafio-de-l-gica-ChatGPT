# Leia a média e informe: aprovado, recuperação ou aprovado.

media = float(input('Informe a média: '))

if media >= 7:
    print("Aprovado!")
elif media < 5:
    print("Reprovado!")
else:
    print("Recuperação!")