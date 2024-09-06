x=1
cont=0
while x != 0 :
    x=int(input("Ingresa un número "))
    if x > 10:
        cont=cont+1
print(f"ingresaste {cont} números mayores a 10")