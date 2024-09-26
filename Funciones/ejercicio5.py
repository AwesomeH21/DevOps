def greet_with_default(name="Guest"):
    print("Bienvenido "+name)

nam=input("Ingresa tu nombre ")
if nam=="":
    greet_with_default()
else:
    greet_with_default(nam)