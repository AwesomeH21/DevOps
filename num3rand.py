#hecho por: Napoleon
import random
numr=random.randrange(1,30)
print(f"{numr} número aleatorio")
x=1
numl=0
while x<numr:
    x=x+1
    numrd=x%3
    if numrd==0:
        print(x)