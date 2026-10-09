equipamentos = []
print('======TESTES DE EQUIPAMENTOS======')
for i in range(4):
        nome = input("Digite o nome do equipamento: ")
        equipamentos.append(nome)
equipamento_urgente=input('digite o equipamento URGENTE: ')
equipamentos.insert(0, equipamento_urgente)
print(equipamentos)
equipamento_cancelado=input('Digite o equipamento retirado da lista: ')
equipamentos.remove(equipamento_cancelado)
print(equipamentos)
equipamento_testado=print('O equipamento sendo testado atualmente é:', equipamento_cancelado )
equipamento_restante=print('equipamento restante é: ', equipamentos )
