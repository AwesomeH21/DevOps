def square(num):
    nums=num*num
    return nums


def sum_of_squares(numeros):
    lista1=[]
    for num in numeros:
        lista1.append(square(num))
    return lista1

lista=[]

for i in range(5):
    num=int(input("Dame un número para la lista: "))
    lista.append(num)

res=sum_of_squares(lista)
print("Ahí te van los cuadrados: ",res)