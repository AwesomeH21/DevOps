import random


def checker(self,pelou, generou, arreglou):
    if generou in arreglou and pelou in arreglou:
        return "has escogido bien"
    elif generou in arreglou:
        return "El género está bien"
    elif pelou in arreglou:
        return "El pelo está bien"
    else:
        return "Nada está correcto"

x=""

personaje = []

personas = ["Anita", "Diego", "Isabel", "Santiago", "Adriana", "Carlos"]

categorias = {
    "mujer": ["Anita", "Isabel", "Adriana"],
    "hombre": ["Diego", "Santiago", "Carlos"],
    "largo": ["Anita", "Isabel", "Carlos"],
    "corto": ["Diego", "Santiago", "Adriana"]
}

selecc = random.choice(personas)

for categoria, lista_personas in categorias.items():
    if selecc in lista_personas:
        personaje.append(categoria)


gen=input("Género del personaje: ").lower()
pel=input("Pelo del personaje: ").lower()

x=checker(checker, pel, gen, personaje)

print(x)

while x != "has escogido bien":
    if x=="El género está bien":
        pel=input("Pelo del personaje: ").lower()
    elif x=="El pelo está bien":
        gen=input("Género del personaje: ").lower()

    else:
        gen=input("Género del personaje: ").lower()
        pel=input("Pelo del personaje: ").lower()
    x=checker(checker, pel, gen, personaje)
    print(x)

name=input("Cómo se llama el persona?: ")

if selecc == name:
    print("Es correcto, has ganado")
else:
    print("Perdiste, vuelve a intentarlo")
