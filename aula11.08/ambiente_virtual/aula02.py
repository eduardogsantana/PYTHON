entrada = input('[E] para entrar e [S] para passar: ')
senha_digitada = input('Digite a senha de acesso: ')
senha = "123456"

if (entrada == 'E' or entrada == 'e'):
    if (senha == senha_digitada):
        print("Sucesso, você entrou no sistema")
    else:
        print("Senha incorreta")
elif (entrada == 'S' or entrada == 's'):
    if (senha == senha_digitada):
        print("Sucesso, você passou")
    else:
        print('Você errou a senha.')

else:
    print("Você não selecionou para entrar")