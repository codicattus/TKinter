import tkinter as tk

# Función para actualizar la pantalla
def click(boton):
    pantalla.insert(tk.END, str(boton))  # Inserta el nuevo dígito al final

# Función para evaluar la expresión matemática
def calcular():
    try:
        resultado = eval(pantalla.get())
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, str(resultado))
    except:
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, "Error")

# Función para limpiar la pantalla
def limpiar():
    pantalla.delete(0, tk.END)

# Crear ventana principal
root = tk.Tk()
root.title("Calculadora")

# Crear pantalla de entrada
pantalla = tk.Entry(root, 
                    font=("Arial", 20),
                    relief="groove",
                    width=40, 
                    bd= 6, 
                    justify="right")
pantalla.grid(row=0, 
              column=0, 
              columnspan=4,
              pady=10)

# Definir botones
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

# Crear y colocar botones
for texto, fila, columna in botones:
    if texto == "=":
        cmd = calcular
    else:
        cmd = lambda t=texto: click(t)
    boton = tk.Button(root, 
              text=texto, 
              width=10, 
              height=2, 
              font=("Arial", 14), 
              command=cmd)
    boton.grid(row=fila, 
               column=columna, 
               sticky="nsew")

boton_c = tk.Button(root, 
          text="C", 
          width=5, 
          height=2, 
          font=("Arial", 14), 
          command=limpiar)
boton_c.grid(row=5, 
             column=0, 
             columnspan=4, 
             sticky="nsew")

root.mainloop()



# Ojo con eval(). Se ha puesto a propósito para mostrar las vulnerabilidades de un código.

# Código vulnerable:
# eval('__import__("os").system("echo Hola > archivo.txt")')

# ======================================================================================= #

# Algunas soluciones:
# --------------------------------------------------------------------------------------- #
# resultado = eval(pantalla.get(), {"__builtins__": None}, {})
# Deshabilitamos los "builtins" (funciones y módulos predeterminados de Python) pasando {"__builtins__": None} 
# como el primer argumento del entorno de eval(), lo que evita que el usuario pueda acceder a funciones como os.system
# --------------------------------------------------------------------------------------- #
# import ast
# resultado = ast.literal_eval(pantalla.get()) 
# solo permite la evaluación de literales seguros (como números, cadenas de texto, listas, diccionarios, etc.) 
# y no permite ejecutar ningún código arbitrario.
# --------------------------------------------------------------------------------------- #
