la_tupla =(1,2,3,4,5)
lista=[]
for tuplear in la_tupla:
    lista.append(tuplear)

lista[2]=8
nuevatupla=()


nuevatupla=tuple(lista)

print(la_tupla,lista,nuevatupla)