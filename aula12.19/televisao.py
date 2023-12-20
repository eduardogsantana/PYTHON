class Televisão:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.canal = 0
        self.ligada = False

    #GETS
    def get_tamanho(self):
        return self.tamanho
    def get_canal(self):
        return self.canal
    
    # SETS
    def set_tamanho(self, novo_tamanho):
        self.tamanho = novo_tamanho
    def set_canal(self, novo_canal):
        if self.ligada == True and novo_canal > 0  and novo_canal <= 999:
                self.canal = novo_canal

    def valida_ligada(self):
        if self.ligada == True:
            return 'Ligada'
        else:
            return 'Desligada'

    def ligar(self):
        self.ligada = True
        print('Você ligou a televisão.')
    
    def desligar(self):
        self.ligada = False
        print('A televisão está desligada.')

    def __str__(self):
        return f'Sua televisão é de: {self.valida_ligada()}, tem o tamanho de: {self.tamanho} polegadas, e está no canal {self.canal}'


tv = Televisão(32)

tv.ligar()
tv.set_canal(10)
print(tv.get_canal())
tv.desligar()
tv.set_canal(12)
print(tv.get_canal())
print(tv)