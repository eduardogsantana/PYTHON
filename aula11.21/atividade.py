
lista_inteiros = []
contador = 0
while contador <= 10:
    contador = int(input('numero: '))
    lista_inteiros.append(contador)
    contador += 1
    
print(lista_inteiros[0::2])
print(lista_inteiros[1::2])