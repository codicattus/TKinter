import tkinter as tk

root = tk.Tk()

btn = tk.Button(root, text="Haz clic", command=lambda: print("Botón presionado"), fg= "moccasin", bg= "saddlebrown")

btn.pack(pady=80)




root.mainloop()








# Propiedades principales de un botón


# Parámetro	                        Descripción	                                          Ejemplo
# =================================================================================================================
# text	                           Texto del botón	                                   text="Enviar"
# command	               Función que se ejecuta al hacer clic	                     command=mi_funcion
# fg / bg	                 Color del texto / fondo	                             fg="white", bg="blue"
# font	                      Tipo y tamaño de letra	                            font=("Arial", 12, "bold")
# width / height	     Ancho y alto del botón en caracteres	                     width=10, height=2
# padx / pady	         Espaciado interno (horizontal/vertical)	                   padx=10, pady=5
# relief	                      Estilo del borde	                                   relief="raised"
# state	               Estado del botón (normal, disabled, active)	                   state="disabled"
# image	                      Imagen en lugar de texto	                               image=mi_imagen