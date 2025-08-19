import tkinter as tk
from tkinter import ttk, messagebox
from database import execute_query, fetch_query

tree_peleas = None  # Treeview global


def registrar_pelea_gui(tab):
    """Crea el formulario y Treeview para manejar la tabla Peleas"""
    global tree_peleas

    # Frame de formulario
    frame_form = tk.Frame(tab)
    frame_form.pack(pady=10)

    # ---- Campos del formulario ----
    tk.Label(frame_form, text="IdEvento:").grid(row=0, column=0, padx=5, pady=5)
    entry_evento = tk.Entry(frame_form)
    entry_evento.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame_form, text="Peleador 1:").grid(row=1, column=0, padx=5, pady=5)
    peleador1_cb = ttk.Combobox(frame_form, state="readonly")
    peleador1_cb.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(frame_form, text="Peleador 2:").grid(row=2, column=0, padx=5, pady=5)
    peleador2_cb = ttk.Combobox(frame_form, state="readonly")
    peleador2_cb.grid(row=2, column=1, padx=5, pady=5)
    
    # ---- Botón de Actualizar ----
    btn_actualizar = tk.Button(
        frame_form,
        text="Actualizar Peleadores",
        command=lambda: llenar_peleadores(peleador1_cb, peleador2_cb)
    )
    btn_actualizar.grid(row=2, column=2, padx=5, pady=5) # Colocado al lado de los combobox

    tk.Label(frame_form, text="Ganador:").grid(row=3, column=0, padx=5, pady=5)
    entry_ganador = tk.Entry(frame_form)
    entry_ganador.grid(row=3, column=1, padx=5, pady=5)

    tk.Label(frame_form, text="Método:").grid(row=4, column=0, padx=5, pady=5)
    entry_metodo = tk.Entry(frame_form)
    entry_metodo.grid(row=4, column=1, padx=5, pady=5)

    tk.Label(frame_form, text="Ronda:").grid(row=5, column=0, padx=5, pady=5)
    entry_ronda = tk.Entry(frame_form)
    entry_ronda.grid(row=5, column=1, padx=5, pady=5)

    tk.Label(frame_form, text="Duración (segundos):").grid(row=6, column=0, padx=5, pady=5)
    entry_duracion = tk.Entry(frame_form)
    entry_duracion.grid(row=6, column=1, padx=5, pady=5)

    tk.Label(frame_form, text="Tipo de Pelea:").grid(row=7, column=0, padx=5, pady=5)
    entry_tipo = tk.Entry(frame_form)
    entry_tipo.grid(row=7, column=1, padx=5, pady=5)

    # Botón guardar
    btn_guardar = tk.Button(
        frame_form,
        text="Guardar Pelea",
        bg="green",
        fg="white",
        command=lambda: guardar_pelea(
            entry_evento,
            peleador1_cb,
            peleador2_cb,
            entry_ganador,
            entry_metodo,
            entry_ronda,
            entry_duracion,
            entry_tipo,
        ),
    )
    btn_guardar.grid(row=8, column=0, columnspan=2, pady=10)

    # ---- Treeview ----
    columnas = (
        "IdPelea",
        "IdEvento",
        "IdPeleador1",
        "IdPeleador2",
        "Ganador",
        "Metodo",
        "Ronda",
        "DuracionSegundos",
        "TipoPelea",
    )

    tree_peleas = ttk.Treeview(tab, columns=columnas, show="headings", selectmode="extended")

    for col in columnas:
        tree_peleas.heading(col, text=col)
        tree_peleas.column(col, width=120, anchor="center")

    tree_peleas.pack(expand=1, fill="both", padx=10, pady=10)

    # Botón eliminar
    btn_eliminar = tk.Button(tab, text="Eliminar Pelea(s)", bg="red", fg="white", command=eliminar_pelea)
    btn_eliminar.pack(pady=5)

    # Llenar peleadores en los combobox al iniciar
    llenar_peleadores(peleador1_cb, peleador2_cb)

    # Refrescar tabla
    refrescar_peleas()


def llenar_peleadores(cb1, cb2):
    """Llena los combobox con los IdPeleador existentes en la tabla Peleadores"""
    try:
        peleadores = fetch_query("SELECT IdPeleador, Nombre FROM Peleadores")
        ids = [f"{row[0]} - {row[1]}" for row in peleadores]
        cb1["values"] = ids
        cb2["values"] = ids
        messagebox.showinfo("Actualización", "Lista de peleadores actualizada correctamente.")
    except Exception as e:
        messagebox.showerror("Error de Actualización", f"No se pudo actualizar la lista de peleadores.\n{e}")

# ... (El resto del código como guardar_pelea, refrescar_peleas y eliminar_pelea se mantiene igual)
def guardar_pelea(entry_evento, cb1, cb2, entry_ganador, entry_metodo, entry_ronda, entry_duracion, entry_tipo):
    """Inserta una nueva pelea en la BD"""
    try:
        id_evento = entry_evento.get()
        id_peleador1 = cb1.get().split(" - ")[0] if cb1.get() else None
        id_peleador2 = cb2.get().split(" - ")[0] if cb2.get() else None
        ganador = entry_ganador.get()
        metodo = entry_metodo.get()
        ronda = entry_ronda.get()
        duracion = entry_duracion.get()
        tipo = entry_tipo.get()

        if not id_evento or not id_peleador1 or not id_peleador2:
            messagebox.showwarning("Error", "Debes llenar todos los campos obligatorios.")
            return

        query = """
            INSERT INTO Peleas (IdEvento, IdPeleador1, IdPeleador2, Ganador, Metodo, Ronda, DuracionSegundos, TipoPelea)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        execute_query(query, (id_evento, id_peleador1, id_peleador2, ganador, metodo, ronda, duracion, tipo))

        messagebox.showinfo("Éxito", "Pelea registrada correctamente.")
        refrescar_peleas()
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar la pelea.\n{e}")


def refrescar_peleas():
    """Carga todas las peleas en el Treeview"""
    global tree_peleas
    if tree_peleas:
        for row in tree_peleas.get_children():
            tree_peleas.delete(row)

        data = fetch_query(
            "SELECT IdPelea, IdEvento, IdPeleador1, IdPeleador2, Ganador, Metodo, Ronda, DuracionSegundos, TipoPelea FROM Peleas"
        )
        for row in data:
            tree_peleas.insert("", tk.END, values=row)


def eliminar_pelea():
    """Elimina una o varias peleas seleccionadas del Treeview y la BD"""
    global tree_peleas

    seleccion = tree_peleas.selection()
    if not seleccion:
        messagebox.showwarning("Atención", "Debes seleccionar al menos una pelea para eliminar.")
        return

    if not messagebox.askyesno("Confirmar", "¿Seguro que deseas eliminar las peleas seleccionadas?"):
        return

    try:
        for item in seleccion:
            pelea = tree_peleas.item(item, "values")
            id_pelea = pelea[0]
            
            query = "DELETE FROM Peleas WHERE IdPelea = ?"
            execute_query(query, (id_pelea,))

        refrescar_peleas()
        messagebox.showinfo("Éxito", "Pelea(s) eliminada(s) correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudieron eliminar las peleas.\n{e}")