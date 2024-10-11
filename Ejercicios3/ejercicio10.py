cad=input("Ingresa tu string: ")
cadm=cad.upper()
cadr=cadm.replace("A","*").replace("E","*").replace("I","*").replace("O","*").replace("U","*")
cadll=cadr.count("*")
print(cadr)
print(cadll)
if cadll >= 1:
    print("Se reemplazó una vocal o más")
else:
    print("No se reemplazó nada")