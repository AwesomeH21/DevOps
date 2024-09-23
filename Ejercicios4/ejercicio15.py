nombres_sin_repetir = []
edades_sin_repetir = []
nombres_vistos = set()
nombres = []
edades = []

print("Ingresa 6 nombres y sus edades correspondientes:")
for i in range(6):
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    nombres.append(nombre)
    edades.append(edad)

for nombre, edad in zip(nombres, edades):
    if nombre not in nombres_vistos:
        nombres_sin_repetir.append(nombre)
        edades_sin_repetir.append(edad)
        nombres_vistos.add(nombre)

print("Listas sin nombres repetidos:")
print("Nombres:", nombres_sin_repetir)
print("Edades:", edades_sin_repetir)