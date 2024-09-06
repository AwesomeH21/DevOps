import random
numin=set()
cn=1
acc=0
numr=random.randrange(1,6)
for cn in range(1,7):
    print(f"Bala número {cn}")
    nume=int(input("Dame un número del 1 al 6: "))
    if nume in numin:
            print("No puedes ingresar un valor utilizado antes")
    else:  
        if nume>6 or nume<0:
            print("Ese número no es correcto")
        else:
            if nume==numr:
                print("bang")
                break
            else: print("La libraste")
            numin=nume
else: print("ingresa un número correcto")