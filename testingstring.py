hola=input("Ingresa un string: ")
helou=""

holador=[]
hola=hola.strip("!")

for elements in hola:
    if elements !=  " ":
        holador.append(elements)

for letras in holador:
    helou=helou+letras

print(holador)
print(helou)