lalista=[1,2,3,4]
lista2=[]
def ola(lalista):
    lista2=lalista
    lista2[1]=1000
    return lalista

print(lalista)
print(ola(lalista))