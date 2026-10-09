equipamento = []
for i in range(4):
    nome = int(input('Digite um número: '))
    equipamento.append(nome)
print('\n --------------', equipamento, '--------------')
for nome in equipamento[:]:
    if nome != 22 and nome !=13:
     equipamento.remove(nome)
print('\n os canditados mais votados foram:', equipamento)

vencedor=int(input('\nDigite o melhor qual ganhou a eleição: '))
if vencedor==22:
 print('\nO presidene do Brasil é: ', equipamento[0])
else:
   equipamento[13,22]
print('Pro canditado número', equipamento[1], 'uma boa sorte na próxima eleição') 