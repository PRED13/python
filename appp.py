import os
import socket
import threading
import tkinter as tk
from tkinter import filedialog, messagebox

# Configuración del servidor
HOST = '127.0.0.1'  # Cambiar por la IP de tu red
PORT = 5000
BUFFER_SIZE = 1024

# Función para manejar la recepción de archivos
def start_server():
    def handle_client(conn, addr):
        print(f"Conexión establecida con {addr}")
        with conn:
            # Recibir el nombre del archivo
            file_name = conn.recv(BUFFER_SIZE).decode()
            print(f"Recibiendo archivo: {file_name}")
            # Recibir el archivo
            with open(file_name, 'wb') as f:
                while True:
                    data = conn.recv(BUFFER_SIZE)
                    if not data:
                        break
                    f.write(data)

            print(f"Archivo recibido: {file_name}")

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Servidor escuchando en {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()

# Función para enviar un archivo
def send_file(file_path, target_ip):
    try:
        file_name = os.path.basename(file_path)
        file_size = os.path.getsize(file_path)

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((target_ip, PORT))

        # Enviar el nombre del archivo
        client.send(file_name.encode())

        # Enviar el archivo
        with open(file_path, 'rb') as f:
            while True:
                data = f.read(BUFFER_SIZE)
                if not data:
                    break
                client.send(data)

        print(f"Archivo enviado: {file_name} ({file_size} bytes)")
        client.close()

    except Exception as e:
        print(f"Error al enviar archivo: {e}")

# Función para seleccionar un archivo y enviarlo
def select_file():
    file_path = filedialog.askopenfilename(title="Selecciona un archivo")
    if not file_path:
        return
    target_ip = entry_ip.get()
    if not target_ip:
        messagebox.showerror("Error", "Por favor, ingrese la dirección IP del dispositivo de destino.")
        return
    send_file(file_path, target_ip)

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Transferencia de Archivos")
root.geometry("400x200")

frame = tk.Frame(root, width=400, height=150, bg="lightgray")
frame.pack_propagate(False)
frame.pack(pady=10)

label = tk.Label(frame, text="Selecciona un archivo para enviarlo", bg="lightgray")
label.pack(expand=True)

entry_ip = tk.Entry(root, width=30)
entry_ip.pack(pady=5)
entry_ip.insert(0, "Dirección IP del receptor")

button_select = tk.Button(root, text="Seleccionar Archivo", command=select_file)
button_select.pack(pady=10)

# Iniciar el servidor en un hilo separado
server_thread = threading.Thread(target=start_server, daemon=True)
server_thread.start()

root.mainloop()

