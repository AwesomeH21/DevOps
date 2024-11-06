import random

letrause=[]
pala=[]
comparador=[]

cont=0

animales=["murcielago","mantaraya","nutria","perro","gato"]
adjetivos=["gigante","pequeño","negro","amarillo","rodante"]

x=random.randrange(0,4)
y=random.randrange(0,4)

ahorcado=animales[x],adjetivos[y]

guionesa=(len(animales[x]))
guionesad=(len(adjetivos[y]))



for i in range(guionesa):print("_",end=" ")

print("  ", end=" ")

for j in range(guionesad):print("_",end=" ")

for elem in animales[x]:pala.append(elem)

for elem in adjetivos[y]:pala.append(elem)


while cont <= 5:

    letr=input("Ingresa una letra: ")
    letrause.append(letr)
    if letr in pala:
        print("Esa letra si está")
    else:
        print("Esa letra no está")
    for elem in animales[x]:
        if elem in letrause:
            print(elem, end="")
        else:
            print("_",end=" ")
    print(" ", end="")
    for elems in adjetivos[y]:
        if elems in letrause:
            print(elems, end="")
        else:
            print("_",end=" ")

    seleccion=input("Deseas ingresar la palabra que crees que sea?: S/N")
    seleccion=seleccion.upper()
    if seleccion == "S":
        palabrotaa=input("Ingresa el animal que crees que sea:")
        palabrotas=input("Ingresa el adjetivo crees que sea:")

        palabrota=palabrotaa+palabrotas
        for l in palabrota:
            comparador.append(l)
        

        if comparador == pala:
            print("Si, esa era la palabra!")
            cont=1000
        else:
            print("Esa no era mijo")
    cont=cont+1
