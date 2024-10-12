class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f}"


class CarritoDeCompras:
    def __init__(self):
        self.productos = []  
    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print("Productos en el carrito:")
        for producto in self.productos:
            print(producto)



producto1 = Producto("Manzana", 1.20)
producto2 = Producto("Pan", 0.90)
producto3 = Producto("Leche", 1.50)


carrito = CarritoDeCompras()
carrito.agregar_producto(producto1)
carrito.agregar_producto(producto2)
carrito.agregar_producto(producto3)


carrito.mostrar_productos()
