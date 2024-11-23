import tkinter as tk
from tkinter import messagebox

def enviar_encuesta():
    nombre = entry_nombre.get()
    genero_favorito = genero_var.get()
    frecuencia = frecuencia_var.get()
    dispositivos = []
    if casa_var.get():
        dispositivos.append("En casa")
    if cine_var.get():
        dispositivos.append("En el cine")
    if movil_var.get():
        dispositivos.append("En dispositivos móviles")

    if not nombre or not genero_favorito or not frecuencia or not dispositivos:
        messagebox.showwarning("Encuesta incompleta", "Por favor, completa todos los campos de la encuesta.")
        return

    resumen = (
        f"Gracias por participar, {nombre}!\n\n"
        f"Resumen de tus respuestas:\n"
        f"- Género favorito: {genero_favorito}\n"
        f"- Frecuencia de visitas al cine: {frecuencia}\n"
        f"- Dispositivos preferidos: {', '.join(dispositivos)}"
    )

    messagebox.showinfo("Encuesta enviada", resumen)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Encuesta de Preferencias de Cine")
ventana.geometry("400x400")

# Título
label_titulo = tk.Label(ventana, text="Encuesta de Preferencias de Cine", font=("Arial", 14))
label_titulo.pack(pady=10)

# Nombre del usuario
label_nombre = tk.Label(ventana, text="¿Cuál es tu nombre?")
label_nombre.pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack(pady=5)

# Género favorito
label_genero = tk.Label(ventana, text="Selecciona tu género favorito:")
label_genero.pack()
genero_var = tk.StringVar(value="")
option_menu = tk.OptionMenu(ventana, genero_var, "Acción", "Comedia", "Drama", "Terror")
option_menu.pack(pady=5)

# Frecuencia de visitas al cine
label_frecuencia = tk.Label(ventana, text="¿Con qué frecuencia vas al cine?")
label_frecuencia.pack()
frecuencia_var = tk.StringVar(value="")
radio_semanal = tk.Radiobutton(ventana, text="Semanalmente", variable=frecuencia_var, value="Semanalmente")
radio_mensual = tk.Radiobutton(ventana, text="Mensualmente", variable=frecuencia_var, value="Mensualmente")
radio_ocasional = tk.Radiobutton(ventana, text="Ocasionalmente", variable=frecuencia_var, value="Ocasionalmente")
radio_semanal.pack()
radio_mensual.pack()
radio_ocasional.pack()

# Dispositivos preferidos
label_dispositivos = tk.Label(ventana, text="¿Dónde prefieres ver películas?")
label_dispositivos.pack()
casa_var = tk.BooleanVar()
cine_var = tk.BooleanVar()
movil_var = tk.BooleanVar()
check_casa = tk.Checkbutton(ventana, text="En casa", variable=casa_var)
check_cine = tk.Checkbutton(ventana, text="En el cine", variable=cine_var)
check_movil = tk.Checkbutton(ventana, text="En dispositivos móviles", variable=movil_var)
check_casa.pack()
check_cine.pack()
check_movil.pack()

# Botón de enviar
boton_enviar = tk.Button(ventana, text="Enviar Encuesta", command=enviar_encuesta)
boton_enviar.pack(pady=20)

# Ejecutar aplicación
ventana.mainloop()
