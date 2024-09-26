def make_sandwich(bread_type,filling):
    print(f"Tu sandwich con pan {bread_type} es de {filling}")

pancito=input("Dame un tipo de pan: ")
relleno=input("Dame el relleno para un sandwich: ")

make_sandwich(filling=relleno,bread_type=pancito)