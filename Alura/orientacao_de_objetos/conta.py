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

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel

    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f'O valor {valor} é maior do que o limite disponível para saque. ')

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def get_numero_conta(self):
        return self.__numero

    @property
    def get_saldo(self):
        return self.__saldo

    @property
    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "12"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}