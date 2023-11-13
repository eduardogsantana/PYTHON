import forca
import adivinhacao_for


print(34 * "*")
print("Selecione seu jogo!!")
print(34 * "*")

print("(1) Jogo da Forca (2) Jogo da Adivinhação")

jogo = int(input("Qual jogo deseja selecionar? "))

if(jogo == 1):
    print("Jogo da forca")
    forca.jogar()
elif(jogo == 2):
    print("Jogo da adivinhação")
    adivinhacao_for.jogar()
