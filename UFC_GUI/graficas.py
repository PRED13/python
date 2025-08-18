import tkinter as tk
from database import fetch_query
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def mostrar_dashboard(tab):
    frame = tk.Frame(tab)
    frame.pack(fill='both', expand=1)

    tk.Label(frame, text="Dashboard de Ranking y Estadísticas", font=("Arial", 16)).pack(pady=10)

    data = fetch_query("SELECT Nombre, Victorias, Derrotas, Empates FROM Peleadores ORDER BY Victorias DESC")
    nombres = [d[0] for d in data]
    victorias = [d[1] for d in data]
    derrotas = [d[2] for d in data]
    empates = [d[3] for d in data]

    fig, ax = plt.subplots(figsize=(8,4))
    ax.bar(nombres, victorias, color='green', label='Victorias')
    ax.bar(nombres, derrotas, bottom=victorias, color='red', label='Derrotas')
    ax.bar(nombres, empates, bottom=[i+j for i,j in zip(victorias, derrotas)], color='gray', label='Empates')
    ax.set_ylabel('Cantidad de Peleas')
    ax.set_title('Ranking de Peleadores')
    ax.legend()
    plt.xticks(rotation=45, ha='right')

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=1)
