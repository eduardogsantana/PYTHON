# para usar o property o atributo dos métodos tem que estar privado

class FoneDeOuvido:
    def get_volume(self):
        print('Entrei no GET')
        return self.__volume
    
    def set_volume(self, novo_volume):
        print('Entrei no SET')
        self.__volume = novo_volume

    volume = property(get_volume, set_volume)

fone = FoneDeOuvido()
fone.volume = 200
print(fone.volume)