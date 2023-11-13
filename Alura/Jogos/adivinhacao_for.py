import random

print(34 * "*")
print("Bem vindo ao jogo de Adivinhação!!")
print(34 * "*")

numero_secreto = random.randrange(1,21)
tentativas = 0
rodadas = 1
pontos = 1000

print("Qual nível de dificuldade você deseja?")
print("(1) Para nível fácil (2) Para nível médio (3) Para nível difícil")
nivel = int(input("Escolha seu nível: "))

if(nivel == 1):
    tentativas = 10
elif(nivel == 2):
    tentativas = 7
else:
    tentativas = 5

print(numero_secreto)

for rodada in range(1, tentativas + 1):
    print(f'Tentativa {rodadas} de {tentativas}')
    chute = int(input("Digite número um número entre 1 e 20: "))
    print("Você digitou o número:",chute)

    if(chute < 1 or chute > 20):
        print("Digite apenas um número entre 1 e 20!!!")
        continue

    acertou = chute == numero_secreto
    menor = chute < numero_secreto
    maior = chute > numero_secreto

    if acertou:
        print(f'Você acertou o número secreto e fez {pontos}, PARABÉNS!!!!')
        break
    
    else:
        if menor:
            print("Você errou, seu chute foi menor que o número secreto, tente novamente")
        elif maior:
            print("Você errou, seu chute foi maior que o número secreto, tente novamente.")
        
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
    
    rodadas = rodadas + 1



print("FIM DE JOGO!!")