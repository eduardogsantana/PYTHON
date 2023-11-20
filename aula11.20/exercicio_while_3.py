aluno = 1
while aluno <= 20:
    idade = int(input(f'Qual idade do aluno {aluno} ?: ')) 
    if (idade > 13):
        print(f'O aluno {aluno}, tem mais que 13 anos de idade.')
    aluno += 1