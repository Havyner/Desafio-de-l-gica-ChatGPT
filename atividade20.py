# leia notas até digitar -1 e calcule a média

listaNotas = []

while True:
    nota = float(input('Informe a nota ou -1 para sair: '))
    if nota == -1:
        media = sum(listaNotas) / len(listaNotas)
        break
    else:
        listaNotas.append(nota)
    
print(f"Média: {media:.2f}")