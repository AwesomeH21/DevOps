import random
num1=random.randint(2,7)
acum=1
print(f"factorial de: {num1}")
for i in range(1,num1+1,1):
    acum=acum*i
print(acum)