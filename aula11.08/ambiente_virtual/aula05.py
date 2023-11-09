# Fatiamento de strings
# Obs: Toda string por padrão é uma lista que não saiu do armário.
# Ordem de tratamento:
# 012345678......
# -87654321......
# [i,f,p] i: início f:fim p:PARSE


nome = "João Eduardo"
lista_nome = "J","o","ã","o","E","d","u","a","r","d","o"
print(nome[8])
print(nome[-4])
print(lista_nome[8])
print(lista_nome[-4])

print(nome[5:12])
print(nome[0::2]) # pares
print(nome[1::2]) #ímpares


