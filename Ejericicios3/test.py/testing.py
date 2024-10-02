
cont=0
salir=0

def primador(num):
    cont=0
    for i in range(1,num+1):
        mod=num%i
        if (mod == 0):
            cont=cont+1
    if(cont == 2):
        res=(f"Es primo {i}")
    print(res)


while salir !=1:
    cont=0
    num=int(input("Ingresa un número mayor a 100 y primo: "))
    if num > 100:
        for i in range(1,num+1):
            mod=num%i
            if (mod == 0):
                cont=cont+1
        if(cont == 2):
                salir=1

cont2=0

#Ciclo para iterar número
for x in range(1,num+1):
#Ciclo para calcular si es primo
    primador(x)


#números primos: 2,3,5,7,11,13,17,19