numero = int(input('Digite um número inteiro: '))
intervalo = range(1, numero + 1)
contador = 0
for i in intervalo:
    if numero % i ==0:
        print(f'foi divisivel por {i}')
        contador += 1

print(f'O número {numero} é um número primo.')
