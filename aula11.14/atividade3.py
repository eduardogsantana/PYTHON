# 3. faça um código que pede 3 notas de quatro alunos, calcula a media e printa as medias em uma lista.

lista_media = []
aluno1_1 = float(input("Digite uma nota: "))
aluno1_2 = float(input("Digite uma nota: "))
aluno1_3 = float(input("Digite uma nota: "))

media1 = (aluno1_1 + aluno1_2 + aluno1_3) / 3

lista_media.append(media1)

aluno2_1 = float(input("Digite uma nota: "))
aluno2_2 = float(input("Digite uma nota: "))
aluno2_3 = float(input("Digite uma nota: "))

media2 = (aluno2_1 + aluno2_2 + aluno2_3) / 3

lista_media.append(media2)

aluno3_1 = float(input("Digite uma nota: "))
aluno3_2 = float(input("Digite uma nota: "))
aluno3_3 = float(input("Digite uma nota: "))

media3 = (aluno3_1 + aluno3_2 + aluno3_3) / 3

lista_media.append(media3)
print(lista_media)

