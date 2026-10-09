import os
armazenamento = []
while True:
    os.system('cls')
    print('====================MENU====================')
    print('1. Adicionar Manutenção Manual ')
    print('2. Adicionar Manutenção ')
    print('3. Cancelar uma manutenção')
    print('4. Concluir a manutenção')
    print('5. Retirar da posição')
    print('6. Mostrar a fila')
    print("0. Sair")
    calculo = int(input('Digite a opção desejada: '))
    match calculo:
#definimos uma variável, para podermos trabalhar com as funções da lista
     case 1:
          
          maquina = input('Digite o item na lista ').lower()     
          if maquina in armazenamento:
           print('ERRO. ESSA MAQUINA JÁ ESTÁ NA LISTA')
          else: 
            armazenamento.append(maquina)
            print(f'{maquina}, foi adicionado ao final da lista')
          os.system("pause")

     case 2: 
          maquina_urgente = input('Qual a máquina que vai ser prioridade?: ')
          if maquina_urgente in armazenamento:
              print('ERRO. ESSA MAQUINA JÁ ESTÁ NA LISTA')
          else:
              armazenamento.insert(maquina_urgente)
          os.system("pause")
          
     case 3:
          maquina_cancelada = input('Digite a máquina a ser cancelada: ')
          if maquina_cancelada in armazenamento:
              armazenamento.remove(maquina_cancelada)
          print('Manutenção cancelada')
          os.system("pause")


     case 4:
          if len(armazenamento) > 0:
           remover = armazenamento.pop(0)
           print(f'A manutenção {remover}, foi concluída')
          os.system("pause")
     case 5:
            if len(armazenamento) == 0:
                print("A fila esta vazia.")
            else:
                print("\nFila atual:")

                for i in range(len(armazenamento)):
                    print(i + 1, "-", armazenamento[i])

                posicao = int(input("Posicao que deve ser retirada: "))

                if posicao >= 1 and posicao <= len(armazenamento):
                    maquina_retirada = armazenamento.pop(posicao - 1)
                    print("Maquina retirada:", maquina_retirada)
                else:
                    print("Posicao invalida.")
            os.system('pause')

     case 6:
            if len(armazenamento) == 0:
                print("A fila esta vazia.")
            else:
                print("\nOrdem das manutencoes:")

                for i in range(len(armazenamento)):
                    print(i + 1, "-", armazenamento[i])

                print("Total de maquinas aguardando:", len(armazenamento))
            os.system('pause')

     case 0:
            print("Programa encerrado.")

     case _:
            print("Opcao invalida.")
            os.system('pause')