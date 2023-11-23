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
    
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)



conta_1 = Conta(123, "Gomes", 1500.0, 5000.0)
conta_2 = Conta(312, "Santana", 1000.0, 4000.0)

conta_2.transfere(100.0, conta_1)

conta_2.extrato()
conta_1.extrato()
