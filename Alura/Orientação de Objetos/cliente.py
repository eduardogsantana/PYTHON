class Cliente:
    def __init__(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome.title()


nome_cliente = Cliente("joão")

print(nome_cliente.get_nome())