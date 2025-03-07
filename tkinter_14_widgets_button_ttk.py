import tkinter as tk
from tkinter import ttk

root = tk.Tk()

def on_button_tk_click():
    print("Botón de Tkinter presionado")

def on_button_ttk_click():
    print("Botón de ttk presionado")

# Botón de Tkinter
# ================

btn_tk = tk.Button(root, text="Botón Tkinter", 
                   bg="plum", fg="black", 
                   font=("Helvetica", 12), 
                   width=20, height=2, 
                   activebackground="palevioletred", activeforeground="black")
btn_tk.pack(pady=20)

btn_tk.config(command=on_button_tk_click)


# Botón de ttk
#=============

btn_ttk = ttk.Button(root, text="Botón ttk",
                     width=20, 
                     style="TButton")
btn_ttk.pack(pady=20)

btn_ttk.config(command=on_button_ttk_click)

# Configuración del estilo para ttk
style = ttk.Style()
style.configure("TButton", 
                font=("Helvetica", 12), 
                padding=20,
                background="plum", 
                foreground="black")
style.map("TButton", 
          background=[("active", "palevioletred")], 
          foreground=[("active", "black")])





root.mainloop()



# Comparativa visual y funcional:

# Apariencia:

# Los botones tk.Button pueden tener bordes y estilos personalizados de forma más directa (como el borde elevado, relieve, etc.).
# Los botones ttk.Button tienden a seguir el estilo nativo del sistema operativo (lo que se conoce como "themed"). 
# Esto hace que se vean más consistentes con el resto de las aplicaciones del sistema operativo, aunque a veces limita la personalización visual en cuanto a bordes y relieve.

# Estilo:

# ttk utiliza un sistema de estilos más avanzado que permite gestionar de manera centralizada los estilos de los widgets. 
# Puedes cambiar el comportamiento de todos los botones ttk de una vez utilizando style.configure.
# tk.Button, por otro lado, se personaliza directamente en el widget con propiedades como bg, fg, font, etc.

# Interactividad:

# Ambos botones muestran un comportamiento similar con el uso de eventos (<Button-1>, command, etc.). 
# Los botones de ttk tienen un aspecto más integrado con el sistema operativo y por tanto pueden tener un comportamiento más natural en cuanto a animaciones y respuesta al clic.