opd={}

opd={'Estudiante0': [10,7,8], 'Estudiante1': [9,9,9],'Estudiante2': [8,7,9]}
acum=0
for x in range(0,3,1):
    for i in range(0,3,1):
        acum=acum+opd[f'Estudiante{x}'][i]
    prom=acum/3
    print(f"El promedio del Estudiante{x} es de: ", prom)
    prom=0
    acum=0