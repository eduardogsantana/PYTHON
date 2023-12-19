# cria a abstração para uma super classe funcionário com duas subclasses.
class Funcionario:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Professor(Funcionario):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.materia = input(f'Professor {nome}, digite qual matéria você ensina: ').capitalize()
        self.turno = input(f'Professor {nome}, digite o seu turno: ').capitalize()
    
    def __str__(self):
        return f'Seja bem-vindo, professor: {self.nome}, leciona a matéria: {self.materia}, no turno: {self.turno}'
        

class Diretor(Funcionario):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.direcao = input(f'Diretor {nome}, digite qual departamento você dirige: ').capitalize()

    def __str__(self):
        return f'Seja bem-vindo, diretor {self.nome}, você dirige o departamente: {self.direcao}'

professor = Professor('Eduardo', 27)
print(professor)

diretor = Diretor('João', 27)
print(diretor)