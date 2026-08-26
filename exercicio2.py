from datetime import datetime
minuto = datetime.now().minute
print ("o minuto atual é "+str(minuto))
if minuto%2==0:
    print("o minuto é par")
else:
    print("o minuto é impar")