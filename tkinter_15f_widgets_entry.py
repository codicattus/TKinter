import tkinter as tk
import re


def validate_length(new_value):
    return len(new_value) <= 10

def validate_range(event):
    value = entry_2.get()
    if value.isdigit(): 
        num = int(value)
        if 10 <= num <= 100:
            error_label.config(text="Número válido", fg="green")
        else:
            error_label.config(text="Número fuera de rango (10-100)", fg="red")
    else:
        error_label.config(text="Ingrese un número válido", fg="red")

def validate_text(new_value):
    return re.fullmatch(r"[A-Za-z ]*", new_value) is not None


root = tk.Tk()

tk.Frame(root,height=40).pack()
label_1 = tk.Label(root,text="Máximo 10 caracteres")
label_1.pack()

validate_command = root.register(validate_length)
entry_1 = tk.Entry(root, validate="key", validatecommand=(validate_command, "%P"))
entry_1.pack(pady=20)


tk.Frame(root,height=40).pack()
label_2 = tk.Label(root,text="Permitir solo valores entre cierto rango")
label_2.pack()

entry_2 = tk.Entry(root)
entry_2.pack(pady=10)
entry_2.bind("<Return>", validate_range) 

error_label = tk.Label(root, text="", fg="red")
error_label.pack()

tk.Frame(root,height=40).pack()
label_3 = tk.Label(root,text="Permitir solo letras y espacios")
label_3.pack()

validate_command = root.register(validate_text)
entry = tk.Entry(root, validate="key", validatecommand=(validate_command, "%P"))
entry.pack(pady=20)

root.mainloop()



# La biblioteca re en Python proporciona herramientas para trabajar con expresiones regulares (regex)
# re.fullmatch() compara toda la cadena con el patrón r"[A-Za-z ]*".

# Patrón r"[A-Za-z ]*":

# A-Z → Mayúsculas permitidas.
# a-z → Minúsculas permitidas.
# " " (espacio) → Se permiten espacios.
# * → Permite cualquier cantidad de caracteres (incluyendo ninguno).

# Otras opciones en re

# re.fullmatch(patron, texto)	          Verifica si toda la cadena coincide con el patrón.
# re.match(patron, texto)	              Verifica si el inicio de la cadena coincide con el patrón.
# re.search(patron, texto)	              Busca si en cualquier parte de la cadena hay una coincidencia.
# re.findall(patron, texto)	              Encuentra todas las coincidencias en la cadena.