# Conte números pares e ímpares da lista.

lista = [3, 2, 6, 11, 17, 23, 34, 10, 21, 54, 63, 77]

par = 0
impar = 0

for i in lista:
    if i % 2 == 0:
        par += 1
    else:
        impar += 1

print(f"Pares: {par}")
print(f"Ímpares: {impar}")