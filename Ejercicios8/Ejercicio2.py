class ColeccionNumeros:
    def maximo(self,nums):
        compa=0
        for x in nums:
            if(x > compa):
                maximomeridio=x
            compa = x
        return maximomeridio

La_lista=[]
for i in range(5):
    num=int(input("Ingresa números para la lista"))
    La_lista.append(num)
print(ColeccionNumeros.maximo(ColeccionNumeros,La_lista))

