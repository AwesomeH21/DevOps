import tkinter as tk
from tkinter import messagebox
import requests

def buscar():
    url = "https://catfact.ninja/fact"

    try:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            dato = datos["fact"]

            messagebox.showinfo("Dato random de los gatos", dato)
            
        else:
            messagebox.showerror("Error", "Pokemón no encontrado, intenta nuevamente.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"No se pudo conectar con la API: {e}")

ventana=tk.Tk()
ventana.title("Datos sobre gatos")
ventana.geometry("300x100")


etiqueta1=tk.Label(ventana, text="Oprime el botón para un dato curioso sobre un gato", justify="center")
etiqueta1.pack()
sumador=tk.Button(ventana, text="Dame un dato random", command=buscar)
sumador.pack(padx=5, pady=15)

ventana.mainloop()