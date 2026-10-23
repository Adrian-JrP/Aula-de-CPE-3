# João Pedro Rodrigues Moreira
# Trabalho em aula, do dia 16/10/2026

tabuleiro = []

# Cria as 9 casas vazias
for i in range(9):
    tabuleiro.append(" ")

jogador = "X"
jogadas = 0

while jogadas < 9:
    # Mostra o tabuleiro
    print()
    for i in range(9):
        print(" " + tabuleiro[i] + " ", end="")

        if (i + 1) % 3 == 0:
            print()
        else:
            print("|", end="")

        if (i + 1) % 3 == 0 and i < 8:
            print("-----------")

    # Pede a jogada
    posicao = int(input(
        "Jogador " + jogador +
        ", escolha uma posição de 1 a 9: "
    ))

    # Verifica se a posição é válida
    if posicao >= 1 and posicao <= 9:

        # Verifica se a casa está vazia
        if tabuleiro[posicao - 1] == " ":
            tabuleiro[posicao - 1] = jogador
            jogadas = jogadas + 1

            # Troca o jogador
            if jogador == "X":
                jogador = "O"
            else:
                jogador = "X"
        else:
            print("Essa casa já está ocupada! Tente novamente.")
    else:
        print("Posição inválida! Escolha de 1 a 9.")

# Mostra o tabuleiro depois da última jogada
print()
for i in range(9):
    print(" " + tabuleiro[i] + " ", end="")

    if (i + 1) % 3 == 0:
        print()
    else:
        print("|", end="")

    if (i + 1) % 3 == 0 and i < 8:
        print("-----------")

print("Fim do jogo!")