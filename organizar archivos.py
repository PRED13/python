# organizador.py
import os
import shutil

def organizar_por_extension(ruta):
    for archivo in os.listdir(ruta):
        full_path = os.path.join(ruta, archivo)
        if os.path.isfile(full_path):
            extension = archivo.split('.')[-1]
            carpeta_destino = os.path.join(ruta, extension.upper())
            os.makedirs(carpeta_destino, exist_ok=True)
            shutil.move(full_path, os.path.join(carpeta_destino, archivo))

ruta = input("Ingresa la ruta a organizar: ")
organizar_por_extension(ruta)
print("Organización completa.")
