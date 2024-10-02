opd={'clave1':(1,2,3),'clave2':(4,5,6)}

for x in range(0,3,1):
    print(f"Elemento de la {x} de la clave1 es: ", opd['clave1'][x])

for j in range(0,3,1):
    print(f"Elemento de la {j} de la clave2 es: ", opd['clave2'][j])