import random

animales=["murcielago","mantaraya","nutria","perro","gato"]
adjetivos=["gigante","pequño","negro","amarillo","rodante"]

x=random.randrange(0,4)
y=random.randrange(0,4)

ahorcado=animales[x],adjetivos[y]

guionesa=(len(animales[x]))
guionesad=(len(adjetivos[y]))

for i in range(guionesa):print("_",end=" ")

print("  ", end=" ")

for j in range(guionesad):print("_",end=" ")

print(ahorcado)

