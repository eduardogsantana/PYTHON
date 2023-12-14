class Restaurante:
    def __init__(self):
        self.cliente = None
        self.pedido_anotado = False
        self.pedido = False
        self.cliente_chegou = False

    def reserva_cliente(self):
        nome_reserva = []
        mesas_disponíveis = ['1','2','3','4','5','6','7','8','9']
        horario_disponivel = ['18:00', '18:30', '19:00','19:30', '20:00']
        self.cliente = input('Digite seu nome: ')
        nome_reserva.append(self.cliente)
        
        while True:
            mesa = input('Qual mesa deseja reservar: ')
            if mesa in mesas_disponíveis:
                print(f'A mesa: {mesa}, está disponível e foi reservada para o cliente {self.cliente}')
                break
            else:
                print(f'A mesa {mesa} não está disponível no momento, por favor escolha outra. ')

        while True:      
            horario_reserva = input('Qual horário deseja reservar: ')
            if horario_reserva in horario_disponivel:
                print(f'O horário deseja de {horario_reserva}, está disponível e foi reservado por {self.cliente}.')
                break
            else:
                print(f'O horario de {horario_reserva} não está disponível, por favor escolha outro.')
            

        print(f'O cliente: {self.cliente}, reservou a mesa: {mesa}, no horário: {horario_reserva}.')
    
    def anotar_pedido(self, cliente_chegou, ):
        self.cliente_chegou = cliente_chegou
        if cliente_chegou == True:
            print(f'O cliente {self.cliente} já chegou.')
            pedidos = []
            while True:
                pedido_cliente = input('Faça o seu pedido: ')
                pedidos.append(pedido_cliente)
                fim_pedido = input('Deseja algo mais? ')
                if fim_pedido == 'não':
                    print(f'Seu pedido de: {pedidos} foi anotado, aguarde até ficar pronto.')
                    pedido = True
                    break
        elif cliente_chegou == False:
            print(f'O cliente {self.cliente} ainda não chegou, aguarde.')

    def preparar_comida(self):
        if self.pedido  == True:
            print('O seu pedido está sendo preparado. ')
        else:
            print('O pedido não foi feito.')
            

        




restaurante = Restaurante()
restaurante.reserva_cliente()
restaurante.anotar_pedido(False)
restaurante.preparar_comida()