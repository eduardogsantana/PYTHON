# url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"
url = " "

#sanitização da url:
url = url.replace(" ","") # poderia usar só o .strip, também tem o .lstrip que trabalha só com a esqueda e o .rstrip que trabalha só com a direita. Strip é mais indicado pois retira também caracteres especiais.


# validação da url:
if url == "": 
    raise ValueError("A URL está vazia")

 #retorna para o usuário que ocorreu um erro de valor. Nesse caso o valor da url está vazia.

indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]

url_parametros = url[indice_interrogacao+1:]
print(url_parametros)  

parametro_busca = 'moedaOrigem'
indice_parametro  = url_parametros.find(parametro_busca)
print(indice_parametro)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor) # assim ele vai procurar o caractere '&' a partir do indice que eu colocar depois da vírgula.
if indice_e_comercial == -1:
    valor  = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(valor)