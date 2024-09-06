num=int(input("Ingresa un número del 0 al 100 "))
if num <= 100 and num >= 90 :
    print("Calificación A")
else: 
    if num <= 89 and num >= 80 :
        print("calificación B")
    else:
        if num <= 79 and num >= 70 :
            print("calificación C")
        else:
            if num <= 69 and num >= 60 :
                print("calificación D")
            else:
                if num < 60 and num > 0 :
                    print("calificación F")
                else :
                    print("Ingresa un número correcto ")