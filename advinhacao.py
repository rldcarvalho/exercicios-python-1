import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    pontuacao = 1000


    def selecionar_nivel():
        tab_dificuldade = [1, 2, 3]
        tab_tentativas = [20, 10, 5]
        print("Qual o nível de dificuldade?")
        print("(1) Fácil (2) Médio (3) Difícil")
        nivel = int(input("Defina o nível: "))
        if nivel < 1 or nivel > 3:
            print("Número inválido")
            nivel = int(input("Defina o nível com um número de 1 a 3! "))
        tentativas = tab_dificuldade.index(nivel)
        return tab_tentativas[tentativas]


    total_de_tentativas = selecionar_nivel()


    for rodada in range(1, total_de_tentativas + 1):
        print(f'Tentativa {rodada} de {total_de_tentativas}')
        chute_str = input("Digite um número entre 1 e 100: ")

        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if not acertou:
            pontos_perdidos = abs(numero_secreto - chute)
            pontuacao = pontuacao - pontos_perdidos
            if maior:
                print("Você errou! O seu chute foi maior que o número secreto")
            elif menor:
                print("Você errou! O seu chute foi menor que o número secreto")
        else:
            print("Você acertou!")
            rodada = total_de_tentativas + 1
            print(f'Sua pontuação foi de {pontuacao}.')
            break

    print("Fim do jogo")

if __name__ == '__main__':
    jogar()