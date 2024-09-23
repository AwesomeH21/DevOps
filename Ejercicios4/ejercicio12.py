
lista_principal=[]
listain=[]

print("Ingresa 3 listas, cada una con 4 números enteros:")
for i in range(3):
    print(f"\nIngresa los 4 números para la lista {i}:")
    lista = [int(input(f"Número {j}: ")) for j in range(4)]
    lista_principal.append(lista)

listamain=int(input("Ingresa el número de lista que deseas abrir "))
listainn=int(input("Ingresa la ubicación de la lista que deseas abrir "))

selecc=lista_principal[listamain][listainn]

print("El número que has escogido es el: ",selecc)