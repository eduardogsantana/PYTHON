def criar_conta(numero, titular, saldo, limite):
    conta = {"Número": numero, "Titular": titular, "Saldo": saldo, "Limite": limite}
    return conta

def desposita(conta, valor):
    conta["Saldo"] += valor

def saca(conta, valor):
    conta["Saldo"] -= valor

def extrato(conta):
    print(f'O Saldo da conta é de {conta["Saldo"]}')

conta = criar_conta(123, "Eduardo", 125.0, 1000.0)
print(conta)
desposita(conta, 125.0)
extrato(conta)
saca(conta, 25.0)
extrato(conta)