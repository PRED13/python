import tkinter as tk
from tkinter import ttk, messagebox
from database import execute_query, fetch_query

# Treeview global para poder refrescarlo
tree_peleadores = None

def agregar_peleador_gui(tab):
    global tree_peleadores
    
    frame_formulario = tk.Frame(tab)
    frame_formulario.pack(pady=10)

    campos = ['Nombre', 'Nacionalidad', 'CategoriaPeso', 'Peso', 'EstiloCombate',
              'Altura', 'AlcanceBrazo', 'Entrenador', 'Gimnasio']
    entradas = {}
    for idx, campo in enumerate(campos):
        tk.Label(frame_formulario, text=campo).grid(row=idx, column=0, sticky='e')
        entradas[campo] = tk.Entry(frame_formulario)
        entradas[campo].grid(row=idx, column=1)

    def guardar():
        try:
            query = """INSERT INTO Peleadores 
                       (Nombre, Nacionalidad, CategoriaPeso, Peso, EstiloCombate,
                        Altura, AlcanceBrazo, Entrenador, Gimnasio)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
            params = (
                entradas['Nombre'].get(),
                entradas['Nacionalidad'].get(),
                entradas['CategoriaPeso'].get(),
                float(entradas['Peso'].get()),
                entradas['EstiloCombate'].get(),
                float(entradas['Altura'].get()),
                float(entradas['AlcanceBrazo'].get()),
                entradas['Entrenador'].get(),
                entradas['Gimnasio'].get()
            )
            execute_query(query, params)
            messagebox.showinfo("Éxito", "Peleador agregado correctamente")
            for e in entradas.values():
                e.delete(0, tk.END)
            refrescar_peleadores()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(frame_formulario, text="Agregar Peleador", command=guardar).grid(row=len(campos), column=0, columnspan=2, pady=10)

    # Crear un frame para la tabla y las barras de desplazamiento
    frame_tabla = tk.Frame(tab)
    frame_tabla.pack(expand=1, fill='both', padx=10, pady=10)

    # Configurar todas las 9 columnas para el Treeview
    columnas_treeview = ('Nombre', 'Nacionalidad', 'CategoriaPeso', 'Peso', 'EstiloCombate', 'Altura', 'AlcanceBrazo', 'Entrenador', 'Gimnasio')
    
    # Crear un estilo para los bordes de las celdas
    style = ttk.Style()
    style.configure("Treeview.Heading", font=('Helvetica', 10, 'bold'))
    style.configure("Treeview", background="#ffffff", foreground="black", fieldbackground="white", bordercolor="black", relief="solid", rowheight=25)
    style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])
    
    # Crear Treeview con las nuevas columnas
    tree_peleadores = ttk.Treeview(frame_tabla, columns=columnas_treeview, show='headings')
    
    # Agregar barra de desplazamiento horizontal
    scrollbar_horizontal = ttk.Scrollbar(frame_tabla, orient='horizontal', command=tree_peleadores.xview)
    tree_peleadores.configure(xscrollcommand=scrollbar_horizontal.set)
    scrollbar_horizontal.pack(side='bottom', fill='x')

    # Agregar barra de desplazamiento vertical (opcional, pero útil)
    scrollbar_vertical = ttk.Scrollbar(frame_tabla, orient='vertical', command=tree_peleadores.yview)
    tree_peleadores.configure(yscrollcommand=scrollbar_vertical.set)
    scrollbar_vertical.pack(side='right', fill='y')

    tree_peleadores.pack(side='left', expand=1, fill='both')

    for col in columnas_treeview:
        tree_peleadores.heading(col, text=col, anchor='center')
        tree_peleadores.column(col, anchor='center', width=120)  # Establecer un ancho inicial para que el scroll funcione
    
    refrescar_peleadores()

def refrescar_peleadores():
    global tree_peleadores
    if tree_peleadores:
        for row in tree_peleadores.get_children():
            tree_peleadores.delete(row)

        query = """
            SELECT Nombre, Nacionalidad, CategoriaPeso, Peso, EstiloCombate, Altura, AlcanceBrazo, Entrenador, Gimnasio
            FROM Peleadores
            ORDER BY Nombre ASC
        """
        data = fetch_query(query)

        for row_data in data:
            fila_para_treeview = (
                row_data[0], # Nombre
                row_data[1], # Nacionalidad
                row_data[2], # CategoriaPeso
                row_data[3], # Peso
                row_data[4], # EstiloCombate
                row_data[5], # Altura
                row_data[6], # AlcanceBrazo
                row_data[7], # Entrenador
                row_data[8]  # Gimnasio
            )
            tree_peleadores.insert('', tk.END, values=fila_para_treeview)