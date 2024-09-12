num=int(input("Ingresa un número entero "))
cad=input("Ingresa un string ")

cadc=len(cad)
countr=cadc%2

if num >= 0 and countr == 0:
    print("Se cumplió la condición")
else:
    print("Pues no se cumplió la condición")