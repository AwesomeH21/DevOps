palabras = []

for i in range(0,10,1):
    palabra = input("Ingresa una palabra: ")
    palabras.append(palabra)
palabra_buscada=input("Ingresa la palabra que deseas buscar: ")
ocurrencias=palabras.count(palabra_buscada)

print(f"La palabra {palabra_buscada} apareció: ",ocurrencias," veces ")