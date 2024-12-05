listauser=[]

for i in range(10):
    vapadentro = int(input("Ingresa un número a la lista: "))
    listauser.append(vapadentro)

for elemen in listauser:
    if elemen % 2 == 0:
        print(f"El número {elemen} es par")