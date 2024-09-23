lista1=[]
lista2=[]

for i in range(0,5,1):
    numero1=int(input("Ingresa un número para la primera lista: "))
    lista1.append(numero1)
    numero2=int(input("Ingresa un número para la segunda lista: "))
    lista2.append(numero2)
listas_ordenadas=sorted(zip(lista1,lista2))

lista1_ordenada, lista2_ordenada = zip(*listas_ordenadas)

print("Pimera lista ordenada: ", lista1_ordenada)
print("Segunda lista ordenada según la primera: ", lista2_ordenada)