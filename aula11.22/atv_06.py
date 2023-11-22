# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia um conjunto 
# indeterminado de temperaturas em graus celsius, e informe ao final a menor e a maior temperaturas informadas.
# Para sair do programa deve digitar "SAIR"

maior = None
menor = None

while True:
    sair = input("Digir [SAIR] para sair do programa: ")
    if sair == "SAIR" or sair == "sair":
        print("Você saiu do programa com sucesso.")
        break
    
    temperatura = float(input('Digite a temperatura desejada: '))

    if maior == None or temperatura > maior:
        maior =  temperatura
    if menor == None or temperatura < menor:
        menor = temperatura

print(f'A menor temperatura é de {menor} graus celsius, a maior temperatura é de {maior} graus celsius.')
