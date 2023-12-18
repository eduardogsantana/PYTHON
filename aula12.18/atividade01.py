# dunder método => __metodo__
# __str__ = método de impressão

class Pessoa:
    nome = 'Eduardo'

    #self.nome_classe = self;__class__.__name__

class Empregado(Pessoa):
    cargo = 'Professor'
    salario = 1500

class Estudante(Pessoa):
    matricula = 5523
    def __str__(self):
        return f'Seu nome é: {self.nome} e sua matrícula é: {self.matricula}'

class EstudanteGraduacao(Pessoa):
    curso = 'Administração'

class EstudantePos(Pessoa):
    orientador = 'Prof Paulo'
    nivel = 3
    def __str__(self):
        return f'Seu orientador é o: {self.orientador} e seu nível é de: {self.nivel}'

pessoa1 = Estudante()
pessoa2 = EstudantePos()

print(pessoa1)
print(pessoa2)