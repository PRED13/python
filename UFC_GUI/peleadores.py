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

    # Botón para eliminar
    tk.Button(frame_formulario, text="Eliminar Peleador", command=eliminar_peleador).grid(row=len(campos)+1, column=0, columnspan=2, pady=5)

    # Crear un frame para la tabla y las barras de desplazamiento
    frame_tabla = tk.Frame(tab)
    frame_tabla.pack(expand=1, fill='both', padx=10, pady=10)

    # Configurar todas las 9 columnas para el Treeview
    columnas_treeview = ('IdPeleador', 'Nombre', 'Nacionalidad', 'CategoriaPeso', 'Peso', 'EstiloCombate', 'Altura', 'AlcanceBrazo', 'Entrenador', 'Gimnasio')
    
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

    # Ajustar las columnas para mostrar solo las que nos interesan
    tree_peleadores.heading('IdPeleador', text='IdPeleador')
    tree_peleadores.column('IdPeleador', width=0, stretch=tk.NO) # Hacemos la columna del ID invisible

    tree_peleadores.heading('Nombre', text='Nombre', anchor='center')
    tree_peleadores.column('Nombre', anchor='center', width=120)
    
    tree_peleadores.heading('Nacionalidad', text='Nacionalidad', anchor='center')
    tree_peleadores.column('Nacionalidad', anchor='center', width=120)
    
    tree_peleadores.heading('CategoriaPeso', text='CategoriaPeso', anchor='center')
    tree_peleadores.column('CategoriaPeso', anchor='center', width=120)

    tree_peleadores.heading('Peso', text='Peso', anchor='center')
    tree_peleadores.column('Peso', anchor='center', width=120)
    
    tree_peleadores.heading('EstiloCombate', text='EstiloCombate', anchor='center')
    tree_peleadores.column('EstiloCombate', anchor='center', width=120)

    tree_peleadores.heading('Altura', text='Altura', anchor='center')
    tree_peleadores.column('Altura', anchor='center', width=120)
    
    tree_peleadores.heading('AlcanceBrazo', text='AlcanceBrazo', anchor='center')
    tree_peleadores.column('AlcanceBrazo', anchor='center', width=120)

    tree_peleadores.heading('Entrenador', text='Entrenador', anchor='center')
    tree_peleadores.column('Entrenador', anchor='center', width=120)
    
    tree_peleadores.heading('Gimnasio', text='Gimnasio', anchor='center')
    tree_peleadores.column('Gimnasio', anchor='center', width=120)

    refrescar_peleadores()

def refrescar_peleadores():
    global tree_peleadores
    if tree_peleadores:
        for row in tree_peleadores.get_children():
            tree_peleadores.delete(row)

        query = """
            -- Agrega IdPeleador a la consulta
            SELECT IdPeleador, Nombre, Nacionalidad, CategoriaPeso, Peso, EstiloCombate, Altura, AlcanceBrazo, Entrenador, Gimnasio
            FROM Peleadores
            ORDER BY Nombre ASC
        """
        data = fetch_query(query)

        for row_data in data:
            fila_para_treeview = (
                row_data[0], # IdPeleador
                row_data[1], # Nombre
                row_data[2], # Nacionalidad
                row_data[3], # CategoriaPeso
                row_data[4], # Peso
                row_data[5], # EstiloCombate
                row_data[6], # Altura
                row_data[7], # AlcanceBrazo
                row_data[8], # Entrenador
                row_data[9]  # Gimnasio
            )
            tree_peleadores.insert('', tk.END, values=fila_para_treeview)

def eliminar_peleador():
    """
    Función para eliminar la fila seleccionada del Treeview y de la base de datos.
    """
    global tree_peleadores
    seleccion = tree_peleadores.selection()

    if not seleccion:
        messagebox.showwarning("Advertencia", "Por favor, selecciona una fila para eliminar.")
        return

    item = tree_peleadores.item(seleccion[0])
    
    # El ID es el primer valor en la lista de valores de la fila
    id_peleador = item['values'][0] 
    
    # El nombre se usa para el mensaje de confirmación
    nombre_peleador = item['values'][1] 

    try:
        # Verifica si el peleador está en la tabla de Peleas.
        query_verificar = "SELECT COUNT(*) FROM Peleas WHERE IdPeleador1 = ? OR IdPeleador2 = ?"
        
        # Se asegura de que el ID es de tipo entero para la consulta SQL
        peleas_referenciadas = fetch_query(query_verificar, (id_peleador, id_peleador))
        
        if peleas_referenciadas and peleas_referenciadas[0][0] > 0:
            messagebox.showerror("Error", "No se puede eliminar este peleador porque está referenciado en las peleas.")
            return

    except Exception as e:
        messagebox.showerror("Error de Verificación", f"Ocurrió un error al verificar las referencias: {str(e)}")
        return

    # Confirmar la eliminación con el usuario
    if messagebox.askyesno("Confirmar Eliminación", f"¿Estás seguro de que deseas eliminar a {nombre_peleador}?"):
        try:
            query_eliminar = "DELETE FROM Peleadores WHERE IdPeleador = ?"
            execute_query(query_eliminar, (id_peleador,))
            messagebox.showinfo("Éxito", f"Peleador {nombre_peleador} eliminado correctamente.")
            refrescar_peleadores()
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al intentar eliminar al peleador: {str(e)}")