def filter_even_numbers(numeros):
    filt=[]
    for numero in numeros:
        if (numero%2 == 0):
            filt.append(numero)
    return filt
lista=[]
for i in range(5):
    num=int(input("Dame un número: "))
    lista.append(num)

print("Números pares de tu lista ",filter_even_numbers(lista))