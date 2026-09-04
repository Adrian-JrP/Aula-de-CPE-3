import sys
num = int(input("um número de 6 algarismos: "))
print (num)
if (num< 99999 or num>999999):
    print("O número não tem 6 dígitos")
    sys.exit()
d1=num//100000
print(d1)
r1=d1%10000

d2=num//10000
print(d2)
r2=r1%1000

d3=num//1000
print(d3)
r3=r2%1000

d4=num//100
print(d4)
r4=r3%100

d5=num//10
print(d5)
r5=r4%10

d6=num//10
print(d6)
r6=r5%1

