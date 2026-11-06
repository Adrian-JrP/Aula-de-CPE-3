# import os
# from colorama import Fore, Style, init
# azazel=[]

# def incluir():
#  item=input("Digite o que incluir: ")
#  quantidade=input("Digite a quantidade de itens:")
#  preco=input("coloque o preço: ")
#  produto = {"item": item, "quantidade": quantidade, "preco": preco}
#  azazel.append(produto)
#  #print("Item:", item, "Quatidade restante:", quantidade, "Valor R$:", preco)
#  print(f"{Fore.LIGHTBLUE_EX}\n------------------------\n{Style.RESET_ALL}")
#  print(f'{Fore.LIGHTBLUE_EX}Item incluido com sucesso!\n{Style.RESET_ALL}')

# def apagar():
#  item = input(f"{Fore.LIGHTBLUE_EX}Digite o que deseja apagar: {Style.RESET_ALL}")
#  if item in azazel:
#      azazel.remove(item)
#  else: 
#      print(f"{Fore.RED}-----------------------\n item não encontrado \n-----------------------{Style.RESET_ALL}")

# # def listar():
# #  print(f"{Fore.LIGHTBLUE_EX}Itens na lista:")
# #  for item in azazel:
# #    print(f"{item}|")
# #  quantidade in azazel:
# #    print(f"{quantidade}|")
     
# #    preco in azazel:
# #    print(f"{preco}")
# def listar():
#   print(f"{Fore.LIGHTBLUE_EX}Itens na lista:")
#   for item, quantidade, preco in azazel:
#     print(f"{item} | {quantidade} | {preco}")
import sys
import os
from colorama import Fore, Style, init

azazel = []


def incluir():
  item = input("Digite o que incluir: ")
  quantidade = input("Digite a quantidade de itens: ")
  preco = input("coloque o preço: ")

  # Mantém o seu método de adicionar um elemento atrás do outro
  azazel.append(item)
  azazel.append(quantidade)
  azazel.append(preco)

  print(f"{Fore.LIGHTBLUE_EX}\n------------------------\n{Style.RESET_ALL}")
  print(f"{Fore.LIGHTBLUE_EX}Item incluido com sucesso!\n{Style.RESET_ALL}")


def apagar():
  item = input(
      f"{Fore.LIGHTBLUE_EX}Digite o que deseja apagar: {Style.RESET_ALL}"
  )

  if item in azazel:
    # Como os itens estão em sequência (item, quantidade, preço),
    # descobrimos a posição do nome para apagar ele e os dois valores que vêm logo depois.
    indice = azazel.index(item)
    azazel.pop(indice + 2)  # Apaga o preço
    azazel.pop(indice + 1)  # Apaga a quantidade
    azazel.pop(indice)  # Apaga o nome do item
    print(
        f"{Fore.GREEN}-----------------------\n Item removido com sucesso!"
        f" \n-----------------------{Style.RESET_ALL}"
    )
  else:
    print(
        f"{Fore.RED}-----------------------\n item não encontrado"
        f" \n-----------------------{Style.RESET_ALL}"
    )


def listar():
  print(f"{Fore.LIGHTBLUE_EX}Itens na lista:{Style.RESET_ALL}")

  # Para ler uma lista linear de 3 em 3 elementos, usamos o 'range' pulando de 3 em 3 steps.
  for i in range(0, len(azazel), 3):
    item = azazel[i]
    quantidade = azazel[i + 1]
    preco = azazel[i + 2]
    print(f"{item} | Quantidade:{quantidade} | R$:{preco}")

def modificar():
  print(f"{Fore.LIGHTBLUE_EX}Itens na lista:{Style.RESET_ALL}")
  item = input("Qual você deseja modificar?: ")

  if item in azazel:
    indice = azazel.index(item)

    # Apaga os 3 dados antigos (Nome, Quantidade, Preço)
    azazel.pop(indice)
    azazel.pop(indice)
    azazel.pop(indice)

    # Além do novo nome, pede os novos dados para preencher o buraco dos que foram apagados
    item_novo = input("Quer modificar pelo que?: ")
    quantidade_nova = input("Digite a nova quantidade: ")
    preco_novo = input("Digite o novo preço: ")

    # Insere de trás para frente na mesma posição para manter a ordem certa
    azazel.insert(indice, preco_novo)
    azazel.insert(indice, quantidade_nova)
    azazel.insert(indice, item_novo)

    print(f"{Fore.GREEN}Item modificado com sucesso!{Style.RESET_ALL}")
  else:
    print(f"{Fore.RED}Item não encontrado na lista.{Style.RESET_ALL}")




os.system("Pause")
while True:
      os.system('cls') 
      print(f"{Fore.LIGHTBLUE_EX}-------MENU-------{Style.RESET_ALL}")
      print(f"{Fore.LIGHTBLUE_EX}1. Incluir{Style.RESET_ALL}")
      print(f"{Fore.LIGHTBLUE_EX}2. Apagar{Style.RESET_ALL}")
      print(f"{Fore.LIGHTBLUE_EX}3. Listar{Style.RESET_ALL}")
      print(f"{Fore.LIGHTBLUE_EX}4. modificar{Style.RESET_ALL}")
      print(f"{Fore.LIGHTBLUE_EX}5. sair{Style.RESET_ALL}")
      opcao = input(f"{Fore.LIGHTBLACK_EX}\nDigite a opcao desejada: {Style.RESET_ALL}")
      match opcao:
            case "1":
                print(f"{Fore.LIGHTBLUE_EX}------------------------\nVamos incluir um item\n------------------------{Style.RESET_ALL}")
                incluir()
                os.system('pause')
                # Adicione aqui o código para incluir um item------------------>
            case "2":
                print(f"{Fore.LIGHTBLUE_EX}------------------------\nApagar\n------------------------{Style.RESET_ALL}")
                apagar()
                os.system('pause')
                # Adicione aqui o código para excluir um item----------------->
            case "3":
                print(f"{Fore.LIGHTBLUE_EX}------------------------\nListando itens...\n------------------------{Style.RESET_ALL}")
                listar()
                os.system('pause')
                # Adicione aqui o código para listar os itens----------------->
            case "4":
                print(f"{Fore.LIGHTBLUE_EX}------------------------\nModificando...\n------------------------{Style.RESET_ALL}")
                modificar()
                os.system('pause')
                # Adicione aqui o código para listar os itens----------------->
            case "5":
                print(f"{Fore.RED}Saindo do programa.{Style.RESET_ALL}")
                break
            case _:
                print("Opcao invalida. Tente novamente.")
      import os