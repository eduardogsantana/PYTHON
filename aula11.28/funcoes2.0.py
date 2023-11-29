def numero_reverso(numero):
    num_rev = numero [::-1]
    return int(num_rev)

def numero_reverso2(numero):
    reverso = 0
    while numero > 0:
        ultimo_valor = numero % 10 # pegar o último valor.
        reverso = (reverso * 10) + ultimo_valor # adiciona o último valor.
        numero = numero // 10 #tira o ultimo valor.
    return reverso   

numero = int(input('Digite um número inteiro: '))

print(f'O número informado foi {numero} e o reverso dele é {numero_reverso2(numero)}')
