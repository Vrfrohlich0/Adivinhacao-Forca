import Forca
import Adivinhacao
#foram importados os arquivos dos outros jogos
#Mas como ao importar um arquivo ele já roda direto, foram criadas as funções pra poder escolher o jogo dentro do if

def escolha_jogo():
    print("\n*********************************")
    print("********Escolha o seu jogo!********")
    print("*********************************")

    print("(1) forca (2) adivinhção")

    jogo = int(input("Qual jogo?"))

    #chama as funções e por consequencia os codigos dos outros jogos
    if (jogo == 1):
        print("Inicializando o jogo de forca")
        Forca.jogar()
    #elif é o meio termo entre if e else em que vem dps de um if, mas pode-ser usar comandos
    elif (jogo == 2):
        print("Inicializando o jogo de adivinhacao")
        Adivinhacao.jogar()
#para poder-se chamar a função pelo prompto ou ide
if (__name__ == "__main__"):
    escolha_jogo()
