import tkinter as tk

root = tk.Tk()
root.title("TKinter")
width = 1200                                              # ----> Anchura de la ventana
height = 600                                              # ----> Altura de la ventana
x_pos = 100                                               # ----> Posición en eje x respecto a la esquina superior izquierda
y_pos = 400                                               # ----> Posición en eje y respecto a la esquina superior izquierda
geometry = f"{width}x{height}+{x_pos}+{y_pos}"            # ----> Generación del string en el orden y formato que espera recibir el método geometry  
root.geometry(geometry)                                   # ----> Adjudicamos las dimensiones y la posición a la ventana

root.mainloop()

