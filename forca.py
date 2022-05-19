def jogar():
    import random

    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

    #arquivo = open("palavras.txt", "r") - modo alternativo para abertura de arquivo
    palavras = []
    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    #arquivo.close() - modo alternativo para fechamento do aquivo
    #O modo implementado para abertura do arquivi permite q o python feche o mesmo automaticamente em caso de erro

    palavra_secreta = random.choice(palavras).upper()
    letras_acertadas = ["_"] * len(palavra_secreta)
    #alternativamente: letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual a letra? ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print(f"Ops, você errou! Faltam {6-erros} tentativas.")

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print("Você ganhou!")
    else:
        print("Você perdeu")

    print("Fim do jogo")

if __name__ == '__main__':
    jogar()