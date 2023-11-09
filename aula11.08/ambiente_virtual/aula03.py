#Operadores IN e NOT IN
nome = "Eduardo Gomes"
print ( 'uard' in nome)

seu_nome = input('Digite seu nome corretamente: ')
buscar = input('Informe o valor a ser encontrado: ')

if (buscar in seu_nome):
    print(f'{buscar} está contido em {seu_nome}')
else:
    print(f'{buscar} NÃO está contido em {seu_nome}')

nao_nome = "Mariazinha"
print( 'iaz' not in nao_nome)