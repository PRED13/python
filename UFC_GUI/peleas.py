import tkinter as tk
from tkinter import ttk, messagebox
from database import execute_query, fetch_query

tree_peleas = None  # Treeview global


def registrar_pelea_gui(tab):
    """Muestra formulario y Treeview con TODAS las columnas de la tabla Peleas"""
    global tree_peleas

    # Frame para formulario
    form_frame = tk.LabelFrame(tab, text="Ingresar nueva pelea", padx=10, pady=10)
    form_frame.pack(fill="x", padx=10, pady=10)

    entradas = {}

    # ======= CAMPOS ======= #
    # IdEvento (texto normal)
    tk.Label(form_frame, text="IdEvento").grid(row=0, column=0, sticky="e", pady=2)
    id_evento_var = tk.StringVar()
    tk.Entry(form_frame, textvariable=id_evento_var, width=30).grid(row=0, column=1, pady=2)
    entradas["IdEvento"] = id_evento_var

    # PELEADOR 1
    tk.Label(form_frame, text="Peleador 1").grid(row=1, column=0, sticky="e", pady=2)
    peleadores = fetch_query("SELECT IdPeleador, Nombre FROM Peleadores WHERE EstadoActivo=1")
    peleador1_var = tk.StringVar()
    combo1 = ttk.Combobox(form_frame, textvariable=peleador1_var, width=30,
                          values=[f"{p[0]} - {p[1]}" for p in peleadores])
    combo1.grid(row=1, column=1, pady=2)
    entradas["IdPeleador1"] = peleador1_var

    # PELEADOR 2
    tk.Label(form_frame, text="Peleador 2").grid(row=2, column=0, sticky="e", pady=2)
    peleador2_var = tk.StringVar()
    combo2 = ttk.Combobox(form_frame, textvariable=peleador2_var, width=30,
                          values=[f"{p[0]} - {p[1]}" for p in peleadores])
    combo2.grid(row=2, column=1, pady=2)
    entradas["IdPeleador2"] = peleador2_var

    # GANADOR (también un combobox con los dos + empate)
    tk.Label(form_frame, text="Ganador (0 = Empate)").grid(row=3, column=0, sticky="e", pady=2)
    ganador_var = tk.StringVar()
    combo_ganador = ttk.Combobox(form_frame, textvariable=ganador_var, width=30,
                                 values=["0 - Empate"] + [f"{p[0]} - {p[1]}" for p in peleadores])
    combo_ganador.grid(row=3, column=1, pady=2)
    entradas["Ganador"] = ganador_var

    # Método
    tk.Label(form_frame, text="Método").grid(row=4, column=0, sticky="e", pady=2)
    metodo_var = tk.StringVar()
    tk.Entry(form_frame, textvariable=metodo_var, width=30).grid(row=4, column=1, pady=2)
    entradas["Metodo"] = metodo_var

    # Ronda
    tk.Label(form_frame, text="Ronda").grid(row=5, column=0, sticky="e", pady=2)
    ronda_var = tk.StringVar()
    tk.Entry(form_frame, textvariable=ronda_var, width=30).grid(row=5, column=1, pady=2)
    entradas["Ronda"] = ronda_var

    # Duración en segundos
    tk.Label(form_frame, text="Duración (segundos)").grid(row=6, column=0, sticky="e", pady=2)
    duracion_var = tk.StringVar()
    tk.Entry(form_frame, textvariable=duracion_var, width=30).grid(row=6, column=1, pady=2)
    entradas["DuracionSegundos"] = duracion_var

    # Tipo de pelea
    tk.Label(form_frame, text="TipoPelea").grid(row=7, column=0, sticky="e", pady=2)
    tipo_var = tk.StringVar()
    tk.Entry(form_frame, textvariable=tipo_var, width=30).grid(row=7, column=1, pady=2)
    entradas["TipoPelea"] = tipo_var

    # Botón guardar
    tk.Button(
        form_frame, text="Guardar Pelea", bg="green", fg="white",
        command=lambda: guardar_pelea(entradas)
    ).grid(row=8, column=0, columnspan=2, pady=10)

    # ======= TREEVIEW ======= #
    columnas = ("IdPelea", "IdEvento", "IdPeleador1", "IdPeleador2",
                "Ganador", "Metodo", "Ronda", "DuracionSegundos", "TipoPelea")

    tree_peleas = ttk.Treeview(tab, columns=columnas, show="headings")

    for col in columnas:
        tree_peleas.heading(col, text=col)
        tree_peleas.column(col, width=120, anchor="center")

    tree_peleas.pack(expand=1, fill="both", padx=10, pady=10)

    refrescar_peleas()


def guardar_pelea(entradas):
    """Inserta una nueva pelea en la base de datos"""
    try:
        # Convertir valores
        id_evento = entradas["IdEvento"].get().strip()

        id1_text = entradas["IdPeleador1"].get()
        id2_text = entradas["IdPeleador2"].get()
        ganador_text = entradas["Ganador"].get()

        if not id1_text or not id2_text or not ganador_text:
            messagebox.showerror("Error", "Debe seleccionar los peleadores y el ganador.")
            return

        id1 = int(id1_text.split(" - ")[0])
        id2 = int(id2_text.split(" - ")[0])
        ganador_id = 0 if ganador_text.startswith("0") else int(ganador_text.split(" - ")[0])

        metodo = entradas["Metodo"].get().strip()
        ronda = int(entradas["Ronda"].get())
        duracion = int(entradas["DuracionSegundos"].get())
        tipo = entradas["TipoPelea"].get().strip()

        if id1 == id2:
            messagebox.showerror("Error", "Un peleador no puede pelear contra sí mismo.")
            return

        query = """
        INSERT INTO Peleas (IdEvento, IdPeleador1, IdPeleador2, Ganador, Metodo, Ronda, DuracionSegundos, TipoPelea)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        execute_query(query, (id_evento, id1, id2, ganador_id if ganador_id != 0 else None,
                              metodo, ronda, duracion, tipo))

        messagebox.showinfo("Éxito", "Pelea registrada correctamente")
        refrescar_peleas()

        # Limpiar campos
        for v in entradas.values():
            v.set("")

    except Exception as e:
        messagebox.showerror("Error", str(e))


def refrescar_peleas():
    """Refresca el Treeview con los datos exactos de la tabla Peleas"""
    global tree_peleas
    if tree_peleas:
        tree_peleas.delete(*tree_peleas.get_children())

        data = fetch_query("""
            SELECT IdPelea, IdEvento, IdPeleador1, IdPeleador2, Ganador,
                   Metodo, Ronda, DuracionSegundos, TipoPelea
            FROM Peleas
        """)

        for row in data:
            tree_peleas.insert("", tk.END, values=row)
