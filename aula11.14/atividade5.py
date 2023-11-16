# 5. faça um código que crie uma lista com 20 números inteiros e armazene os números pares na lista pares e os números impares na lista impar, imprima as duas listas.

lista_1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
list2 = ['ricao', 'ruhno', 'savbd', 'rhhro', 'rai', 'veua']
lista_pares = []
lista_impares = []
del list2[2]
del list2[3]
del list2[3]

print(list2)

del list2[2::3]
print(list2)
print([list2[1], list2[3], list2[5]])

del lista_1[0::4]

print(lista_1)

lista_pares = lista_1[1::2]
print(lista_pares)

lista_impares = lista_1[0::2]
print(lista_impares)