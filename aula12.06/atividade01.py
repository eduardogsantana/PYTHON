# 1. Crie uma lista de alunos com nome e nota final de cada aluno e coloque em um dicionario, depois imprima:
'''dicionario = {}
lista_alunos = [['Eduardo', 10],['Elvis', 10],['Francisco', 10]]

dicionario.update(lista_alunos)
print(dicionario)
# 2.
lista_nomes2 = [['Mikael', 10],['Artur', 10],['Jeferson', 10], ['Alice', 10]]
dicionario.update(lista_nomes2)
print(dicionario)
dicionario.update({'Junior': 10, 'Lara': 10, 'Jefeson': 10, })
print(dicionario)'''

#3. 
''''lista_marca_modelo = []

marca = input('Digite a marca do seu carro: ')
modelo = input('Digite o modelo do seu carro: ')
lista_marca_modelo.append(marca)
lista_marca_modelo.append(modelo)

dic_marca_modelo = {}
dic_marca_modelo.update([lista_marca_modelo])

print(lista_marca_modelo)
print(dic_marca_modelo)

dic_marca_modelo['Fiat'] = 'Uno' # método para adicionar um por vez.
print(dic_marca_modelo)'''

#4. # crie um cadastro de clientes recebendo nome, idade, data de aniversário e endereço completo(rua, numero da casa e bairro). Adicione todas as informações em um dicionário. Imprima ao final.


'''lista_cadastro = []
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
data_aniversario = input('Digite sua data de aniversário: ')
endereco_rua = input('Digite o nome da sua rua: ')
endereco_numero = input('Digite o número da sua casa: ')
endereco_bairro = input('Digite o seu bairro: ')

lista_cadastro.append(nome)
lista_cadastro.append(idade)
lista_cadastro.append(data_aniversario)
lista_cadastro.append(endereco_rua)
lista_cadastro.append(endereco_bairro)
lista_cadastro.append(endereco_numero)
dic_cadastro = {}
dic_cadastro.update([lista_cadastro])

print(dic_cadastro)'''

# 5.Vamos criar um sistema de login e senha. Crie um dicionário contendo os acessos dos colaboradores com nome de usuário e senha. Em seguida peça as informações e valide o login do usuário.
validar_acesso = {
    'Eduardo': '123',
    'Elvis': '456',
    'Mikael': '321'
}

usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario in validar_acesso and validar_acesso[usuario] == senha:
    print("Login validado.")
else:
    print("Usuário ou senha incorretos.")