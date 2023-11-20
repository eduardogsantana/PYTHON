# while = enquanto

# loop infinito: quando uma estrutura de repetição não tem fim.
# while True

contador = 0
while contador < 30:
    contador += 1 # contador = contador + 1
    print(contador)
    if(contador == 15):
        print("Chegamos ao 15")
    if(contador == 27):
        break

