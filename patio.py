import random
cn=1
numr=random.randrange(1,6)
for cn in range(1,7):
    print(f"Bala número {cn}")
    nume=int(input("Dame un número del 1 al 6: "))
    if nume<=6 and nume>=0:
        if nume==numr:
            print("bang")
            break
        else: print("La libraste")
    else: print("ingresa un número correcto")