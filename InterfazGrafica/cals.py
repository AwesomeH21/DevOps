import tkinter as tk
from tkinter import messagebox

# Datos de calorías por alimento y tamaño de porción
calorias_por_alimento = {
    "Desayuno": {"Panqueques": 150, "Huevos": 100, "Frutas": 80},
    "Almuerzo": {"Pasta": 300, "Ensalada": 200, "Carne": 400},
    "Cena": {"Sopa": 150, "Pollo": 250, "Puré de papa": 200},
    "Snacks": {"Galletas": 100, "Frutos secos": 150, "Barra energética": 180}
}
calorias_por_porcion = {"Pequeña": 0.5, "Mediana": 1, "Grande": 1.5}
calorias_bebidas = {"Jugos": 120, "Café": 50}

def calcular_calorias():
    nombre = entry_nombre.get()
    if not nombre:
        messagebox.showwarning("Campo vacío", "Por favor, ingresa tu nombre.")
        return

    total_calorias = 0

    # Calcular calorías por comida
    for comida, opciones in comidas.items():
        alimento = opciones["var"].get()
        porcion = opciones["porcion_var"].get()
        if alimento and porcion:
            total_calorias += calorias_por_alimento[comida][alimento] * calorias_por_porcion[porcion]

    # Calcular calorías por bebidas
    if jugo_var.get():
        total_calorias += calorias_bebidas["Jugos"]
    if cafe_var.get():
        total_calorias += calorias_bebidas["Café"]

    # Mostrar resultados
    messagebox.showinfo(
        "Cálculo de Calorías",
        f"Hola {nombre}, has consumido un total aproximado de {total_calorias} calorías hoy."
    )

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Calorías")
ventana.geometry("450x500")

# Título
label_titulo = tk.Label(ventana, text="Calculadora de Calorías", font=("Arial", 16))
label_titulo.pack(pady=10)

# Nombre del usuario
label_nombre = tk.Label(ventana, text="¿Cuál es tu nombre?")
label_nombre.pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack(pady=5)

# Opciones para cada comida
comidas = {}
for comida, opciones in calorias_por_alimento.items():
    label_comida = tk.Label(ventana, text=f"Selecciona tu {comida.lower()}:")
    label_comida.pack(pady=5)

    comida_var = tk.StringVar(value="")
    menu_comida = tk.OptionMenu(ventana, comida_var, *opciones.keys())
    menu_comida.pack()

    porcion_var = tk.StringVar(value="")
    radio_pequena = tk.Radiobutton(ventana, text="Pequeña", variable=porcion_var, value="Pequeña")
    radio_mediana = tk.Radiobutton(ventana, text="Mediana", variable=porcion_var, value="Mediana")
    radio_grande = tk.Radiobutton(ventana, text="Grande", variable=porcion_var, value="Grande")

    radio_pequena.pack()
    radio_mediana.pack()
    radio_grande.pack()

    comidas[comida] = {"var": comida_var, "porcion_var": porcion_var}

# Opciones de bebidas
label_bebidas = tk.Label(ventana, text="¿Incluyes bebidas?")
label_bebidas.pack(pady=5)

jugo_var = tk.BooleanVar()
cafe_var = tk.BooleanVar()
check_jugo = tk.Checkbutton(ventana, text="Jugos", variable=jugo_var)
check_cafe = tk.Checkbutton(ventana, text="Café", variable=cafe_var)

check_jugo.pack()
check_cafe.pack()

# Botón para calcular
boton_calcular = tk.Button(ventana, text="Calcular Calorías", command=calcular_calorias)
boton_calcular.pack(pady=20)

# Ejecutar aplicación
ventana.mainloop()
