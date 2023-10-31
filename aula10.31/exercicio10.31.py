distancia_km = float(input("Digite quantos KM você andou: "))
quantidade_litros = float(input("Quantos litros de combustivel foram consumidos?: "))

consumo = distancia_km / quantidade_litros

if consumo < 8:
    print("Venda o carro")
elif consumo >= 8 and consumo <= 14:
    print("Econômico")
else:
    print("Super Econômico")

