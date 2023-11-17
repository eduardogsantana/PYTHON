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

        enforcou = tentativas == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
    if(acertou):
        print("Você ganhou o jogo, PARABÉNS!!!!!")
    else:
        print("Você perdeu, tente novamente!!!")
    
    print("!!!! Fim de jogo!!!!")

if(__name__ == "__main__"):
    jogar()