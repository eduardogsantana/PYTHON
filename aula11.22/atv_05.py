# Supondo que a população de um país A seja de 80000 habitantes com uma taxa anual de crescimento de 3% Faça um 
# programa que calcule e escreva o número de anos necessários para que a população do país A chegar a 120000 habitantes.

atual = 80000
crescimento = 3
anos = 0 
alvo = 120000

while atual < alvo:
        atual *= 1 + 3 / 100
        anos += 1
        
print(f'Levou {anos} anos até atingir os 120000 habitantes. ')