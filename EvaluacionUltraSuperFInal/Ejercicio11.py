import tkinter as tk
from tkinter import messagebox

def sum():
    num1=int(field1.get())
    num2=int(field2.get())

    suma=num1+num2
    messagebox.showinfo("Atención",f"La suma fue de: {suma}")

ventana=tk.Tk()
ventana.title("Ejercicio1")
ventana.geometry("400x300")

etiqueta1=tk.Label(ventana, text="Num1")
etiqueta1.pack()
field1=tk.Entry(ventana)
field1.pack(padx=5,pady=5)

etiqueta2=tk.Label(ventana, text="Num2")
etiqueta2.pack()
field2=tk.Entry(ventana)
field2.pack(padx=5, pady=10)

sumador=tk.Button(ventana, text="Sumar", command=sum)
sumador.pack(padx=5, pady=15)

ventana.mainloop()