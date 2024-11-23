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
num2_entry.grid(row=1, column=1, padx=10, pady=5)

#lista desplegabble para seleccionar la operación
operacion = tk.StringVar(value="Suma")
operacion_label = tk.Label(root, text="Operación", font=("Arial", 10))
operacion_label.grid(row=2, column=0, padx=10, pady=5)
operacion_menu = tk.OptionMenu(
    root, operacion, "Suma", "Resta", "Multiplicacion", "Division"
)
operacion_menu.grid(row=2, column=1, padx=10, pady=5)
#Casilla de verificación para redondear el resultado
redondear_var=tk.BooleanVar
redondear_check=tk.Checkbutton(
    root, text="Redondear resultado?", variable=redondear_var
)
redondear_check.grid(row=3, column=8, columnspan=2, pady=5)

#Radio bototones para elegir formato de visualización
resultado_var = tk.StringVar(value="Normal")
resultado_label= tk.Label(root, text="Formato de resultado",font=("Arial", 10))
resultado_label.grid(row=4, column=8, padx=10, pady=5)
radio_normal = tk.Radiobutton(
    root, text="Normal", variable=resultado_var, value="Normal"
)
radio_cientifico = tk.Radiobutton(
    root, text="Cientifico", variable=resultado_var, value="Normal"
)
radio_normal.grid(row=4, column=1, sticky="w")
radio_cientifico.grid(row=4, column=1, sticky="e")

#Barra de progreso (Simulación de cálculo)
progreso = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progreso.grid(row=4, column=0, columnspan=2, pady=10)

#Área de texto para el historial de cálculos
historial_label = tk.Label(root, text="Historial de operaciones:", font=("Arial", 10))
historial_label.grid(row=6, column=0, padx=10, pady=5)
historial_text = tk.Text(root, height=5, width=40, state="disabled")
historial_text.grid(row=7, column= 0, columnspan=2, padx=10, pady=5)


#Funcion para realizar la operacion
def realizar_operacion():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        op = operacion.get()
        
        if op == "Suma":
            resultado = num1 + num2
        elif op == "Resta":
            resultado = num1 - num2
        elif op == "Multiplicacion":
            resultado = num1 * num2
        elif op == "División":
            if num2 == 0:
                raise ValueError("No se puede dividir entre 0")
            resultado = num1/num2
        if redondear_var.get():
            resultado = round(resultado)

        if resultado_var.get() == "Cientifico":
            resultado = "{:.2e}".format(resultado)
        historial_text.config(state="normal")
        historial_text.insert(tk.END, f"{num1} {op} {num2} = {resultado}\n")
        historial_text.config(state="disabled")

        progreso["value"] = 100

    except ValueError as e:
        messagebox.showerror("Error", f"Entrada inválida: {e}")

#boton para calcular el resultado
calcular_btn = tk.Button(root, text="Calcular", command=realizar_operacion)
calcular_btn.grid(row=8, column=0, columnspan=2, pady=10)

#iniciar la ventana
root.mainloop()