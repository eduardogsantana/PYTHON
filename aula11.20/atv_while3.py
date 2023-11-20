numeros = 1
num01 = 0

while numeros <= 5:
    num = int(input("Digite um número: "))
    if num > num01:
        num01 = num
    numeros += 1

print(f'O maior número é o {num}')

