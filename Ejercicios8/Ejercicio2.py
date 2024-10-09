class ColeccionNumeros:
    def maximo(self,nums):
        orden=sorted(nums)
        return orden[4]

La_lista=[]
for i in range(5):
    num=int(input("Ingresa números para la lista"))
    La_lista.append(num)
print(ColeccionNumeros.maximo(ColeccionNumeros,La_lista))

