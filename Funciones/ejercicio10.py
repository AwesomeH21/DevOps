def double_values(nums):
    neu=[]
    for num in nums:
        nume=num*2
        neu.append(nume)
    return neu

lista=[]
for i in range(5):
    num=int(input("Ingresa un número para la lista: "))
    lista.append(num)

nuevo=double_values(lista)
print("Ahí te va un duplicado: ",nuevo)