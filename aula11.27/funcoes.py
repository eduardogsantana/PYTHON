# funções são blocos de códigos que são executados somente quando são chamados
# parametro: def
# as funções devem ter prioridade no código.

def media(nota01, nota02, nota03):
    media = (nota01 + nota02 + nota03) / 3
    return media

nota01 = int(input('Digite uma nota: '))
nota02 = int(input('Digite uma nota: '))
nota03 = int(input('Digite uma nota: '))

print(media(nota01, nota02, nota03))

nota04 = int(input('Digite uma nota: '))
nota05 = int(input('Digite uma nota: '))
nota06 = int(input('Digite uma nota: '))

print(media(nota04, nota05, nota06))


def calcular_horas_extras(quantidade_horas, valor_hora):
    horas = float(quantidade_horas)
    taxa = float(valor_hora)
    if horas >= 40:
        valor_receber = (horas - 40) * taxa

    return valor_receber


quantidade_horas = float(input('Digite quantas horas trabalhou: '))
taxa_por_hora = float(input('Digite a taxa do funcionário: '))

print(calcular_horas_extras(quantidade_horas, taxa_por_hora))