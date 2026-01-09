# Jogo de adivinhação (0 à 10).

import random

def jogo_adivinha():

    numero_secreto = random.randint(0, 10) #sorteia o numero
    tentativas = 0

    print("Bem-vindo ao jogo de adivinhação do Batman")
    print("Tente adivinhar o número entre 0 e 10")

    while True:
        try:
            palpite = int(input("Digite seu palpite: "))

        except ValueError:
            print("Digite apenas números!")
            continue

        tentativas += 1

        if palpite < 0 or palpite > 10:
            print("O número deve estar entre 0 e 10!")

        if palpite == numero_secreto:
            print(f"ACERTOUUUU!\nVocê acertou em {tentativas} tentativas.")
            break
        elif palpite < numero_secreto:
            print("O número secreto é MAIOR!")
        else:
            print("O número secreto é MENOR!")

jogo_adivinha()