class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Profesor(Persona):
    def __init__(self, nombre, edad, materias):
        super().__init__(nombre, edad)
        self.materias = materias

    def mostrar_materias(self):
        print(f"Materias impartidas por {self.nombre}:")
        for materia in self.materias:
            print(f"- {materia}")

profesor = Profesor("Carlos Martínez", 45, ["Matemáticas", "Física", "Química"])

profesor.mostrar_materias()
