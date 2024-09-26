def create_profile(name,age=18,country="Unknown"):
    print(f"El perfil de {name} fue creado en el país {country} y tiene una edad de {age}")
nomb=input("Ingresa tu nombre ")
edad=int(input("Ingresa tu edad "))
pais=input("Ingresa tu país ")

create_profile(name=nomb,country=pais,age=edad)
create_profile(nomb)