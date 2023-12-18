class Pessoas:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.__cpf = None

    def get_cpf(self):
        return self.__cpf
    
    def set_cpf(self, novo_cpf):
        self.__cpf = novo_cpf

    def __str__(self):
        return f'O seu nome é: {self.nome}, sua idade é: {self.idade}, seu CPF é: {self.__cpf}'
    
class Professor(Pessoas):
    def __init__(self, nome, idade, salario, disciplina):
        super().__init__(nome, idade)
        self.salario = salario
        self.disciplina = disciplina

class Aluno(Pessoas):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)


paulo = Professor('Paulo', 30, 1400.00, 'Back-End')
paulo.set_cpf(12131415)
print(paulo)