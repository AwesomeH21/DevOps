def calculate_discount(price,discount_precentage,tax=0):
    taxer=100-tax
    discounter=100-discount_precentage
    if tax != 0:
        res=(price*(discounter/100))*(taxer/100)
    else:
        res=price*(discounter/100)
    return res

num1=float(input("Dame el precio "))
num2=float(input("Dame el descuento "))
num3=float(input("Dame el tax"))

res2=calculate_discount(discount_precentage=num2,price=num1)
res1=calculate_discount(discount_precentage=num2,price=num1,tax=num3)
print("Precio final: ",res1)
print("Precio final ",res2)