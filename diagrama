import tkinter as tk
import matplotlib.pyplot as plt
import networkx as nx

# Crear una ventana para la interfaz gráfica
root = tk.Tk()
root.title("Diseño de base de datos - Escuela Secundaria")

# Función para generar y mostrar la gráfica de entidad-relación
def generar_grafica():
    # Crear un grafo dirigido para representar las entidades y relaciones
    G = nx.DiGraph()

    # Agregar entidades (nodos)
    G.add_node("Profesor", shape="box", style="filled", fillcolor="lightblue")
    G.add_node("Modulo", shape="ellipse", style="filled", fillcolor="lightgreen")
    G.add_node("Alumno", shape="ellipse", style="filled", fillcolor="lightyellow")
    G.add_node("Curso", shape="ellipse", style="filled", fillcolor="lightcoral")

    # Agregar relaciones (aristas)
    G.add_edge("Profesor", "Modulo", label="Imparte")
    G.add_edge("Modulo", "Alumno", label="Matricula")
    G.add_edge("Alumno", "Curso", label="Pertenece a")
    G.add_edge("Curso", "Alumno", label="Jefe de grupo")

    # Posicionar los nodos para una visualización clara
    pos = {
        "Profesor": (0, 1),
        "Modulo": (1, 1),
        "Alumno": (2, 1),
        "Curso": (1, 0)
    }

    # Dibujar la gráfica
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=10, font_weight="bold", arrows=True)

    # Mostrar las etiquetas de las relaciones
    edge_labels = nx.get_edge_attributes(G, "label")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Mostrar el gráfico en una ventana emergente
    plt.title("Gráfica de Entidad-Relación - Escuela Secundaria")
    plt.show()

# Crear un botón para generar la gráfica
btn_generar = tk.Button(root, text="Generar Gráfica de Entidad-Relación", command=generar_grafica)
btn_generar.pack(pady=20)

# Iniciar la interfaz gráfica
root.mainloop()

