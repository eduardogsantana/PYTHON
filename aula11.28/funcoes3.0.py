def quantidade_digitos(numero):
    quant_digi = len(numero)
    return int(quant_digi)

numero = input('Digite um número inteiro: ')
print(quantidade_digitos(numero))