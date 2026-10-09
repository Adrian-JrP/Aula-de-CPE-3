import random
import sys

# 1. Lista de palavras para o jogo
palavras = input('Digite uma palavra')

# 2. Sorteia uma palavra da lista aleatoriamente
palavra_secreta = random.choice(palavras)

# 3. Cria a lista de lacunas baseada no tamanho da palavra sorteada
adivinha = ["_"] * len(palavra_secreta)

print("Bem-vindo ao jogo da Forca!")
print(" ".join(adivinha))  # Mostra as lacunas separadas por espaço

# 4. Loop principal do jogo
while True:
    letra = str(input("\nDigite uma letra: ")).lower()

    # Verifica se a letra está na palavra secreta
    for i in range(len(palavra_secreta)):
        if letra == palavra_secreta[i]:
            adivinha[i] = letra  # Substitui o "_" pela letra correta na posição exata

    # Mostra o progresso atual do jogador
    print(" ".join(adivinha))

    # Verifica se o jogador completou a palavra
    if "_" not in adivinha:
        print("\nParabéns, você acertou!")
        sys.exit()