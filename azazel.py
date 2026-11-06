import os
from colorama import Fore, Style, init
azazel=[]

def incluir():
 item=input("Digite o que incluir: ")
 azazel.append(item)
 print(f"{Fore.LIGHTBLUE_EX}\n------------------------\n{Style.RESET_ALL}")
 print(f'{Fore.LIGHTBLUE_EX}Item incluido com sucesso!\n{Style.RESET_ALL}')

def apagar():
 item = input(f"{Fore.LIGHTBLUE_EX}Digite o que deseja apagar: {Style.RESET_ALL}")
 if item in azazel:
     azazel.remove(item)
 else: 
     print(f"{Fore.RED}-----------------------\n item não encontrado \n-----------------------{Style.RESET_ALL}")

def listar():
 print(f"{Fore.LIGHTBLUE_EX}Itens na lista:")
 for item in azazel:
     print(f"- {item}")



while True:
      os.system('cls') 
      print(f"{Fore.LIGHTBLUE_EX}-------MENU-------{Style.RESET_ALL}")
      print(f"{Fore.LIGHTBLUE_EX}1. Incluir{Style.RESET_ALL}")
      print(f"{Fore.LIGHTBLUE_EX}2. Apagar{Style.RESET_ALL}")
      print(f"{Fore.LIGHTBLUE_EX}3. Listar{Style.RESET_ALL}")
      print(f"{Fore.LIGHTBLUE_EX}4. Sair{Style.RESET_ALL}")
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
                print(f"{Fore.RED}Saindo do programa.{Style.RESET_ALL}")
                break
            case _:
                print("Opcao invalida. Tente novamente.")
      import os
