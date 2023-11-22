maior = 0
menor = None

while True:
    saida = input('Digite [S] para sair: ')
    if saida == "s" or saida == "S":
        print("Você saiu do programa. ")
        break
    
    numero = int(input("Digite um número inteiro: "))

    if numero > maior:
        maior = numero
    if menor == None or numero < menor:
        menor = numero
        
print(f'O número {maior} + {menor} é igual a {maior+menor}')
print(f'O maior número é {maior}.')
print(f'O menor número é {menor}.')
