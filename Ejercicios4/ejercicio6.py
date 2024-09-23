numeros=[]

for i in range(0,10,1):
    numero = int(input("Ingrese un número"))
    numeros.append(numero)
numeros_no_rep=list(set(numeros))
print("Lista sin repetidos: ",numeros_no_rep)
