pala=0
for c in range(1,9,1):
    pal=float(input(f"ingresa tu calificación número {c}: "))
    pala=pala+pal
prom=pala/c
print(prom)
promres=prom // 1
print(promres)
match promres :
    case 8: print(f"Tu calificación es de {promres} ocho")
    case 9: print(f"Tu calificación es de {promres} nueve")
    case 10: print(f"Tu calificación es de {promres} diez")
    case _: print(f"Tu calificación es de {promres} No Acreditado")