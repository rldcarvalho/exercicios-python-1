import forca
import advinhacao

print("*********************************")
print("*******Escolha o seu Jogo********")
print("*********************************")

print("(1) Forca (2) Adivinhacao")

jogo = int(input("Qual o seu jogo? "))

if jogo == 1:
    print('Jogando forca')
    forca.jogar()
elif jogo == 2:
    print('Jogando Adivinhação')
    advinhacao.jogar()

