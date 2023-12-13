# • Escreva um código que, recebe três palavras e uma frase, crie uma função que verifique se as palavras aparecem COMPLETAS na frase e indique qual intervalo de índices ele foi encontrada. Você deve utilizar uma lista para realizar a atividade.
# Obs.: você deve validar se a palavra tem três ou mais letras
# Obs.: você deve validar se a frase tem pelo menos 20 palavras

def encontrar_palavras(palavra1, palavra2, palavra3, frase):
    
    if len(frase) < 20:
        return "A frase deve conter pelo menos 20 palavras."

    if len(palavra1) < 3 or len(palavra2) < 3 or len(palavra3) < 3:
        return "As palavras devem ter pelo menos 3 letras."

    lista_de_palavras = [palavra1, palavra2, palavra3]

    indices = []
    for i, palavra in enumerate(frase):
        if palavra in lista_de_palavras:
            indices.append(i)

    intervalos = []
    for i in indices:
        intervalo_inicio = i
        while i + 1 < len(frase) and frase[i + 1] in lista_de_palavras:
            i += 1
        intervalos.append((intervalo_inicio, i))

    return intervalos if intervalos else "Nenhuma das palavras foi encontrada na frase."

palavra1 = input('Digite uma palavra: ')
palavra2 = input('Digite uma palavra: ')
palavra3 = input('Digite uma palavra: ')
frase = input('Digite uma frase: ')

encontrar_palavras(palavra1, palavra2, palavra3, frase)