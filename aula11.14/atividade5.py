# 5. faça um código que crie uma lista com 20 números inteiros e armazene os números pares na lista pares e os números impares na lista impar, imprima as duas listas.

lista_1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(lista_1)

lista_pares = []
lista_impares= []

lista_pares = lista_1[1::2]
print(lista_pares)

lista_impares = lista_1[2::2]
print(lista_impares)