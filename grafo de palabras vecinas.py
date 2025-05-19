from collections import deque, defaultdict

def palabras_vecinas(palabra, diccionario):
    vecinos = []
    for w in diccionario:
        if sum(a != b for a, b in zip(palabra, w)) == 1:
            vecinos.append(w)
    return vecinos

def camino_mas_corto(inicio, fin, diccionario):
    if fin not in diccionario:
        return "No hay conexión"

    grafo = defaultdict(list)
    for palabra in diccionario:
        grafo[palabra] = palabras_vecinas(palabra, diccionario)

    visitado = set()
    cola = deque([[inicio]])

    while cola:
        camino = cola.popleft()
        actual = camino[-1]

        if actual == fin:
            return camino

        if actual not in visitado:
            visitado.add(actual)
            for vecino in grafo[actual]:
                cola.append(camino + [vecino])

    return "No hay conexión"

# Prueba
diccionario = ["cold", "cord", "card", "ward", "warm"]
print(camino_mas_corto("cold", "warm", diccionario))
