import Forca
import Adivinhacao
#Foram importados os arquivos dos outros jogos


def escolha_jogo():
    print("\n*********************************")
    print("********Escolha o seu jogo!********")
    print("*********************************")

    print("(1) forca (2) adivinhção")

    jogo = int(input("Qual jogo?"))

    #Chama as funções e por consequência os codigos dos outros jogos
    if (jogo == 1):
        print("Inicializando o jogo de forca")
        Forca.jogar()

    elif (jogo == 2):
        print("Inicializando o jogo de adivinhacao")
        Adivinhacao.jogar()

#Para ser possível chamar a função pelo prompto ou o IDE
if (__name__ == "__main__"):
    escolha_jogo()
