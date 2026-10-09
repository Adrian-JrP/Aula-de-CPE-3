import os
import sys
palavra=str(input("Digite a palavra a ser adivinhada: "))
palavra=palavra.lower()
os.system("cls")
adivinha=["_"]*len(palavra)
print(adivinha)
while True:
    letra=str(input("Digite uma letra "))
    letra=letra.lower()
    for l in range(0, len(palavra)):
        if letra == palavra[l]:
            # 2. TRANSFORMAÇÃO: Altera o elemento da lista diretamente pelo índice
            adivinha[l] = letra
            
            print(" ".join(adivinha))
    if "_" not in adivinha:
      print("Parabens voce acertou!")
      sys.exit()
    