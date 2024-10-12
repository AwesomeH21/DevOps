class Estudiante:
    def __init__(self, nombre, calificaciones):
        self.nombre = nombre
        self.calificaciones = calificaciones 
    def promedio(self):
        total = sum(self.calificaciones.values())
        cantidad = len(self.calificaciones)
        return total / cantidad if cantidad > 0 else 0


calificaciones = {
    "Matemáticas": 85,
    "Física": 90,
    "Química": 78,
    "Historia": 88
}

estudiante = Estudiante("Juan", calificaciones)


promedio_calificaciones = estudiante.promedio()
print(f"El promedio de calificaciones de {estudiante.nombre} es: {promedio_calificaciones:.2f}")
