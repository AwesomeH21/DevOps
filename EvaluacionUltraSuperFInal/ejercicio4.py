tupla=(6,9,10,5,8)
destupla=0.0

for elem in tupla:
    destupla=destupla+elem

prom=destupla/5

if prom >= 6:
    print("Felicidades, has aprobado con un promedio de: ",prom)
else:
    print("Ponte pilas")