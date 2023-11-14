# uma lista é representada pelos "[]"
# len = método que retorna a quantidade de itens de uma lista. OBS: Todo método por obrigação ele retorna algum valor.
# del = remove item específico da lista pelo índice.
# remove = remove item pelo valor.
# pop = remove o último item da lista.
# insert = adiciona um objeto onde desejar na lista.
lista = []
print(lista)
lista = ['front']
print(lista, type(lista))
print(len(lista))
lista = ['back']
print(lista, type(lista))
print(len(lista))
lista.append('front') # metodo que insere itens no final da lista
print(lista, type(lista))
print(len(lista))