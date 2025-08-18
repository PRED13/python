import tkinter as tk
from tkinter import ttk, messagebox
from database import execute_query, fetch_query

# Treeview global para mostrar las peleas
tree_peleas = None

def registrar_pelea_gui(tab):
    """
    Crea el formulario para registrar peleas en la pestaña especificada (tab)
    y muestra un Treeview de peleas que se actualiza automáticamente.
    """
    global tree_peleas
    frame = tk.Frame(tab)
    frame.pack(pady=10)

    # Obtener peleadores activos
    peleadores = fetch_query("SELECT IdPeleador, Nombre FROM Peleadores WHERE EstadoActivo=1")
    peleadores_dict = {str(p[0]): p[1] for p in peleadores}

    # Selección de peleadores
    tk.Label(frame, text="Peleador 1").grid(row=0, column=0)
    id1_var = tk.StringVar()
    ttk.Combobox(frame, textvariable=id1_var, values=list(peleadores_dict.keys())).grid(row=0, column=1)

    tk.Label(frame, text="Peleador 2").grid(row=1, column=0)
    id2_var = tk.StringVar()
    ttk.Combobox(frame, textvariable=id2_var, values=list(peleadores_dict.keys())).grid(row=1, column=1)

    # Selección de evento
    tk.Label(frame, text="Id Evento").grid(row=2, column=0)
    evento_id_var = tk.StringVar()
    tk.Entry(frame, textvariable=evento_id_var).grid(row=2, column=1)
    
    tk.Label(frame, text="Nombre Evento (si es nuevo)").grid(row=3, column=0)
    evento_nombre_var = tk.StringVar()
    tk.Entry(frame, textvariable=evento_nombre_var).grid(row=3, column=1)

    # Ganador y detalles de la pelea
    tk.Label(frame, text="Ganador (0 si empate)").grid(row=4, column=0)
    ganador_var = tk.StringVar()
    tk.Entry(frame, textvariable=ganador_var).grid(row=4, column=1)

    tk.Label(frame, text="Método").grid(row=5, column=0)
    metodo_var = tk.StringVar()
    tk.Entry(frame, textvariable=metodo_var).grid(row=5, column=1)

    tk.Label(frame, text="Ronda").grid(row=6, column=0)
    ronda_var = tk.StringVar()
    tk.Entry(frame, textvariable=ronda_var).grid(row=6, column=1)

    tk.Label(frame, text="Duración (segundos)").grid(row=7, column=0)
    duracion_var = tk.StringVar()
    tk.Entry(frame, textvariable=duracion_var).grid(row=7, column=1)
    
    # Botón para guardar la pelea
    tk.Button(frame, text="Registrar Pelea", command=lambda: guardar_pelea(id1_var, id2_var, evento_id_var, evento_nombre_var, ganador_var, metodo_var, ronda_var, duracion_var)).grid(row=8, column=0, columnspan=2, pady=10)

    # Treeview para mostrar peleas
    tree_peleas = ttk.Treeview(tab, columns=('Evento', 'Peleador1', 'Peleador2', 'Ganador', 'Metodo'), show='headings')
    for col in tree_peleas['columns']:
        tree_peleas.heading(col, text=col)
    tree_peleas.pack(expand=1, fill='both', padx=10, pady=10)

    refrescar_peleas()

def guardar_pelea(id1_var, id2_var, evento_id_var, evento_nombre_var, ganador_var, metodo_var, ronda_var, duracion_var):
    """
    Guarda una pelea en la base de datos y actualiza estadísticas.
    """
    try:
        id1 = int(id1_var.get())
        id2 = int(id2_var.get())
        id_evento = int(evento_id_var.get())
        nombre_evento = evento_nombre_var.get()
        ganador_id = int(ganador_var.get())
        metodo = metodo_var.get()
        ronda = int(ronda_var.get())
        duracion = int(duracion_var.get())

        # Validar que el ID del ganador sea válido
        if ganador_id not in [id1, id2, 0]:
            messagebox.showerror("Error", "El ID del ganador debe ser el del Peleador 1, Peleador 2 o 0 para empate.")
            return

        # Verificar y/o crear el evento si es nuevo
        check_event_query = "SELECT IdEvento, NombreEvento FROM Eventos WHERE IdEvento = ?"
        existing_event = fetch_query(check_event_query, (id_evento,))

        if not existing_event:
            if not nombre_evento:
                messagebox.showerror("Error", "Debe proporcionar un nombre para el nuevo evento.")
                return
            insert_event_query = "INSERT INTO Eventos (IdEvento, NombreEvento) VALUES (?, ?)"
            execute_query(insert_event_query, (id_evento, nombre_evento))
        elif nombre_evento and existing_event[0][1] != nombre_evento:
            # Opcional: Actualizar nombre si el ID existe pero el nombre es diferente
            update_event_query = "UPDATE Eventos SET NombreEvento = ? WHERE IdEvento = ?"
            execute_query(update_event_query, (nombre_evento, id_evento))

        # Determinar el valor del ganador para la base de datos (None para empate)
        ganador_db = None if ganador_id == 0 else ganador_id

        # Insertar pelea
        query = """INSERT INTO Peleas
                   (IdEvento, IdPeleador1, IdPeleador2, Ganador, Metodo, Ronda, DuracionSegundos)
                   VALUES (?, ?, ?, ?, ?, ?, ?)"""
        execute_query(query, (id_evento, id1, id2, ganador_db, metodo, ronda, duracion))

        # Actualizar estadísticas de victorias/derrotas/empates
        if ganador_id == 0:
            execute_query("UPDATE Peleadores SET Empates=Empates+1 WHERE IdPeleador IN (?, ?)", (id1, id2))
        else:
            loser = id2 if ganador_id == id1 else id1
            execute_query("UPDATE Peleadores SET Victorias=Victorias+1 WHERE IdPeleador=?", (ganador_id,))
            execute_query("UPDATE Peleadores SET Derrotas=Derrotas+1 WHERE IdPeleador=?", (loser,))

        messagebox.showinfo("Éxito", "Pelea registrada correctamente")
        refrescar_peleas()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def refrescar_peleas():
    """
    Refresca el Treeview de peleas mostrando todas las peleas registradas.
    """
    global tree_peleas
    if tree_peleas:
        # Limpiar Treeview
        for row in tree_peleas.get_children():
            tree_peleas.delete(row)

        # Traer datos de peleas con nombres de peleadores y eventos
        data = fetch_query("""
            SELECT E.NombreEvento, P1.Nombre, P2.Nombre,
                   CASE WHEN Peleas.Ganador IS NULL THEN 'Empate' 
                        ELSE (SELECT Nombre FROM Peleadores WHERE IdPeleador = Peleas.Ganador) END,
                   Peleas.Metodo
            FROM Peleas
            INNER JOIN Eventos E ON Peleas.IdEvento = E.IdEvento
            INNER JOIN Peleadores P1 ON Peleas.IdPeleador1 = P1.IdPeleador
            INNER JOIN Peleadores P2 ON Peleas.IdPeleador2 = P2.IdPeleador
        """)

        for row in data:
            tree_peleas.insert('', tk.END, values=row)