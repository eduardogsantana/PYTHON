class Conta:

    def __init__(self,numero, titular, saldo, limite):
        print("Construindo objeto....")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    
    def extrato(self):
        print(f'O saldo é de R${self.saldo}, da conta do titular {self.titular}.')

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor



conta = Conta(122, "João", 500.0, 1000.0)
conta_2 = Conta(123, "Eduardo", 50.0, 1000.0)

conta.deposita(100.0)
conta_2.deposita(50.0)

print(conta.saldo) # Para acessar o atributo específico que deseja.
print(conta.extrato())
print(conta_2.extrato())