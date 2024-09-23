pals=[]
for i in range(6):
    pal=input("Ingresa una palabra ")
    palc=len(pal)
    if (i == 0):
        maximus=palc
    if (palc >= maximus):
        pals.append(pal)
print("Palabras filtradas: ",pals)