import tkinter as tk
from tkinter import ttk

def calcular_costos():
    try:
        # Obtener datos ingresados
        normal = list(map(int, normal_entries.get().split(',')))
        extra = list(map(int, extra_entries.get().split(',')))
        demanda = list(map(int, demanda_entries.get().split(',')))

        # Verificar que las listas tengan la longitud correcta
        if len(normal) != len(meses) or len(extra) != len(meses) or len(demanda) != len(meses):
            raise ValueError("Ingrese exactamente 6 valores para cada campo separados por comas.")

        # Variables acumuladas
        inventario = almacen_inicial
        costo_total = 0
        costos_detalle = []

        for i in range(len(meses)):
            produccion_normal = normal[i]
            produccion_extra = extra[i]
            demanda_mes = demanda[i]

            # Inventario disponible al inicio del mes
            inventario += produccion_normal + produccion_extra - demanda_mes

            # Cálculo de costos mensuales
            costo_normal_mes = produccion_normal * costo_normal
            costo_extra_mes = produccion_extra * costo_extra
            costo_almacen_mes = max(0, inventario) * costo_almacenamiento

            # Suma de costos
            costo_mes = costo_normal_mes + costo_extra_mes + costo_almacen_mes
            costo_total += costo_mes

            # Registro de costos detallados
            costos_detalle.append([
                meses[i],
                produccion_normal,
                produccion_extra,
                demanda_mes,
                inventario,
                round(costo_normal_mes, 2),
                round(costo_extra_mes, 2),
                round(costo_almacen_mes, 2),
                round(costo_mes, 2),
            ])

        # Mostrar resultados en la interfaz
        for row in tree.get_children():
            tree.delete(row)
        
        for detalle in costos_detalle:
            tree.insert("", "end", values=detalle)
        
        total_label.config(text=f"Costo Total: {round(costo_total, 2)} USD")

    except ValueError as e:
        total_label.config(text=f"Error: {e}")

# Datos base
meses = ["Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre"]
costo_normal = 6
costo_extra = 9
costo_almacenamiento = 0.15
almacen_inicial = 10

# Crear ventana principal
root = tk.Tk()
root.title("Cálculo de Costos")
root.geometry("900x500")

# Título
title = tk.Label(root, text="Cálculo de Costos Mensuales", font=("Arial", 16))
title.pack(pady=10)

# Sección de entrada de datos
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Producción Normal (separada por comas):").grid(row=0, column=0, sticky="w")
normal_entries = tk.Entry(frame, width=50)
normal_entries.grid(row=0, column=1)

tk.Label(frame, text="Producción Extra (separada por comas):").grid(row=1, column=0, sticky="w")
extra_entries = tk.Entry(frame, width=50)
extra_entries.grid(row=1, column=1)

tk.Label(frame, text="Demanda (separada por comas):").grid(row=2, column=0, sticky="w")
demanda_entries = tk.Entry(frame, width=50)
demanda_entries.grid(row=2, column=1)

# Tabla para mostrar resultados
columns = ["Mes", "Producción Normal", "Producción Extra", "Demanda", "Inventario Final", 
           "Costo Normal", "Costo Extra", "Costo Almacenamiento", "Costo Total Mes"]
tree = ttk.Treeview(root, columns=columns, show="headings", height=10)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100, anchor="center")

tree.pack(pady=10, fill="x")

# Botón para calcular
calculate_button = tk.Button(root, text="Calcular Costos", command=calcular_costos)
calculate_button.pack(pady=10)

# Etiqueta para costo total
total_label = tk.Label(root, text="Costo Total: 0 USD", font=("Arial", 14))
total_label.pack(pady=10)

# Ejecutar la interfaz
root.mainloop()
