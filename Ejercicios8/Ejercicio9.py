class Profesor:
    def __init__(self, materias):
        self.materias = materias

    def filtrar_materias(self, letra_inicial):
        materias_filtradas = []
        for materia in self.materias:
            if materia.startswith(letra_inicial):
                materias_filtradas.append(materia)
        return materias_filtradas

materias = ["Matemáticas", "Física", "Química", "Historia", "Informática"]

profesor = Profesor(materias)

materias_con_m = profesor.filtrar_materias("M")
print(f"Materias que comienzan con 'M': {materias_con_m}")

materias_con_i = profesor.filtrar_materias("I")
print(f"Materias que comienzan con 'I': {materias_con_i}")
