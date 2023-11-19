import random

def imprime_mensagem_abertura():
    print(34 * "*")
    print("Bem vindo ao jogo de Forca!!")
    print(34 * "*")

def jogar():

    imprime_mensagem_abertura()

    arquivo = open("palavras.txt", "r")
    palavras_1 = []

    for linha in arquivo:
        linha = linha.strip()
        palavras_1.append(linha)

    arquivo.close()
    numero = random.randrange(0, len(palavras_1))
    palavra_secreta = palavras_1[numero].upper()

    letras_acertadas = ["_" for letra in palavra_secreta]
     
    print(letras_acertadas)

    enforcou = False
    acertou = False
    tentativas = 0 

    #enquanto (True and True):
    while(not enforcou and not acertou):

        chute = input("Qual letra deseja chutar? ")
        chute = chute.upper()
        chute = chute.strip()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra.upper()):
                    letras_acertadas[index] = letra
                index = index + 1
        else:
            tentativas = tentativas + 1
             
        print("  _______     ")
        print(" |/      |    ")

        if(tentativas == 1):
            print(" |      (_)   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")

        if(tentativas == 2):
            print(" |      (_)   ")
            print(" |      \     ")
            print(" |            ")
            print(" |            ")

        if(tentativas == 3):
            print(" |      (_)   ")
            print(" |      \|    ")
            print(" |            ")
            print(" |            ")

        if(tentativas == 4):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |            ")
            print(" |            ")

        if(tentativas == 5):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |            ")

        if(tentativas == 6):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
        print(" |      /     ")

        if (tentativas == 7):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      / \   ")

        print(" |            ")
        print("_|___         ")
        print()


        enforcou = tentativas == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)


    if(acertou):
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    else:
        print("Puxa, você foi enforcado!")
        print("A palavra era {}".format(palavra_secreta))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
    
    print("!!!! Fim de jogo!!!!")

if(__name__ == "__main__"):
    jogar()