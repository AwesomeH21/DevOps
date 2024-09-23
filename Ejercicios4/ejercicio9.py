listas = []

for i in range (0,3,1):
    lista = []
    for x in range(0,4,1):
        numero = int(input(f"ingresa el número {x} de la lista {i}: "))
        lista.append(numero)
    listas.append[lista]

for lista in listas:
    lista[:] = [numero for numero in lista if numero <= 50]
print("Listas con números menores o iguales a 50: ",listas)