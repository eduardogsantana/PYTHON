# cria a abstração para uma super classe funcionário com duas subclasses.
class Funcionario:
    def __init__(self, nome, idade, cpf):
        self.__nome = nome
        self.idade = idade
        self.__cpf = cpf 

    def get_nome(self):
        return self.__nome
    
    def get_cpf(self):
        return self.__cpf
    
    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def set_cpf(self, novo_cpf):
        self.__cpf = novo_cpf
    
class Professor(Funcionario):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.materia = input(f'Professor {nome}, digite qual matéria você ensina: ').capitalize()
        self.turno = input(f'Professor {nome}, digite o seu turno: ').capitalize()
    
    def __str__(self):
        return f'Seja bem-vindo, professor: {self.__nome}, leciona a matéria: {self.materia}, no turno: {self.turno}'
        

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