class Automovel:
    def __init__(self, placa, cor):
        self.__placa = placa
        self.cor = cor

    @property
    def placa(self):
        return self.__placa
    
    def get_cor(self):
        return self.cor
    
    def set_cor(self, nova_cor):
        self.cor = nova_cor
    
    def dirigir(self, velocidade):
        print(f'Estou dirigindo a {velocidade}km/h.')

    

    
# Sempre que estiver criando suas classes em Python, você deve separar seus métodos por categoria.
carro = Automovel('ABC-2323', 'Verde')
moto = Automovel('XTZ-1516', 'Azul')

print(f'A placa do carro é: {carro.placa}')
print(f'A placa da moto é: {moto.placa}')
print(f'A cor do carro é: {carro.get_cor()}')
print(f'A cor da moto é: {moto.get_cor()}')
carro.dirigir(100)
moto.dirigir(80)


carro.set_cor('Amarelo')
print(f'A nova cor do carro é: {carro.get_cor()}')




