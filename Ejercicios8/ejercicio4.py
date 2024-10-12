class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_info(self):
        return f"{self.año} {self.marca} {self.modelo}"


class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, características):
        super().__init__(marca, modelo, año)
        self.características = características  
    def imprimir_caracteristicas(self):
        print("Características de la moto:")
        for caracteristica in self.características:
            print(f"- {caracteristica}")



caracteristicas_moto = (
    "2 ruedas",
    "Motor de 150cc",
    "Frenos de disco",
    "Transmisión manual"
)

moto = Moto("Yamaha", "YZF-R15", 2020, caracteristicas_moto)


print(moto.mostrar_info())
moto.imprimir_caracteristicas()
