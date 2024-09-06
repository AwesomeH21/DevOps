#hecho por: Napoleon
elecc="S"
user="DiegoRosga"
pasw="2023371025"
while elecc=="S":
    useri=input("Ingresa tu usuario")
    if useri ==user:
        while useri == user:
            paswi=input("Ahora ingresa tu contraseña")
            if paswi==pasw:
                print("contraseña correcta, iniciando sesión...")
                elecc=""
                useri=""
            else: print("contraseña incorrecta...")
            elecc=""
            useri=""
print("Saliendo del sistema...")