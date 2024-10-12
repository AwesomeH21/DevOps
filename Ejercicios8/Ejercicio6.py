
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def __init__(self):
        self.libros = {}

    def agregar_libro(self, libro):
        self.libros[libro.titulo] = libro

  
    def buscar_autor(self, titulo):
        if titulo in self.libros:
            return self.libros[titulo].autor
        else:
            return "Libro no encontrado"

libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
libro2 = Libro("El Quijote", "Miguel de Cervantes")

biblioteca = Biblioteca()
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

print(biblioteca.buscar_autor("Cien años de soledad"))  
print(biblioteca.buscar_autor("El Quijote"))  
print(biblioteca.buscar_autor("Donde los árboles cantan")) 