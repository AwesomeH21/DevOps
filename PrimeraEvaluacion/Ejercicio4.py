Estudiante1=83
Estudiante2=70
Estudiante3=92
Estudiante4=100
Estudiante5=30
Estudiante6=61

Estudiantes=[Estudiante1,Estudiante2,Estudiante3,Estudiante4,Estudiante5,Estudiante6]
cont = 0
for stud in Estudiantes:
    cont=cont+1
    if (stud > 91):
        print(f"El estudiante {cont} es de tipo A")
    elif (stud > 81):
        print(f"El estudiante {cont} es de tipo B")
    elif (stud > 71):
        print(f"El estudiante {cont} es de tipo C")
    elif (stud > 61):
        print(f"El estudiante {cont} es de tipo D")
    elif (stud > 42):
        print(f"El estudiante {cont} es de tipo E")
    elif (stud <= 41):
        print(f"El estudiante {cont} es de tipo F")