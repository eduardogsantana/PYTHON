# estruturas condicionais
variavel = 20
if variavel < 20:
    print("menor que 20")
elif variavel == 20:
    print("igual a 20")
elif variavel > 20 and variavel < 50:
    print("esta no intervalo entre 21 e 49")
else:
    print("Qualquer coisa")

# estruturas de repetição = for e while.
# for sempre vai querer um iterável para comparar. Ex: range.
for i in range(1, 5):
    print(f'print o numero {i}')

contador = 5
while contador > 0 :
    print(f'Print do número: {contador}')
    contador -= 1

# join - unir strings
lista = ["Papa", "Pedro", "I"]
nome = ' '.join(lista)
print(nome)
