def check_even(num):
    if num%2 == 0:
        res=True
    else:
        res=False
    return res

num=int(input("Ingresa un número "))

nume=check_even(num)
print(nume)