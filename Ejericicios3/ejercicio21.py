vent=list()
y=int(1)
sum=int(0)
for i in range(0,5,1):
    num=int(input("Ingresa el número de ventas "))
    if (num >= 0):
        vent.append(num)

for x in range(0,5,1):
    if (vent[x] > 500):
        print(f"la categoría {y} tiene Ventas altas")
    elif (vent[x] >= 100 and vent[x] <= 500):
        print(f"la categoría {y} tiene Ventas moderadas")
    elif (vent[x] > 0 and vent[x] < 100):
        print(f"la categoría {y} tiene Ventas bajas")
    else:
        print("Se ingresó una cantidad incorrecta para esta cateogría")
    y=y+1
for z in range(0,5,1):
    sum=sum+vent[z]
print(f"El total de ventas fue de {sum}")