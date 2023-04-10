
def jogar():
    print("\n*********************************")
    print("***Bem vindo ao jogo de forca***!")
    print("*********************************")

    palavra = "banana"
    # Uma lista para verificar a quantidade de letras acertadas
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False

    print(letras_acertadas)

    while (not acertou and not enforcou):

        chute = input("Qual a letra?")
        chute = chute.strip() #Para que não haja espaço no inicio ou no final
        index = 0

        #Realizamos a iteração das letras na palavra e verificamos se ela faz parte da palavra
        for letra in palavra:
            #Para que não haja diferença entre serem maiusculas ou minusculas
            if(chute.upper() == letra.upper()):
                letras_acertadas [index] = letra
            index= index + 1

        print(letras_acertadas)


    print("Fim de jogo!")

#Para ser possível chamar a função pelo prompto ou o IDE
if (__name__ == "__main__"):
    jogar()
