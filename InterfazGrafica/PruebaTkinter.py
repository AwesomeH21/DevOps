import tkinter as tk
from tkinter import messagebox, ttk

#Ventana principal
root = tk.Tk()
root.title("Cacluladora extendida")
root.geometry("500x400")

#Etiqueta y cargo de entrada para el primer número
label1 = tk.Label(root, text="Número 1:", font=("Arial", 10))
label1.grid(row=0, column=0, padx=10, pady=5)
num1_entry = tk.Entry(root, width=15)
num1_entry.grid(row=0, column=1, padx=10, pady=5)

#Etiqueta y cambo de entrada para el segundo número
label2 = tk.Label(root, text="Número 2:", font=("Arial", 10))
label2.grid(row=0, column=0, padx=10, pady=5)
num2_entry = tk.Entry(root, width=15)
num2_entry.grid(row=0, column=1, padx=10, pady=5)

#lista desplegabble para seleccionar la operación
operacion = tk.StringVar(value="Suma")
operacion_label = tk.Label(root, text="Operación", font=("Arial", 10))
operacion_label.grid(row=2, column=0, padx=10, pady=5)
operacion_menu = tk.OptionMenu(
    root, operacion, "Suma", "Resta", "Multiplicacion", "Division"
)

