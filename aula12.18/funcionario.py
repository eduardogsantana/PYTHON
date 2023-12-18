# cria a abstração para uma super classe funcionário com duas subclasses.

class Funcionario:
    def __init__(self, nome, idade):
        self.nome = nome
        self.nome = idade

class recepcionista(Funcionario):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        

class vigia(Funcionario):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)