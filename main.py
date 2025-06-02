import tkinter as tk

def saludar():
    nombre = entrada.get()
    etiqueta_resultado.config(text=f"¡Hola, {nombre}!")

# Crear ventana
ventana = tk.Tk()
ventana.title("Saludo personalizado")
ventana.geometry("300x150")
ventana2 = tk.Tk()
ventana2.title("VENTANA 2")
ventana2.geometry("800x600")

# Etiqueta y campo de entrada
etiqueta = tk.Label(ventana, text="¿Cómo te llamas?")
etiqueta.pack(pady=5)



entrada = tk.Entry(ventana)
entrada.pack(pady=5)

# Botón de saludo
boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack(pady=5)

# Etiqueta para mostrar el saludo
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack(pady=10)

# Iniciar la ventana
ventana.mainloop()

