import tkinter as tk

# Función para manejar los clics de los botones numéricos y de operadores
def click_button(value):
    current = screen.get()
    screen.delete(0, tk.END)
    screen.insert(tk.END, current + value)

# Función para calcular el resultado de la expresión en la pantalla
def calculate():
    try:
        result = eval(screen.get())
        screen.delete(0, tk.END)
        screen.insert(tk.END, str(result))
    except Exception as e:
        screen.delete(0, tk.END)
        screen.insert(tk.END, "Error")

# Función para limpiar la pantalla
def clear_screen():
    screen.delete(0, tk.END)

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora Personalizada")
root.configure(bg='black')

# Crear la pantalla de entrada/salida
screen = tk.Entry(root, font=("Arial", 18), borderwidth=2, relief="sunken", bg='light gray', fg='black')
screen.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Lista de botones (números y operaciones) con sus respectivas posiciones
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Crear y posicionar los botones en la ventana
for (text, row, column) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, font=("Arial", 18), width=5, height=2,
                           bg='yellow', fg='black', activebackground='yellow', activeforeground='black',
                           command=calculate)
    else:
        button = tk.Button(root, text=text, font=("Arial", 18), width=5, height=2,
                           bg='yellow', fg='black', activebackground='yellow', activeforeground='black',
                           command=lambda t=text: click_button(t))
    button.grid(row=row, column=column, padx=5, pady=5)

# Botón para limpiar la pantalla
clear_button = tk.Button(root, text='C', font=("Arial", 18), width=5, height=2,
                         bg='red', fg='white', activebackground='red', activeforeground='white',
                         command=clear_screen)
clear_button.grid(row=4, column=3, padx=5, pady=5)

# Iniciar el loop de la ventana
root.mainloop()
