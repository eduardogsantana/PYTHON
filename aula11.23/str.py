# count - função é contar quantas vezes um determinado caractere aparece em uma string.
# upper e a lower - dois métodos que deixa a string toda maiúscula ou minúscula respectivamente
# find - busca por uma expressão dentro da frase
# replace - é utilizado para realizar alterções dentro das strings
# capitalize - Deixa a primeira letra da frase maiúscula.
# split - Transforma a string numa lista.
frase = " A banana é amarela e o abacate é verde. ".lower()
letra = 'a'

print(f'A letra "{letra}" aparece "{frase.count(letra)}" vezes na frase "{frase}"')

achei = frase.find('nana')
if achei >= 0:
    print(f'A expressão se inicia no índice {achei}')
else:
    print('Não achei a expressão.')

nova_frase = frase.replace('banana', 'manga')
print(frase)
print(nova_frase)
print(frase.split())