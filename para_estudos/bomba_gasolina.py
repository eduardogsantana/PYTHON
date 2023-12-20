class BombaGasolina:
    def __init__(self, quantidade_combustivel):
        self.quantidade_combustivel = quantidade_combustivel
        self.tipo_combustivel = None
        self.valor_combustivel = 0
        self.valor_pagar = 0 

    def set_tipo_combustivel(self):
        print('!!!!SEJA BEM VINDO AO POSTO ELVIS VALLEY!!!!')

        while True:
            self.tipo_combustivel = input('Qual o tipo de combustível deseja, Digite [A] para Álcool ou [G] para Gasolina: ').lower()

            if self.tipo_combustivel == 'a':
                self.valor_combustivel = 4.50
                print(f'Você irá pagar R${self.valor_combustivel:.2f} por litro de Álcool')
                self.escolha_cliente()
                break
            elif self.tipo_combustivel == 'g':
                self.valor_combustivel = 6.30
                print(f'Você irá pagar R${self.valor_combustivel:.2f} por litro de Gasolina')
                self.escolha_cliente()
                break
            else:
                print('Opção inválida, por favor, escolha entre [A] para Álcool ou [G] para Gasolina.')

    def escolha_cliente(self):
        while True:
            escolha = input('Você deseja abastecer em litros ou dinheiro? Digite [L] para litros e [D] para dinheiro: ').lower()

            if escolha == 'l':
                self.abastecer_litro()
                break
            elif escolha == 'd':
                self.abastecer_dinheiro()
                break
            else:
                print('Opção inválida, por favor, escolha entre [L] para litros ou [D] para dinheiro.')

    def abastecer_litro(self):
        litro = float(input('Digite a quantidade de litros desejada: '))
        self.valor_pagar = litro * self.valor_combustivel

        if litro > self.quantidade_combustivel:
            print(f'Quantidade de litros insuficiente. A quantidade de litros da bomba é de: {self.quantidade_combustivel} litros. Por favor, tente novamente. ')
            self.abastecer_litro()
        
        elif self. quantidade_combustivel >= litro:
            print(f'Você irá pagar R${self.valor_pagar} em {litro} litros.')
            self.quantidade_combustivel -= litro
            print(f'A quantidade de litros atual da bomba é de: {self.quantidade_combustivel} litros')

    def abastecer_dinheiro(self):
        dinheiro = float(input(f'Digite o valor em R$ que você deseja abastecer: '))
        litros_abastecidos = dinheiro / self.valor_combustivel
        print(f'Você vai pagar R${dinheiro} em {litros_abastecidos:.2f} litros')
        self.quantidade_combustivel -= litros_abastecidos
        print(f'A quantidade de litros atual da bomba é de: {self.quantidade_combustivel:.2f}')
        

bomba = BombaGasolina(1000)
bomba.set_tipo_combustivel()