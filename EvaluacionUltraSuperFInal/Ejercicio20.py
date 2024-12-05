import tkinter as tk
from tkinter import messagebox

diccionario={"clave1": 1, "clave2": 2, "clave3": 3, "clave4": 4, "clave5": 5}

def diccionar():
    EntradaUsuario=field1.get()

    if EntradaUsuario in diccionario:
        messagebox.showinfo("La clave se encuentra en el diccionario",f"La clave {EntradaUsuario} se encuentra en el diccionario y tiene el valor: {diccionario[EntradaUsuario]}")
    else:
        messagebox.showinfo("La clave no se encuentra en el diccionario",f"La clave {EntradaUsuario} no se ecuentra en el diccionario")





ventana=tk.Tk()
ventana.title("Diccionario")
ventana.geometry("300x100")


etiqueta1=tk.Label(ventana, text="Busca una clave del diccionario", justify="center")
etiqueta1.pack()

field1=tk.Entry(ventana)
field1.pack(padx=5,pady=5)

sumador=tk.Button(ventana, text="Dame una clave", command=diccionar)
sumador.pack(padx=5, pady=15)

ventana.mainloop() 