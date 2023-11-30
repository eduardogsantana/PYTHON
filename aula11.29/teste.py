def respostas():
    lista_questoes = ['v','f','v','f','v','f','v','f','v','f']
    respostas_usuario = []
    for i in range(1,11):
        respondendo = input(f"Digite a resposta da questão {i}: ")
        respostas_usuario.append(respondendo)

    respostas_corretas = 0
    for i in range(10):
        if respostas_usuario == lista_questoes:
            respostas_corretas += 1
    
    print(f"Foram acertadas {respostas_corretas} questões de 10 possíveis.")

respostas()