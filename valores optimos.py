import tkinter as tk
from tkinter import ttk, messagebox
from scipy.optimize import linprog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Resolver problema
def resolver_simplex():
    try:
        c = [-20, -30, -25]
        A = [
            [1, 1, 3],
            [1, 2, 1],
            [1, 1, 1]
        ]
        b = [600, 500, 300]
        res = linprog(c, A_ub=A, b_ub=b, method='simplex')

        if res.success:
            x1, x2, x3 = res.x
            z = -res.fun

            resumen = (
                f"{'VARIABLE':<15}{'DESCRIPCIÓN':<30}{'VALOR ÓPTIMO'}\n"
                f"{'-'*65}\n"
                f"{'x1':<15}{'Sillas a fabricar':<30}{x1:10.2f}\n"
                f"{'x2':<15}{'Mesas a fabricar':<30}{x2:10.2f}\n"
                f"{'x3':<15}{'Librerías a fabricar':<30}{x3:10.2f}\n"
                f"{'-'*65}\n"
                f"{'Z':<15}{'Ganancia total':<30}${z:10,.2f} MXN\n"
            )

            text_resultado.config(state='normal')
            text_resultado.delete("1.0", tk.END)
            text_resultado.insert(tk.END, resumen)
            text_resultado.config(state='disabled')

            mostrar_grafica(["Sillas", "Mesas", "Librerías"], [x1, x2, x3], [20, 30, 25])
        else:
            messagebox.showerror("Resultado", "❌ No se encontró solución óptima.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Mostrar gráfica
def mostrar_grafica(productos, cantidades, precios_unitarios):
    for widget in frame_grafica.winfo_children():
        widget.destroy()

    ganancias = [cantidades[i] * precios_unitarios[i] for i in range(len(productos))]

    colores = ["#5E60CE", "#64C9CF", "#F9A620"]  # Diferentes colores para cada barra

    fig, ax = plt.subplots(figsize=(6.5, 4), dpi=100)
    bars = ax.bar(productos, ganancias, color=colores, edgecolor="#2E2E2E", width=0.5)

    ax.set_title("Ganancia por Tipo de Producto", fontsize=14, weight='bold', color="#2E2E2E")
    ax.set_ylabel("Ganancia ($)", fontsize=11, color="#2E2E2E")
    ax.set_ylim(0, max(ganancias) * 1.25)

    # Agregar valores sobre las barras
    for bar, value in zip(bars, ganancias):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            value + (max(ganancias) * 0.04),
            f"${value:,.0f}",
            ha='center',
            va='bottom',
            fontsize=11,
            color="#2E2E2E",
            fontweight='bold'
        )

    # Estética general
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_facecolor("#FFFFFF")
    fig.patch.set_facecolor("#FFFFFF")

    canvas = FigureCanvasTkAgg(fig, master=frame_grafica)
    canvas.draw()
    canvas.get_tk_widget().pack()


# === Interfaz principal ===
ventana = tk.Tk()
ventana.title("Optimización de Producción con Método Simplex")
ventana.geometry("720x660")
ventana.configure(bg="#F2F4F8")
ventana.resizable(False, False)

# Título
tk.Label(
    ventana, text="📈 Optimización de Producción (Método Simplex)",
    font=("Segoe UI", 16, "bold"), bg="#F2F4F8", fg="#2E2E2E"
).pack(pady=15)

# Botón personalizado
def on_enter(e): btn.config(bg="#004C99")
def on_leave(e): btn.config(bg="#0066CC")

btn = tk.Button(
    ventana, text="Calcular Solución Óptima", font=("Segoe UI", 12, "bold"),
    bg="#0066CC", fg="white", activebackground="#004C99",
    relief="flat", padx=20, pady=10, command=resolver_simplex
)
btn.bind("<Enter>", on_enter)
btn.bind("<Leave>", on_leave)
btn.pack(pady=5)

# Frame de resultados
frame_resultado = tk.LabelFrame(
    ventana, text="📋 Informe de Resultados", font=("Segoe UI", 11, "bold"),
    padx=12, pady=10, bg="#FFFFFF", fg="#2E2E2E"
)
frame_resultado.pack(pady=10)

text_resultado = tk.Text(frame_resultado, height=10, width=80, font=("Consolas", 10), bg="#F9F9F9", bd=0, fg="#2E2E2E")
text_resultado.pack()
text_resultado.config(state='disabled')

# Frame gráfica
frame_grafica = tk.LabelFrame(
    ventana, text="📊 Visualización de Ganancias", font=("Segoe UI", 11, "bold"),
    padx=10, pady=10, bg="#FFFFFF", fg="#2E2E2E"
)
frame_grafica.pack(pady=10)

# Footer
tk.Label(
    ventana, text="© J.C S.M | Investigación de Operaciones 2025",
    font=("Segoe UI", 8), bg="#F2F4F8", fg="#666666"
).pack(pady=15)

ventana.mainloop()
