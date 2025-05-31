import tkinter as Tk
from tkinter import messagebox

def suma():
    try:
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        resultado = num1 + num2
        label_resultado.config(text="Resultado: " + str(resultado))
    except ValueError:
        messagebox.showerror("Error de entrada", "Por favor, ingrese números válidos")

def resta():
    try:
        num1 = int(entry_num1.get())
        num2 =int(entry_num2.get())
        resultado = num1 - num2
        label_resultado.config(text="Resultado: " + str(resultado))
    except ValueError:
        messagebox.showerror("Error de entrada", "Por favor, ingrese números válidos")

def multiplica():
    try:
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        resultado = num1 * num2
        label_resultado.config(text="Resultado: " + str(resultado))
    except ValueError:
        messagebox.showerror("Error de entrada", "Por favor, ingrese números válidos")

def divide():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if num2 == 0:
            raise ZeroDivisionError
        resultado = num1 / num2
        label_resultado.config(text="Resultado: " + str(resultado))
    except ValueError:
        messagebox.showerror("Error de entrada", "Por favor, ingrese números válidos")
    except ZeroDivisionError:
        messagebox.showerror("Error matemático", "La división por cero no está permitida")

# Crear la ventana principal
app = Tk.Tk()
app.title("Calculadora Básica")

# Crear y colocar los widgets
Tk.Label(app, text="Primer número:").pack()
entry_num1 = Tk.Entry(app)
entry_num1.pack()

Tk.Label(app, text="Segundo número:").pack()
entry_num2 = Tk.Entry(app)
entry_num2.pack()

label_resultado = Tk.Label(app, text="Resultado: ")
label_resultado.pack()

Tk.Button(app, text="Sumar", command=suma).pack()
Tk.Button(app, text="Restar", command=resta).pack()
Tk.Button(app, text="Multiplicar", command=multiplica).pack()
Tk.Button(app, text="Dividir", command=divide).pack()

# Configurar la geometría de la ventana
app.geometry("500x500")

# Ejecutar la aplicación
app.mainloop()
