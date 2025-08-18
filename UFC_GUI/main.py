import tkinter as tk
from tkinter import ttk
from peleadores import agregar_peleador_gui
from peleas import registrar_pelea_gui
from graficas import mostrar_dashboard

def main():
    root = tk.Tk()
    root.title("Sistema UFC - Versión 2.0")
    root.geometry("1000x600")

    tab_control = ttk.Notebook(root)

    tab1 = ttk.Frame(tab_control)
    tab2 = ttk.Frame(tab_control)
    tab3 = ttk.Frame(tab_control)

    tab_control.add(tab1, text='Peleadores')
    tab_control.add(tab2, text='Peleas')
    tab_control.add(tab3, text='Dashboard')

    agregar_peleador_gui(tab1)
    registrar_pelea_gui(tab2)
    mostrar_dashboard(tab3)

    tab_control.pack(expand=1, fill='both')
    root.mainloop()

if __name__ == "__main__":
    main()
