import tkinter as tk

root = tk.Tk()
root.title("TKinter")
width = 1200                                             
height = 600                                              
                                  
screen_width = root.winfo_screenwidth()                               # ----> Obtiene el ancho de la pantalla
screen_height = root.winfo_screenheight()                              # ----> Obtiene el alto de la pantalla

x_pos = (screen_width - width) // 2                                              
y_pos = (screen_height - height) // 2

print(y_pos)

geometry = f"{width}x{height}+{x_pos}+{y_pos}" 
root.geometry(geometry) 

print(root.winfo_screenheight())
root.mainloop()


