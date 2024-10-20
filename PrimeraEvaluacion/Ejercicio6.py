
def contar(archivo):
    with open(archivo, 'r') as f:
        lineas = f.readlines()
    return len(lineas)


archivo = "c:/AquiVaDondeUstedDescargueLaCarpeta/PrimeraEvaluacion/hola.txt"
numlin = contar(archivo)
print(f"El archivo '{archivo}' tiene {numlin} líneas.")
