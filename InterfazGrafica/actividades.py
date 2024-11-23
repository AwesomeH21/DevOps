import tkinter as tk
from tkinter import messagebox

# Lista para almacenar actividades
actividades = []

def agregar_actividad():
    descripcion = entry_descripcion.get()
    categoria = categoria_var.get()
    completado = completado_var.get()

    if not descripcion or not categoria:
        messagebox.showwarning("Datos incompletos", "Por favor, ingresa una descripción y selecciona una categoría.")
        return

    # Guardar la actividad como un diccionario
    actividad = {"Descripción": descripcion, "Categoría": categoria, "Completado": completado}
    actividades.append(actividad)

    # Mostrar la actividad en la lista
    lista_actividades.insert(tk.END, f"{descripcion} - {categoria} - {'Completado' if completado else 'Pendiente'}")

    # Limpiar campos
    entry_descripcion.delete(0, tk.END)
    categoria_var.set("")
    completado_var.set(False)

def ver_reporte():
    completadas = [a for a in actividades if a["Completado"]]
    pendientes = [a for a in actividades if not a["Completado"]]

    reporte = (
        f"Actividades completadas ({len(completadas)}):\n"
        + "\n".join([f"- {a['Descripción']} ({a['Categoría']})" for a in completadas])
        + "\n\n"
        + f"Actividades pendientes ({len(pendientes)}):\n"
        + "\n".join([f"- {a['Descripción']} ({a['Categoría']})" for a in pendientes])
    )

    messagebox.showinfo("Reporte de Actividades", reporte)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Seguimiento de Actividades Diarias")
ventana.geometry("500x500")

# Título
label_titulo = tk.Label(ventana, text="Seguimiento de Actividades Diarias", font=("Arial", 16))
label_titulo.pack(pady=10)

# Descripción de la actividad
label_descripcion = tk.Label(ventana, text="Descripción de la actividad:")
label_descripcion.pack()
entry_descripcion = tk.Entry(ventana, width=50)
entry_descripcion.pack(pady=5)

# Categoría de la actividad
label_categoria = tk.Label(ventana, text="Selecciona una categoría:")
label_categoria.pack()
categoria_var = tk.StringVar(value="")
menu_categoria = tk.OptionMenu(ventana, categoria_var, "Física", "Mental", "Profesional", "Personal")
menu_categoria.pack(pady=5)

# Completado
completado_var = tk.BooleanVar()
check_completado = tk.Checkbutton(ventana, text="¿Completado?", variable=completado_var)
check_completado.pack(pady=5)

# Botón para agregar actividad
boton_agregar = tk.Button(ventana, text="Añadir Actividad", command=agregar_actividad)
boton_agregar.pack(pady=10)

# Lista de actividades
label_lista = tk.Label(ventana, text="Lista de actividades:")
label_lista.pack()
lista_actividades = tk.Listbox(ventana, width=70, height=10)
lista_actividades.pack(pady=10)

# Botón para ver reporte
boton_reporte = tk.Button(ventana, text="Ver Reporte de Actividades", command=ver_reporte)
boton_reporte.pack(pady=10)

# Ejecutar aplicación
ventana.mainloop()
