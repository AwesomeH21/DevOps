cad=input("Ingresa tu cadena: ")
with open('resultado.txt', 'w') as resultado:
    print(cad, file=resultado)