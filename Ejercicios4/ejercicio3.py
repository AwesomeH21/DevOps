nums=[]

for i in range (0,8,1):
    num=int(input("Ingresa un número"))
    nums.append(num)
nums.sort()
print("Lista invertida",nums[::-1])