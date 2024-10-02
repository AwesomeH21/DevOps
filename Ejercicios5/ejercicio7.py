lalista=[1,2,3]
latupla=(4,5,6)

def olas(elemen):
    elemen.append(234)
    return elemen

def olas2(elemen1):
    latupla.append(234)
    return latupla

print("Lista antes de  modificar",lalista,"Tupla antes de modificar", latupla)

print(olas(lalista))
print(olas2(latupla))