def contar_palabras(texto):
    palabras = texto.split()
    conteo = {}
    for palabra in palabras:
        palabra = palabra.lower().strip(",.;:")
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo

# Ejemplo de uso
texto = "Hola mundo. Hola a todos en el mundo."
print(contar_palabras(texto))
