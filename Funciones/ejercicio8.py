def sum_numbers(nums):
    tot=0
    for num in nums:
        tot=tot+num
    return tot
lista=[]
yes="NO"
while yes=="NO":
    num=int(input("Ingresa un número "))
    lista.append(num)
    yes=input("deseas salir? si/no").upper()

suma=sum_numbers(lista)
print("La suma total fue de ", suma)