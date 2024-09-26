def basic_operations(num,nume):
    suma=num+nume
    resta=num-nume
    multi=num*nume
    divi=num/nume
    return suma,resta,multi,divi

num1=int(input("Dame un número: "))
num2=int(input("Dame otro número"))

tot=basic_operations(num1,num2)
print("ahí te van las operaciones básicas",tot)