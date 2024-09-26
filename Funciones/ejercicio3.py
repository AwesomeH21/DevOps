def sum_elemnents(numeros):
    tot=0
    for numero in numeros:
        tot=tot+numero
    return tot
lista=[]

for i in range(5):
    num=int(input("Ingresa un número "))
    lista.append(num)
sumer=sum_elemnents(lista)

print("La suma de todos los elementos es de: ",sumer)