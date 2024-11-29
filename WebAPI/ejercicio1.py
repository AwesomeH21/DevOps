import tkinter as tk
from tkinter import messagebox
import requests 

def obtener_pokemon():
    nombre_pokemon = (
        entrada.get().lower()
    )
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}"

    try:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            datos = respuesta.json()

            id_pokemon = datos["id"]
            altura = datos["height"]
            peso = datos["weight"]
            habilidades = ", ".join(ability["ability"]["name"] for ability in datos["abilities"])

            resultado.config(
                text=f"ID: {id_pokemon}\nAltura: {altura}\nPeso {peso} hectogramos\nHabilidades: {habilidades}"
            )
        else:
            messagebox.showerror("Error", "Pokemón no encontrado, intenta nuevamente.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"No se pudo conectar con la API: {e}")

ventana = tk.Tk()
ventana.title("Busqueda de pokemón")
ventana.geometry("400x300")

tk.Label(ventana, text="Ingresa el nombre del pokemón:", font=("Arial", 12)).pack(
    pady=10
)
entrada = tk.Entry(ventana, font=("Arial", 14))
entrada.pack(pady=10)

boton = tk.Button(ventana, text="Buscar", font=("Arial", 12), command=obtener_pokemon)
boton.pack(pady=10)

resultado = tk.Label(ventana, text="", font=("Arial", 12), justify="center")
resultado.pack(pady=20)

ventana.mainloop()