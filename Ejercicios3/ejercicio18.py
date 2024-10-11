contcal=[0,0,0,0,0]
contcale=int(0)
for i in range(0, 5, 1):
    cal=int(input("Ingresa un valor "))
    contcal[i]=+cal
for i in range (0,5,1):
    contcale=contcal[i]+contcale
prom=contcale/5
print("Tu promedio es: ",prom)

if (prom >= 70):
    print("Estás acreditado")
else:
    print("No estás acreditado")
