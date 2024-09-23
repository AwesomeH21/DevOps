palabras = []
for i in range(6):
    palabra=input("Ingresa la palabra").lower()
    palabras.append(palabra)
vocales= "aeiou"
palabras_vocales= [palabra for palabra in palabras if palabra(0) in vocales]
print("Palabras que comienzan con una vocal", palabras_vocales)