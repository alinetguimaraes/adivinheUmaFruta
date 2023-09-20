#
# Autora: Aline Torres Guimarães
# Jogo: Adivinhe uma fruta
# 

import random


print("----- Adivinhe a fruta <3 -----")

nome = input("Qual o seu nome? ")

print("Olá, " + nome + "! Boa sorte!")
print("Você tem 5 chances")

frutas = ["maçã", "uva", "melancia", "melão", "limão", "laranja", "banana", "abacaxi", "cajá", "kiwi", "manga", "morango", "amora", "pera", "carambola", "ameixa", "abacate"] 


def jogo():
    fruta_secreta = random.choice (frutas)
    palpite = 0
    chance = 1
    

    while palpite != fruta_secreta:
        palpite=input("Digite o nome de uma fruta: ")
        palpite.lower()
        if (palpite == fruta_secreta):
            print("Parabéns, você acertou! <3")
        else:
            print("Ah, não! Tente novamente. :(")
            print("Tentativa nº " + str(chance))
            chance = chance + 1
            if chance > 5:
                print("Você perdeu :( Tente outra vez!")
                print("A fruta secreta era: " + fruta_secreta + " <3")
                break
jogo()
