# Um dicionãrio pode armazenar diferentes tipos de valores. Possui CHAVE(KEYS) e VALOR(VALUE)
# Parametro: {} ou dict()
d = {"user": "Marcel" , "password": 1234}
print(type(d))
# Métodos:
# has_key('eggs'), clear(), del.d['key'], keys(), values(), items(), get(), update().
# copy() fazer cópias de dicionários ! (Lembre-se que dicionário é mutável!)
# ordenando dicionários: sorted() - ordena um dicionário na ordem crescente. sorted(d, key = d.get, reverse = True) - ordem decrescente.

print("-"*100)

pessoa = {"nome": "Eduardo",
          "sobrenome": "Gomes"}
print(len(pessoa)) # len pode ser usado para retornar a quantidade de coisas dentro do dicionário.
print(pessoa.keys())
print(pessoa.values())
for chave in pessoa:
    print(pessoa)

print("-"*100)

for valor in pessoa.values():
    print(valor)

print("-"*100)

print(pessoa["sobrenome"])

print("-"*100)

d1 = {'valor1': 100,
      'valor2': 200,
      'valor3': 300,}

d2 = d1.copy()
print(d1)

d2['valor2'] = 2000
print(d2)

print(d1) # acontece pois o d2 é só uma apontamento para a d1, d2 não é uma lista própria.

print("-"*100)

atualizar = {'valor4': 400,
             'valor5': 500,}
d1.update(atualizar)
print(d1)

print("-"*100)


