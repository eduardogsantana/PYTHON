while True:
    usuario = input("Digite o nome de usuário desejado: ")
    senha = input("Digite a senha desejada: ")
    if senha == usuario:
        print("Sua senha não pode ser igual ao nome de usuário, digite corretamente as informações. ")
    else:
        break