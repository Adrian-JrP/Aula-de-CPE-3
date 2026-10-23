# Cláudia Jacy Barenco Abbas
# 13/10/2026
# Consulta de temperatura e direção do vento

import urllib.request
import json
from datetime import datetime
import os
import time

capitais = [
    "São Paulo (SP)",
    "Rio de Janeiro (RJ)",
    "Salvador (BA)",
    "Fortaleza (CE)",
    "Recife (PE)",
    "Florianópolis (SC)",
    "Porto Alegre (RS)"
]

# Coordenadas: latitude e longitude
coordenadas = [
    [-23.55, -46.63],
    [-22.91, -43.17],
    [-12.97, -38.51],
    [-3.71, -38.54],
    [-8.05, -34.88],
    [-27.59, -48.54],
    [-30.03, -51.23]
]

temperaturas = []
direcoes = []

# O índice representa cada direção do vento
nomes_direcoes = [
    "Norte",
    "Nordeste",
    "Leste",
    "Sudeste",
    "Sul",
    "Sudoeste",
    "Oeste",
    "Noroeste"
]

for i in range(len(capitais)):
    lat = coordenadas[i][0]
    lon = coordenadas[i][1]

    url = (
        "https://api.open-meteo.com/v1/forecast?"
        + "latitude=" + str(lat)
        + "&longitude=" + str(lon)
        + "&current=temperature_2m,wind_speed_10m,"
        + "wind_direction_10m"
    )

    resposta = urllib.request.urlopen(url)
    texto = resposta.read().decode("utf-8")
    dados = json.loads(texto)

    atual = dados["current"]

    temperatura = atual["temperature_2m"]
    velocidade = atual["wind_speed_10m"]
    graus = atual["wind_direction_10m"]

    temperaturas.append(temperatura)

    # Fórmula para converter graus em direção
    indice = int((graus + 22.5) // 45) % 8
    direcao = nomes_direcoes[indice]

    direcoes.append(direcao)

    print("\nCidade:", capitais[i])
    print("Temperatura:", temperatura, "°C")
    print("Velocidade do vento:", velocidade, "km/h")
    print("Direção do vento:", graus, "graus -", direcao)

    time.sleep(1)

print("\n--- RELATÓRIO METEOROLÓGICO ---")
print("Data e hora:", datetime.now())

if len(temperaturas) > 0:
    media = sum(temperaturas) / len(temperaturas)
    temp_max = max(temperaturas)
    temp_min = min(temperaturas)

    posicao_max = temperaturas.index(temp_max)
    posicao_min = temperaturas.index(temp_min)

    print("\n--- ANÁLISE DOS DADOS ---")
    print("Média das temperaturas:", round(media, 2), "°C")
    print("Mais quente:", capitais[posicao_max],
          "com", temp_max, "°C")
    print("Mais fria:", capitais[posicao_min],
          "com", temp_min, "°C")