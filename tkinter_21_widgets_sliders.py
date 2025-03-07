import tkinter as tk

def show_value(valor):
    label.config(text=f"Valor seleccionado: {valor}")

root = tk.Tk()

# Crear una variable para almacenar el valor seleccionado
slider_value = tk.DoubleVar()

# Crear el slider horizontal
slider = tk.Scale(root, from_=0, to=100, orient="horizontal", variable=slider_value, command=show_value, width=40, length=300, bd=5)
slider.pack(pady=20)

# Crear una etiqueta para mostrar el valor
label = tk.Label(root, text="Valor seleccionado: 0")
label.pack(pady=20)

root.mainloop()
