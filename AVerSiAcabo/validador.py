import tkinter as tk
from tkinter import messagebox

# Función para validar la IP
def validar_ip():
    ip = entrada_ip.get()  # Obtener el texto del cuadro de entrada
    partes = ip.split(".")  # Dividir la dirección en partes

    # Verificar si la IP tiene exactamente 4 partes
    if len(partes) != 4:
        messagebox.showerror("Error", "La dirección IP debe tener 4 octetos.")
        return

    for parte in partes:
        # Verificar que cada parte sea un número
        if not parte.isdigit():
            messagebox.showerror("Error", f"'{parte}' no es un número válido.")
            return
        
        # Convertir la parte a un número
        numero = int(parte)
        
        # Verificar si el número está en el rango de 0 a 255
        if numero < 0 or numero > 255:
            messagebox.showerror("Error", f"'{parte}' no está en el rango válido (0-255).")
            return

    # Si pasa todas las validaciones, es una IP válida
    messagebox.showinfo("Éxito", "La dirección IP es válida.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Validador de Dirección IPv4")

# Crear los componentes de la interfaz
label = tk.Label(ventana, text="Ingresa una dirección IPv4:")
label.pack(pady=10)

entrada_ip = tk.Entry(ventana, width=20)
entrada_ip.pack(pady=10)

boton_validar = tk.Button(ventana, text="Validar", command=validar_ip)
boton_validar.pack(pady=20)

# Ejecutar la ventana
ventana.mainloop()
