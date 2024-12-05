import tkinter as tk
from tkinter import messagebox

prodcutos={"perros": 5, "gatos": 4, "conejos": 20, "hámsters" :15}

def buscar():
    busqueda=field1.get()
    busqueda2=busqueda.lower()
    messagebox.showinfo("Atención",f"hay {prodcutos[busqueda2]} {busqueda}")



ventana=tk.Tk()
ventana.title("Ejercicio15")
ventana.geometry("300x200")

etiqueta1=tk.Label(ventana, text="busca")
etiqueta1.pack()
field1=tk.Entry(ventana)
field1.pack(padx=5,pady=5)

sumador=tk.Button(ventana, text="buscar", command=buscar)
sumador.pack(padx=5, pady=15)


ventana.mainloop()