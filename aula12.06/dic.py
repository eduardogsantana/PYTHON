dic = { 'nome': 'Eduardo'} # Create
dic2 = dict(idade=27) # Create
print(dic)
print(dic2)

dic['nome'] # Read
reading = dic2.get('idade') # Read

dic.update(sobrenome= 'Gomes') # Update
dic.update(dic2) # Update
tupla = ('peso', 72.12), # Sempre que for adicionar apenas um iterável(lista ou tupla) a um dicionário, deve botar uma virgula após ele.
dic.update(tupla)
lista = ['data', '03/10/1996'],['numeros',[1,2,3,4,5,6,7,8,9]] # Update
dic.update(lista) # Update

print(dic)
print(dic2)

dic2.clear()
print(dic2)
