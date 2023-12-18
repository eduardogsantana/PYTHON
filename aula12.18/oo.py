# Herança é o mecanismo pelo qual pode-se definir uma nova classe de objetos a partir de uma classe já existente, esta nova classe poderá aproveitar o comportamento e possíveis atributos da classe estendida.

class Estudante:
    nome = 'Eduardo'
    matricula = 123456

class EstudanteGraduacao(Estudante):
    curso = 'Administração'

class EstudantePos(Estudante):
    nivel = 1
    orientador = 'Prof Paulo'

aluno = EstudantePos()
print(aluno.nome)
print(aluno.orientador)