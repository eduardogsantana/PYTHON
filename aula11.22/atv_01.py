contador_par = 0
contador_impar = 0

for i in range(1,11):
    numeros = int(input('Digite um número inteiro: '))
    if numeros % 2 == 0:
        contador_par += 1
    else:
        contador_impar += 1

print(f'{contador_par} números são pares.')
print(f'{contador_impar} números são ímpares.')