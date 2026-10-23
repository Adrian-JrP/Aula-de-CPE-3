# tamanho=int(input('Digite a quantidade de pessoas: '))
# espada = 1
# lista_comum = list (range(1, tamanho, +1))
# while len(lista_comum) > 1:
#     espada = (espada + 1) % len(lista_comum)
#     matou= espada % len(lista_comum, +1)
#     print('O número', espada, 'matou o número', matou)
#     lista_comum.pop(espada)
#     print(lista_comum)

tamanho = int(input('Digite a quantidade de pessoas: '))

lista_comum = list(range(1, tamanho + 1))
espada = 0

while len(lista_comum) > 1:
    espada = (espada + 1) % len(lista_comum)

    matou = lista_comum[espada]
    print('O número', matou, 'matou')

    lista_comum.pop(espada)
    print(lista_comum)

    espada = (espada - 1) % len(lista_comum) if lista_comum else 0

print('Sobrevivente:', lista_comum[0])
