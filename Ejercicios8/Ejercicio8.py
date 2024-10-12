class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto, cantidad):
        self.productos.append((producto, cantidad))

    def mostrar_inventario(self):
        if self.productos:
            print("Inventario actual:")
            for producto, cantidad in self.productos:
                print(f"Producto: {producto}, Cantidad: {cantidad}")
        else:
            print("El inventario está vacío.")

inventario = Inventario()
inventario.agregar_producto("Manzanas", 50)
inventario.agregar_producto("Naranjas", 30)
inventario.agregar_producto("Plátanos", 100)

inventario.mostrar_inventario()
