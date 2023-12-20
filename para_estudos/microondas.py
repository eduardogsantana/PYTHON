class Microondas:
    def __init__(self):
        self.painel = False
        self.botao = None
        self.tempo = 0

    def get_tempo(self):
        return self.tempo
    def set_tempo(self, novo_tempo):
        self.tempo = novo_tempo


    def ligar(self):
        self.painel = True
        print('O microondas está ligado.')
    def desligar(self):
        self.painel = False
        print('O microondas está desligado. ')