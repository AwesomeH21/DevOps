lista1=[]
lista2=[]

for i in range(5):
    numero=int(input("Ingresa un número para la lista 1"))
    lista1.append(numero)
for i in range(5):
    numero=int(input("Ingresa un número para la lista 2"))
    lista2.append(numero)
suma=[lista1[i]+lista2[i] for i in range(5)]
resta=[lista1[i]-lista2[i] for i in range(5)]
print("Las listas sumadas da: ",suma)
print("Las listas restadas da: ",resta)