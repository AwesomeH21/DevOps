print("Ingresa 5 números para la primera lista:")
lista1 = [int(input(f"Número {i+1}: ")) for i in range(5)]

print("Ingresa 5 números para la segunda lista:")
lista2 = [int(input(f"Número {i+1}: ")) for i in range(5)]

lista_intercalada = [None]*(len(lista1) + len(lista2))

for i, (num1, num2) in enumerate(zip(lista1, lista2)):
    lista_intercalada[2*i] = num1  
    lista_intercalada[2*i + 1] = num2 
print("lista intercalada", lista_intercalada)
