vent=list()
for i in range(0,5,1):
    num=int(input("Ingresa el número de ventas"))
    if (num >= 0):
        vent.append(num)
print(vent)
for x in range(0,5,1):
    if (vent[x] > 500):
        print(f"la categoría {x} tiene Ventas altas")
    elif (vent[x] >= 100 and vent[x] <= 500):
        print(f"la categoría {x} tiene Ventas moderadas")
    elif (vent[x] > 0 and vent[x] < 100):
        print(f"la categoría {x} tiene Ventas bajas")
    else:
        print("Se ingresó una cantidad incorrecta para esta cateogría")