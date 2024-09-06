num=int(input("Ingresa un número del 0 al 100 "))
if num <= 100 and num >= 90 :
    print("Calificación A")
elif num <= 89 and num >= 80 :
    print("calificación B")
elif num <= 79 and num >= 70 :
    print("calificación C")
elif num <= 69 and num >= 60 :
    print("calificación D")
elif num < 60 :
    print("calificación F")
else :
    print("Ingresa un número correcto ")
