def jogar():


    print(34 * "*")
    print("Bem vindo ao jogo de Forca!!")
    print(34 * "*")
    palavra_secreta = "batata"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    tentativas = 0  

    print(letras_acertadas)

    enforcou = False
    acertou = False

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

        enforcou = tentativas ==6

    

        print(letras_acertadas)
    print("!!!! Fim de jogo!!!!")

if(__name__ == "__main__"):
    jogar()