import tkinter as tk

root = tk.Tk()

def validar_entrada(texto):
    """ Permite solo números en el Entry """
    print(texto)
    return texto.isdigit() or texto == ""

vcmd = root.register(validar_entrada)  # Registramos la función de validación en Tkinter

entry = tk.Entry(root, validate="key", validatecommand=(vcmd, "%P"))
entry.pack(pady=10)

root.mainloop()



# Opciones del parámetro validate

# "key"	        En cada pulsación de tecla (antes de reflejarse en el Entry).
# "focusin"	    Cuando el Entry gana el foco (cuando el usuario hace clic en él).
# "focusout"	Cuando el Entry pierde el foco (por ejemplo, al hacer clic fuera).
# "all"	        Se activa en todas las situaciones anteriores.
# "none"	    No valida nada (valor por defecto).


# Marcadores disponibles

# %P	Nuevo valor previsto del Entry tras el cambio.
# %s	Valor actual antes de que ocurra el cambio.
# %V	Tipo de validación (key, focusin, focusout, etc.).
# %d	Tipo de acción realizada (1 = insert, 0 = delete).
# %i	Índice donde ocurre el cambio.
# %S	Carácter específico insertado o eliminado.

#      Si se pega texto (Ctrl+V o botón derecho → Pegar), %S solo verá el primer carácter, no todo el contenido pegado.

#      Por eso, en la mayoría de los casos, se recomienda validar usando %P, ya que te da el contexto completo. 
#      %S solo es útil si necesitas controlar la entrada tecla por tecla.

#      El método register() de Tkinter convierte una función de Python en una función que Tkinter puede llamar desde Tcl/Tk.
#      Tkinter es un wrapper de Tcl/Tk, y algunas funciones de validación deben ejecutarse en el motor de Tcl/Tk, no en Python directamente. 
#      Si pasáramos la función de validación sin register(), Tkinter no podría interpretarla correctamente y lanzaría un error.

#      Tcl → Tool Command Language (Lenguaje de Comandos de Herramientas)
#      Tk → Toolkit (Kit de Herramientas)
#      Juntos forman Tcl/Tk, donde Tcl es el lenguaje de scripting y Tk es la biblioteca gráfica para interfaces de usuario. 
#      Tkinter es el "puente" entre Python y Tcl/Tk.