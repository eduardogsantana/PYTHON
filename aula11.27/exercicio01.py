def numero_p_n(numero):

    if numero <= 0:
        return "N"
    elif numero > 0 :
        return "P"
    
numero2 = int(input('Digite um número: '))

print(numero_p_n(numero2))
