import random

#Função
def jogar():

    print("\n*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    # É preciso importar a biblioteca random e chama-la novamente no comando
    numero_secreto = round(random.randrange(1,101))#cria um numero aleatoriamente e o round apenas arredonda

    total_de_tentativas = 0
    pontos = 1000

    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Defina o nível: "))#no input a variavel é sempre str e as vezes é necessario transfomrar em int

    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):

        print("\nTentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100:")
        print("Você digitou:", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você digitou um número fora do limite imposto")
            continue

        acertou = chute == numero_secreto
        maior   = chute >  numero_secreto
        menor   = chute <  numero_secreto

        if(acertou):
            print("\nParabens! Você acertou e fez {} pontos!".format(pontos))
            print("Fim de jogo!")
            break#termina abruptamente o ciclo do for ou while
        else:
            if(menor):
                print("Seu chute foi menor que o numero secreto!")
            if (maior):
                 print("O seu chute foi maior que o número secreto")
            if (rodada == total_de_tentativas):
                print("\nO número secreto era {} Você fez {}".format(numero_secreto, pontos))
                print("Fim de jogo!")

            pontos_perdidos = abs(numero_secreto - chute) #abs() dá o valor absoluto

            pontos_perdidos = abs(numero_secreto - chute) #abs() dá o valor absoluto  v
            pontos = pontos - pontos_perdidos
        rodada = rodada + 1

if (__name__ == "__main__"): #para poder-se chamar a função pelo prompto ou ide
    jogar()