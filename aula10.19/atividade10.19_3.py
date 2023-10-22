# Crie um código que receba o salário atual de um funcionário, que receba o valor em porcentagem de reajuste e 
# calcule o valor do novo salário reajustado de acordo com valor de reajuste(%).

salario_atual = float(input("Digite seu salário atual: "))
porcentagem_reajuste = float(input("Digite a porcentagem de aumento:"))

aumento = salario_atual * porcentagem_reajuste / 100

salario_aumento = salario_atual + aumento

print(f'Seu salario será de R${salario_aumento}. De acordo com a porcentagem de reajuste fornecida.')


