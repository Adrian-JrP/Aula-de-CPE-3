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
    calculo = input('Digite a opção desejada: ')
    match calculo:
#definimos uma variável, para podermos trabalhar com as funções da lista
     case "1":
          
          maquina = input('Digite o item na lista ')
          if maquina in armazenamento:
           print('ERRO. ESSA MAQUINA JÁ ESTÁ NA LISTA')
          else: 
            armazenamento.append(maquina)
            print(f'A maquina {maquina}, foi adicionado ao final da lista')
          os.system("pause")

     case "2": 
          maquina_urgente = input('Qual a máquina que vai ser prioridade?: ')
          if maquina_urgente in armazenamento:
              print('ERRO. ESSA MAQUINA JÁ ESTÁ NA LISTA')
          else:
              armazenamento.insert(maquina_urgente)
          os.system("pause")
          
     case "3":
          maquina_cancelada = input('Digite a máquina a ser cancelada: ')
          if maquina_cancelada in armazenamento:
              armazenamento.remove(maquina_cancelada)
          print('Manutenção cancelada')
          os.system("pause")


     case "4":
          if len(armazenamento) > 0:
           remover = armazenamento.pop(0)
           print(f'A manutenção {remover}, foi concluída')
          os.system("pause")


     case "5":
            if len(armazenamento) == 0:
                print('A fila de manutenção está vazia.')
            else:
                try:
                    posicao = int(input('Digite a posição que deseja retirar: '))
                    if 0 <= posicao < len(armazenamento):
                        removida = armazenamento.pop(posicao)
                        print(f'Máquina "{removida}" retirada da posição {posicao}.')
                    else:
                        print('Erro: Posição inválida!')
                except ValueError:
                    print('Erro: Digite um número inteiro válido.')
            os.system('pause')

     case "6":
            print('\n--- FILA DE MANUTENÇÃO ---')
            if len(armazenamento) == 0:
                print('A fila está vazia.')
            else:
                for idx, maquina in enumerate(armazenamento):
                    print(f'Posição {idx}: {maquina}')
            print('--------------------------')
            os.system('pause')

     case "0":
            print('Encerrando o programa...')
            break

     case _:
            print('Opção inválida!')
            os.system('pause')