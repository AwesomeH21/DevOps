listas = []

for i in range (0,3,1):
    lista = []
    for x in range(0,3,1):
        numero = int(input(f"ingresa el número {x} de la lista {i}: "))
        lista.append(numero)
    listas.append[lista]
suma_listas=[sum(lista) for lista in listas]

print("Listas ingresadas: ", listas)
print("Listas sumadas: ", suma_listas)