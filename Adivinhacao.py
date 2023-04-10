import random

#Função
def jogar():

    print("\n*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    #Criamos um numero aleatoriamente de 1 a 100 e com o round apenas arredondando
    numero_secreto = round(random.randrange(1,101))

    total_de_tentativas = 0
    pontos = 1000

    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Defina o nível: "))

    #Para ser escolhido o nivel de dificuldade do jogo
    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    #realizando o jogo  com base na dificuldade escolhida
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

        #realizando as comparações de caso o chute seja maior, menor ou caso tenha acertado
        if(acertou):
            print("\nParabens! Você acertou e fez {} pontos!".format(pontos))
            print("Fim de jogo!")
            break
        else:
            if(menor):
                print("Seu chute foi menor que o numero secreto!")
            if (maior):
                 print("O seu chute foi maior que o número secreto")
            if (rodada == total_de_tentativas):
                print("\nO número secreto era {} Você fez {}".format(numero_secreto, pontos))
                print("Fim de jogo!")

            #Realizando o calculo para a pontuação final
            pontos_perdidos = abs(numero_secreto - chute)
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        rodada = rodada + 1

#Para ser possível chamar a função pelo prompto ou o IDE
if (__name__ == "__main__"):
    jogar()