lista=[1.52,1.8,1.63,1.65,1.5,1.8]
a=[1.57]
b=[1.51]
x=0
for x in lista:
    print("{:.2f}".format(x))
print(len(lista))
lista1=lista.append(a)
lista2=lista.insert(3,b)
print(lista1)
print(lista2)
x=0