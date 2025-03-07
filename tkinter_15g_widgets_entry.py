import tkinter as tk

def on_focus_in(event, placeholder_text):
    """Elimina el placeholder cuando el usuario hace clic en el Entry"""
    if event.widget.get() == placeholder_text:
        event.widget.delete(0, tk.END)
        event.widget.config(fg="black")

def on_focus_out(event, placeholder_text):
    """Restaura el placeholder si el usuario no ha escrito nada"""
    if event.widget.get() == "":
        event.widget.insert(0, placeholder_text)
        event.widget.config(fg="gray")

root = tk.Tk()

placeholder_text_1 = "Escribe tu nombre aquí"
placeholder_text_2 = "Escribe tu correo aquí"

# Crear el primer Entry con placeholder
entry1 = tk.Entry(root, fg="gray")
entry1.insert(0, placeholder_text_1)
entry1.bind("<FocusIn>", lambda event: on_focus_in(event, placeholder_text_1))
entry1.bind("<FocusOut>", lambda event: on_focus_out(event, placeholder_text_1))
entry1.pack(pady=20)

# Crear el segundo Entry con placeholder
entry2 = tk.Entry(root, fg="gray")
entry2.insert(0, placeholder_text_2)
entry2.bind("<FocusIn>", lambda event: on_focus_in(event, placeholder_text_2))
entry2.bind("<FocusOut>", lambda event: on_focus_out(event, placeholder_text_2))
entry2.pack(pady=20)

root.mainloop()

