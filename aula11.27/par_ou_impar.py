jogador01 = input('Escolha par ou impar: ').lower()

if jogador01 == "par":
    jogador02 = "impar"
else:
    jogador02 = "par"

numero_jogador01: int(input("Escolha seu número: "))
numero_jogador02: int(input("Escolha seu número: "))

soma = numero_jogador01 + numero_jogador02

if soma % 2 == 0:
    if jogador01 == 'par':
        print('Jogador 1: Você ganhou.')
    else:
        print('Jogador 2: Você ganhou')
else:
    if jogador02 == 'impar':
        print('Jogador 1: Você ganhou.')
    else:
        print('Jogador 2: Você ganhou')
