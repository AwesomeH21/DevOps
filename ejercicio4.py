num=int(input("Ingresa una temperatura "))
if num > 30 :
    print("Caluroso")
elif num <= 30 and num >= 16 :
    print("Cálido")
elif num <= 15 and num >= 0 :
    print("frío")
elif num < 0 :
    print("muy frío")
else :
    print("No sé como llegaste aquí ")