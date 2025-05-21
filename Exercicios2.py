# Prática 2

# 1 - Conversor de Moeda 

def currency_converter():
    reais = float(input("Digite o valor em reais: R$ "))
    taxa_dolar = float(input("Digite a taxa do dólar: R$ "))
    taxa_euro = float(input("Digite a taxa do euro: R$ "))

    usd = reais / taxa_dolar
    eur = reais / taxa_euro

    print("\n=== Conversor de Moeda ===")
    print(f"Valor em Reais : R$ {reais:.2f}")
    print(f"Taxa do Dólar  : R$ {taxa_dolar:.2f}")
    print(f"Taxa do Euro   : R$ {taxa_euro:.2f}")
    print(f"Convertido para Dólares: US$ {usd:.2f}")
    print(f"Convertido para Euros  : € {eur:.2f}\n")


# 2 - Calculadora de Desconto 

def discount_calculator():
    nome_produto = input("Digite o nome do produto: ")
    preco_original = float(input("Digite o preço original do produto: R$ "))
    percentual_desconto = float(input("Digite o percentual de desconto (%): "))

    valor_desconto = preco_original * percentual_desconto / 100
    preco_final = preco_original - valor_desconto

    print("\n=== Calculadora de Desconto ===")
    print(f"Produto              : {nome_produto}")
    print(f"Preço original       : R$ {preco_original:.2f}")
    print(f"Percentual de desconto: {percentual_desconto}%")
    print(f"Valor do desconto    : R$ {valor_desconto:.2f}")
    print(f"Preço final          : R$ {preco_final:.2f}\n")


# 3 - Calculadora de Média Escolar 

def calcular_media_escolar():
    notas = []
    for i in range(1, 4):
        nota = float(input(f"Digite a nota {i}: "))
        notas.append(nota)

    media = sum(notas) / len(notas)

    print("\n=== Calculadora de Média Escolar ===")
    for i, nota in enumerate(notas, 1):
        print(f"Nota {i}: {nota:.2f}")
    print(f"Média final: {media:.2f}\n")


# 4 - Calculadora de Consumo de Combustível 

def calcular_consumo_combustivel():
    distancia_km = float(input("Digite a distância percorrida (km): "))
    combustivel_litros = float(input("Digite o combustível gasto (litros): "))

    consumo_medio = distancia_km / combustivel_litros

    print("\n=== Calculadora de Consumo de Combustível ===")
    print(f"Distância percorrida : {distancia_km} km")
    print(f"Combustível gasto     : {combustivel_litros} litros")
    print(f"Consumo médio         : {consumo_medio:.2f} km/l\n")


if __name__ == "__main__":
    currency_converter()
    discount_calculator()
    calcular_media_escolar()
    calcular_consumo_combustivel()