# For trabalha com iteráveis.
# Tem que possuir uma variável de controle.
# iter() - transforma um objeto em iteravel.
# next() - função par imprimir os iteráveis de uma "lista".
# enumerate() - é um iterador de indices e valores.

lista_nomes = ['João', 'Pedro', 'Mateus', 'Judas', 'Tiago']

lista_enumerada = enumerate(lista_nomes)
print(lista_nomes)
print(lista_enumerada)

for item in lista_enumerada:
    print(item)

for indice_lista, nome_lista in enumerate(lista_nomes):
    print(f'O {nome_lista} é o {indice_lista} da lista')