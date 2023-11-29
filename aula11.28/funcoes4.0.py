# Escreva uma função chamada gorjeta, que recebe o valor da conta de um restaurante, calcule e exiba a gorjeta do garçom considerando 12% do valor da conta

def gorjeta(valor_conta):
    valor_gorjeta = valor_conta * 0.12
    
    print(f"A gorjeta é de R${valor_gorjeta: }")

conta = float(input("Digite quanto deu a conta: R$ "))
gorjeta(conta)
