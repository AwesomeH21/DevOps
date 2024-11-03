import random

peliculas=["terminator","mean girls","star wars","et","harry potter"]
peliculasfra={"terminator": "Hasta la vista, baby", "mean girls":"Why are you so obssesed with me?", "star wars":"No, yo soy tu padre", "et":" E.T go home", "harry potter":"Asustado potter?"}

selecc=random.choice(peliculas)


print("La frase es: ", peliculasfra[selecc])

elecc=input("¿Qué película es?: ").lower()

if elecc == selecc:
    print("Es correcto, felicitaciones")
else:
    print("No es correcto, la respuesta correcta era: ", selecc)

