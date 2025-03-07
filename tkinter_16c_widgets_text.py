import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Crear un estilo para personalizar la barra de desplazamiento
style = ttk.Style()
style.configure("TScrollbar",
                gripcount=0,
                background="tomato",  # Color de la barra
                troughcolor="lightgray",  # Color del canal de desplazamiento
                arrowcolor="white",
                width=40)  # Color de las flechas

# Crear un Frame para contener el Text y la barra de desplazamiento
frame = tk.Frame(root, width=400, height=300)
frame.pack(padx=20, pady=20)

# Crear el widget Text dentro del frame
text_area_2 = tk.Text(frame, wrap="word", height=10, width=40)
text_area_2.pack(side="left", fill="both", expand=True)

# Crear la barra de desplazamiento con el estilo modificado
scrollbar = ttk.Scrollbar(frame, style="TScrollbar", command=text_area_2.yview)
scrollbar.pack(side="right", fill="y")

# Vincular la barra de desplazamiento con el widget Text
text_area_2.config(yscrollcommand=scrollbar.set)

# Insertar texto para hacer que aparezca la barra de desplazamiento
for i in range(100):
    text_area_2.insert("end", f"Línea {i+1}\n")

root.mainloop()


