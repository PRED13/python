import socket
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from threading import Thread

# Server-side code
def start_server():
    def handle_client(client_socket):
        try:
            # Receive file name
            file_name = client_socket.recv(1024).decode('utf-8')
            client_socket.send(b'FILENAME_RECEIVED')

            # Receive file size
            file_size = int(client_socket.recv(1024).decode('utf-8'))
            client_socket.send(b'SIZE_RECEIVED')

            # Receive file data
            with open(file_name, 'wb') as f:
                received = 0
                while received < file_size:
                    data = client_socket.recv(4096)
                    f.write(data)
                    received += len(data)
            messagebox.showinfo("File Received", f"File '{file_name}' received successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error receiving file: {e}")
        finally:
            client_socket.close()

    def server_thread():
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("0.0.0.0", 5000))
        server_socket.listen(5)
        messagebox.showinfo("Server", "Server started and waiting for connections...")

        while True:
            client_socket, addr = server_socket.accept()
            client_handler = Thread(target=handle_client, args=(client_socket,))
            client_handler.start()

    Thread(target=server_thread, daemon=True).start()

# Client-side code
def send_file():
    try:
        # Select file
        file_path = filedialog.askopenfilename()
        if not file_path:
            return

        file_name = os.path.basename(file_path)
        file_size = os.path.getsize(file_path)

        # Connect to server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip_entry.get(), 5000))

        # Send file name
        client_socket.send(file_name.encode('utf-8'))
        if client_socket.recv(1024) != b'FILENAME_RECEIVED':
            raise Exception("Filename acknowledgment failed.")

        # Send file size
        client_socket.send(str(file_size).encode('utf-8'))
        if client_socket.recv(1024) != b'SIZE_RECEIVED':
            raise Exception("Size acknowledgment failed.")

        # Send file data
        with open(file_path, 'rb') as f:
            while data := f.read(4096):
                client_socket.send(data)

        messagebox.showinfo("File Sent", f"File '{file_name}' sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error sending file: {e}")
    finally:
        client_socket.close()

# GUI Code
def create_gui():
    root = tk.Tk()
    root.title("File Transfer")

    tk.Label(root, text="Server IP:").pack(pady=5)
    global server_ip_entry
    server_ip_entry = tk.Entry(root)
    server_ip_entry.pack(pady=5)

    send_button = tk.Button(root, text="Send File", command=send_file)
    send_button.pack(pady=5)

    start_server_button = tk.Button(root, text="Start Server", command=start_server)
    start_server_button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
