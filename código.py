# TAREFA DE CASA 02 - CPE 
# Análise de Similaridade Vetorial de Palavras em 3D
# Nome: João Pedro Rodrigues moreira
# Matrícula:262017229

# Importa a biblioteca math para usar a raiz quadrada
import math

# FASE 1 - PROCESSAMENTO DA PALAVRA DE REFERÊNCIA

print("=== FASE 1: PROCESSAMENTO DE SIMILARIDADE VETORIAL 3D ===")

# Solicita a palavra de referência
referencia = input("Digite a palavra de referencia: ")

# Começamos as contagens 
a1 = 0
a2 = 0
a3 = 0

# Percorre cada letra da palavra de referência
for letra in referencia.lower():

    # Verifica se a letra é uma vogal
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        a1 = a1 + 1

    # Verifica se a letra é uma consoante
    elif letra >= "a" and letra <= "z":
        a2 = a2 + 1

    # Verifica se a letra está entre 'a' e 'm'
    if letra >= "a" and letra <= "m":
        a3 = a3 + 1


# Calcula a norma da palavra de referência
norma_A = math.sqrt(a1 * a1 + a2 * a2 + a3 * a3)

print()
print("[Vetor Referencia '" + referencia + "']: Vogais:", a1,
      "| Consoantes:", a2,
      "| Letras A-M:", a3,
      "| Norma 3D:", format(norma_A, ".4f"))

print()


# Variável que vai guardar a soma das distâncias
soma_distancias = 0

# PROCESSAMENTO DAS 10 PALAVRAS

for i in range(10):

    print("Palavra", i + 1, "/10")

    # Solicita a palavra que será analisada
    palavra = input("Digite a palavra: ")

    # Começamos as contagens da palavra com zero
    b1 = 0
    b2 = 0
    b3 = 0

    # Percorre cada letra da palavra
    for letra in palavra.lower():

        # Conta as vogais
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
            b1 = b1 + 1

        # Conta as consoantes
        elif letra >= "a" and letra <= "z":
            b2 = b2 + 1

        # Conta as letras de 'a' até 'm'
        if letra >= "a" and letra <= "m":
            b3 = b3 + 1

    # Cálculo do produto escalar

    produto_escalar = (a1 * b1) + (a2 * b2) + (a3 * b3)

    # Cálculo da norma da palavra analisada

    norma_B = math.sqrt(b1 * b1 + b2 * b2 + b3 * b3)

    # Cálculo da similaridade de cosseno

    if norma_A * norma_B > 0:
        similaridade = produto_escalar / (norma_A * norma_B)
    else:
        similaridade = 0.0

    # Cálculo da distância de cosseno

    distancia = 1.0 - similaridade

    # Guarda a distância para calcular a média depois
    soma_distancias = soma_distancias + distancia

    # Classificação da palavra

    if distancia >= 0.95:
        classificacao = "Alta Similaridade"

    elif distancia >= 0.80:
        classificacao = "Media Similaridade"

    else:
        classificacao = "Baixa Similaridade"

    # Mostra os resultados da palavra

    print("Vetor 3D:", (b1, b2, b3),
          "| Similaridade:", format(similaridade, ".4f"),
          "(", format(similaridade * 100, ".2f"), "%)",
          "| Distancia:", format(distancia, ".4f"))

    print("Classificacao:", classificacao)
    print()

# FASE 2 - RELATÓRIO DO PROCESSAMENTO

print("=== FASE 2: RELATORIO DO PROCESSAMENTO ===")

print("Processamento Concluido com Sucesso!")

print("Referencia '" + referencia + "' -> Vetor 3D:",
      (a1, a2, a3))

# Calcula a média das 10 distâncias

media_distancia = soma_distancias / 10

print("Media de Distancia de Cosseno:",
      format(media_distancia, ".4f"),
      "(", format(media_distancia * 100, ".2f"), "%)")

print()

# FASE 3 - DIAGNÓSTICO DE NOVAS PALAVRAS

print("=== FASE 3: DIAGNOSTICO DE NOVA PALAVRA (INFERENCIA 3D) ===")

# O programa continua até o usuário digitar PARAR
while True:

    palavra_nova = input("Digite a nova palavra para teste (PARAR para sair): ")

    # Verifica se o usuário quer encerrar
    if palavra_nova == "PARAR":
        break

    # Vetorização da nova palavra

    b1_novo = 0
    b2_novo = 0
    b3_novo = 0

    # Percorre cada letra da nova palavra
    for letra in palavra_nova.lower():

        # Conta as vogais
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
            b1_novo = b1_novo + 1

        # Conta as consoantes
        elif letra >= "a" and letra <= "z":
            b2_novo = b2_novo + 1

        # Conta as letras entre 'a' e 'm'
        if letra >= "a" and letra <= "m":
            b3_novo = b3_novo + 1

    # Produto escalar da nova palavra

    produto_escalar_novo = (a1 * b1_novo) + (a2 * b2_novo) + (a3 * b3_novo)

    # Norma da nova palavra

    norma_novo = math.sqrt(
        b1_novo * b1_novo +
        b2_novo * b2_novo +
        b3_novo * b3_novo
    )

    # Similaridade de cosseno da nova palavra

    if norma_A * norma_novo > 0:
        similaridade_nova = produto_escalar_novo / (norma_A * norma_novo)
    else:
        similaridade_nova = 0.0

    # Distância de cosseno da nova palavra

    distancia_nova = 1.0 - similaridade_nova

    # Diagnóstico

    if distancia_nova >= 0.95:
        diagnostico = "Alta Similaridade"

    elif distancia_nova >= 0.80:
        diagnostico = "Media Similaridade"

    else:
        diagnostico = "Baixa Similaridade"

    # Exibe os resultados

    print("Vetor Novo 3D:", (b1_novo, b2_novo, b3_novo))

    print("Similaridade Estimada:",
          format(similaridade_nova, ".4f"),
          "(", format(similaridade_nova * 100, ".2f"), "%)",
          "| Distancia:", format(distancia_nova, ".4f"))

    print("[DIAGNOSTICO]:", diagnostico)
    print()


print("Programa encerrado!")

