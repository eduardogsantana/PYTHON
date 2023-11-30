#nome variável - atribuindo valor - valor
variavel = 'abcdefghijk'
print(variavel[::-1])

frase = 'A casa de Kaynan é azul igual ao céu'
print(frase[19:24])


# utilizando fatiamento e repetição imprima uma lista de "a" até "e" removendo uma letra de cada vez.
lista = ['a', 'b', 'c', 'd', 'e']
for i in range(6):
   print(lista[:5-i])