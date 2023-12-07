# 6. faça um quiz utilizando um dicionário com as seguintes chaves: Pergunta, opções e resposta. Faça a validação da opção escolhida com a resposta e imprima.

dic_quiz = [
    {'Pergunta': 'Quanto é 1+1?',
    'Opções': [2,4,6,8],
    'Resposta': 2,},

    {'Pergunta':'Quanto é 2+2',
    'Opções': [2,4,6,8],
    'Resposta': 4,},

    {'Pergunta':'Quanto é 3+3',
    'Opções': [2,4,6,8],
    'Resposta': 6},
]

for pergunta in dic_quiz:
    print('Pergunta:', pergunta['Pergunta'])

    for i, opcao in enumerate(pergunta['Opções']):
        print(f'{i+1})', opcao)

    escolha = int(input('Escolha sua opção: '))
    acertou = False
    if escolha == int(pergunta['Resposta']):
        acertou = True

    if acertou:
        print('Você acertou 👍')
    else:
        print('Você errou 😔')
        