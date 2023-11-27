from random import randint

placar_jogador = 0
placar_computador = 0


while True:
    jogador01 = input('Escolha par ou impar: ').lower()

    numero_jogador01 = int(input("Escolha seu número: "))
    numero_computador = randint(0,10)

    print(f'O número escolhido pelo computador foi: {numero_computador}')

    soma = numero_jogador01 + numero_computador

    if soma % 2 == 0:
        if jogador01 == 'par':
            placar_jogador += 1
            print(f'Jogador 1: Você ganhou com o número: {numero_jogador01}.')
        else:
            placar_computador += 1
            print(f'O computador ganhou com o número: {numero_computador}')
    else:
        if jogador01 == 'impar':
            placar_jogador += 1
            print(f'Jogador 1: Você ganhou com o número: {numero_jogador01}.')
        else:
            placar_computador += 1
            print(f'O computador ganhou com o número: {numero_computador}')
    print(f'O placar atual é de: Jogador {placar_jogador} x Computador {placar_computador}')
    diferenca = placar_computador - placar_jogador
    sair = input('Digite [s] para Sair: ').lower()
    if sair == 's':
        if placar_computador > placar_jogador:
            confirmar_saida = input(f'Você está perdendo para o computador por {diferenca} pontos de diferença, deseja mesmo sair? Digite [Frango] para sair: ').lower()
            if confirmar_saida == 'frango':
                break
            else:
                continue
        
        print('Volte sempre!!!')
        break



