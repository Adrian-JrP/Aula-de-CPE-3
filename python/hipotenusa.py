def hipotenusa(cateto1:float, cateto2:float) -> float:
    return (cateto1**2 + cateto2**2)**0.5
cateto1 = float(input(f"digite o valor do primeiro cateto: "))
cateto2 = float(input("digite o valor do seundo cateto: "))
print(hipotenusa(cateto1, cateto2))