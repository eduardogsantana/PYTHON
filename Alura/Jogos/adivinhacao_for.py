print(34 * "*")
print("Bem vindo ao jogo de Adivinhação!!")
print(34 * "*")

numero_secreto = 12
tentativas = 5
rodadas = 1

for rodada in range(1, tentativas + 1):
    print(f'Tentativa {rodadas} de {tentativas}')
    chute = int(input("Digite número um número de 1 a 15: "))
    print("Você digitou o número:",chute)

    acertou = chute == numero_secreto
    menor = chute < numero_secreto
    maior = chute > numero_secreto

    if acertou:
        print("Você acertou o número secreto, PARABÉNS!!!!")
    
    else:
        if menor:
            print("Você errou, seu chute foi menor que o número secreto, tente novamente")
        elif maior:
            print("Você errou, seu chute foi maior que o número secreto, tente novamente.")
    rodadas = rodadas + 1

print("FIM DE JOGO!!")