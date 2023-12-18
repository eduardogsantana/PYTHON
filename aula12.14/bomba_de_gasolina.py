class BombaGasolina:
    def __init__(self, quantidade_combustivel):
        self.tipo_combustivel = None
        self.valor_litro = 0
        self.quantidade_combustivel = quantidade_combustivel
        self.valor_pagar = 0

    def get_tipo_combustivel(self):
        tipo = input('Você deseja abastecer com Álcool ou Gasolina? ').lower()
        if tipo == 'álcool':
            print('Você escolheu abastecer com Álcool')
            self.valor_litro == 4.30
        elif tipo == 'gasolina':
            print('Você escolheu Gasolina')
            self.valor_litro == 6.30
    
    def quantidade_litros(self):
        pass
