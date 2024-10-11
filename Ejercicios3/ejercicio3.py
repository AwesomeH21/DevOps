cad1="Soy la cadena uno"
cad2="soy la cadena dos"
lcad1=len(cad1)
lcad2=len(cad2)
in1=cad1[0].upper()
in2=cad2[0].upper()

if lcad1 == lcad2 and in1 ==in2:
    print("Se cumplió la condición")
else:
    print("Pues no se cumplió")