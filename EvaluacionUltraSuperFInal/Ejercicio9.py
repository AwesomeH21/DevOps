lista=[]
compa=0
max=0

for i in range(5):
    entra=int(input("Ingresa un número "))
    lista.append(entra)

for element in lista:
    if compa < element:
        max=element
        compa=element
print("El número más grande fue ",max)