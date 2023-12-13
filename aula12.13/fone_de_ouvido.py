class FoneDeOuvido:
    def get_volume(self):
        return self.volume
    
    def set_volume(self, novo_volume):
        self.volume = novo_volume

    @property
    def volume(self):
        return self.get_volume, self.set_volume
fone = FoneDeOuvido()

fone.set_volume(200)        

print(fone.volume)