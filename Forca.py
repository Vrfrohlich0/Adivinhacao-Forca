
def jogar():
    print("\n*********************************")
    print("***Bem vindo ao jogo de forca***!")
    print("*********************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while (not acertou and not enforcou):

        chute = input("Qual a letra?")

        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                print(chute)
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index= index + 1

        print("jogando...")












    print("Fim de jogo!")
#para poder-se chamar a função pelo prompto ou ide
if (__name__ == "__main__"):
    jogar()
