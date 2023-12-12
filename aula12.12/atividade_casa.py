# • Escreva um código que, recebe três palavras e uma frase, crie uma função que verifique se as palavras aparecem COMPLETAS na frase e indique qual intervalo de índices ele foi encontrada. Você deve utilizar uma lista para realizar a atividade.
# Obs.: você deve validar se a palavra tem três ou mais letras
# Obs.: você deve validar se a frase tem pelo menos 20 palavras
def palavras_na_frase(palavra1, palavra2, palavra3, frase):
    palavras_na_frase = frase.split()
    
    if len(frase) < 20:
        return print("A frase precisa ter pelo menos 20 palavras.")
    
    palavras = [palavra1, palavra2, palavra3]
    for palavra in palavras:
        if len(palavra) < 3:
            return print("Todas as palavras precisam ter três ou mais letras.")
    
    indices = []
    for i in range(len(palavras_na_frase)):
        if palavras_na_frase[i] == palavra1 and palavras_na_frase[i+1] == palavra2 and palavras_na_frase[i+2] == palavra3:
            indices.append(i)
    
    if indices:
        return print(f"As palavras foram encontradas nos índices: {indices}")
    else:
        return print("As palavras não foram encontradas na frase.")

palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")
palavra3 = input("Digite a terceira palavra: ")
frase = input("Digite a frase: ")

resultado = palavras_na_frase(palavra1, palavra2, palavra3, frase)
print(resultado)
