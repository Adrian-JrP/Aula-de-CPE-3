import os
from colorama import Fore, Style, init
azazel=[]

def incluir():
 item=input("Digite o que incluir: ")
 azazel.append(item)
 print('Item incluido com sucesso!')

def apagar():
 item = input("Digite o que deseja apagar: ")
 if item in azazel:
     azazel.remove(item)
 else: 
     print(f"{Fore.RED}item não encontrado ...{Style.RESER_ALL}")

def listar():
 item = len(azazel)


     
while True:
      os.system('cls') 
      print("MENU")
      print("1. Incluir")
      print("2. Apagar")
      print("3. Listar")
      print("4. Sair")
      opcao = input("Digite a opcao desejada: ")
      match opcao:
            case "1":
                print("Vamos incluir um item" )
                return incluir

                os.system('pause')
                # Adicione aqui o código para incluir um item
            case "2":
                print("Apagar")
                # Adicione aqui o código para excluir um item
            case "3":
                print("Listar")
                os.system('pause')
                # Adicione aqui o código para listar os itens
            case "4":
                print("Saindo do programa.")
                break
            case _:
                print("Opcao invalida. Tente novamente.")
      import os

# azazel = []

# def incluir():
#     item = input("Digite o que incluir: ")
#     azazel.append(item)
#     print("Item incluído com sucesso!")

# def apagar():
#     item = input("Digite o item que deseja apagar: ")
#     if item in azazel:
#         azazel.remove(item)
#         print("Item apagado com sucesso!")
#     else:
#         print("Item não encontrado!")

# def listar():
#     print("\nLISTA DE ITENS")
#     for item in azazel:
#         print(item)

# while True:
#     os.system('cls')

#     print("MENU")
#     print("1. Incluir")
#     print("2. Apagar")
#     print("3. Listar")
#     print("4. Sair")

#     opcao = input("Digite a opção desejada: ")

#     match opcao:
#         case "1":
#             print("Vamos incluir um item")
#             incluir()
#             input("Pressione ENTER para continuar...")

#         case "2":
#             apagar()
#             input("Pressione ENTER para continuar...")

#         case "3":
#             listar()
#             input("Pressione ENTER para continuar...")

#         case "4":
#             print("Saindo do programa...")
#             break

#         case _:
#             print("Opção inválida!")
#             input("Pressione ENTER para continuar...")
