# outra forma de INTERPOLAR

nome = "Geisa"
salario = 4500.99

print(nome,"ganha um salário de R$",salario)
print(f'O salário de {nome} é R$ {salario}')

# forma FORMAT de imprimir:
# Regras FORMAT:
# s: string
# "d" e "i": int
# f: float
# x e X: hexadecimais

print('Quem ganha um salário de R$ %.2f é a %s' %(salario, nome))