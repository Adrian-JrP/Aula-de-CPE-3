from colorama import Fore, Style, init

def media_positivos(valores):
    soma = 0
    quantidade = 0
    for valor in valores:
        if valor > 0:
            soma+=valor
            quantidade+= 1


    if quantidade == 0:
        return 0
    return soma/quantidade

a=[]
while True:
    usuario = input(f'{Fore.LIGHTBLACK_EX}digite um valor ou (digite 0 pra sair) {Style.RESET_ALL}: ')
    if usuario == "0":
     input(f"{Fore.RED}.")
     input(f"{Fore.RED}..")
     input(f"{Fore.RED}...")

     input("----- saindo-----")
     break
    else:
     a.append(float(usuario))
print(f"{Fore.LIGHTBLACK_EX}A média é:",media_positivos(a))