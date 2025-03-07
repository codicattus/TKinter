import tkinter as tk

root = tk.Tk()
root.title("TKinter")

root.state("normal")                # Estado normal (por defecto)
#root.attributes('-zoomed', True)    # Maximiza la ventana (En Windows y Linux)
#root.state("iconic")                # Minimiza la ventana (En Windows, en Linux y Mac depende del gestor de ventanas)

# root.withdraw()                             # La oculta completamente
root.after(3000, lambda: root.iconify())    # Después de 3 segundos, la minimiza
# root.after(6000, lambda: root.deiconify())  # Después de 6 segundos, la vuelve a mostrar

# root.wm_iconify()


root.mainloop()