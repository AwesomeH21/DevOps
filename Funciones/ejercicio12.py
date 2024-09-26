def concatenate_strings(lista):
    cadena=""
    for elemento in lista:
        cadena=cadena+elemento
    return cadena
lista=[]
for i in range(5):
    cad=input("Métale su cadena ")
    lista.append(cad)

print(concatenate_strings(lista))