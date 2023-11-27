preco = float(input('Informe o preço do produto desejado: '))
desconto01 = 0.2
desconto02 = 0.5
desconto03 = 0.8

valor = preco * desconto01
print(valor)

if preco < 100:
    valor = preco * desconto01
elif preco >= 100 and preco <= 500:
    valor = preco * desconto02
elif preco > 500:
    valor = preco * desconto03
else:
    print(f'O valor {preco} não está apto a descontos.')