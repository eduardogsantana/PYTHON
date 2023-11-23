class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto....")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'O saldo é de R${self.__saldo}, da conta do titular {self.__titular}.')

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite



conta_1 = Conta(123, "Gomes", 1500.0, 5000.0 )
conta_2 = Conta(312, "Santana", 1000.0, 4000.0)

print(conta_1.get_saldo())

conta_2.transfere(500.0, conta_1)
conta_1.set_limite(15000.0)

print(f'O limite é de {conta_1.get_limite()}')
conta_2.extrato()
conta_1.extrato()



