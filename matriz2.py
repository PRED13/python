import numpy as np
from itertools import permutations

def tsp_dynamic_programming(distancia_matriz):
    n = len(distancia_matriz)
    
    # Lista para almacenar los mínimos costos de las rutas
    # dp[mascara][i] significa el costo mínimo para visitar todos los nodos en "máscara" y terminar en el nodo i
    dp = [[float('inf')] * n for _ in range(1 << n)]
    dp[1][0] = 0  # Empieza en el nodo 0 con costo 0

    # Iteramos sobre todas las combinaciones de nodos visitados
    for mask in range(1 << n):
        for u in range(n):
            if mask & (1 << u):  # Si el nodo u está en la combinación actual
                for v in range(n):
                    if mask & (1 << v) == 0:  # Si el nodo v no está en la combinación actual
                        next_mask = mask | (1 << v)
                        dp[next_mask][v] = min(dp[next_mask][v], dp[mask][u] + distancia_matriz[u][v])

    # Recuperamos la ruta óptima
    min_cost = float('inf')
    last_node = -1
    for i in range(1, n):
        cost = dp[(1 << n) - 1][i] + distancia_matriz[i][0]
        if cost < min_cost:
            min_cost = cost
            last_node = i

    # Reconstrucción de la ruta
    ruta = [0]  # Empezamos en el nodo 0
    mask = (1 << n) - 1
    while last_node != 0:
        ruta.append(last_node)
        new_mask = mask & ~(1 << last_node)
        for i in range(n):
            if dp[mask][last_node] == dp[new_mask][i] + distancia_matriz[i][last_node]:
                last_node = i
                break
        mask = new_mask

    ruta.append(0)  # Volvemos al nodo de inicio
    ruta.reverse()

    return ruta, min_cost

# Matriz de distancias de ejemplo
distancia_matriz = [
    [0, 13, 23, 46, 17, 14, 19],
    [16, 0, 29, 34, 38, 40, 43],
    [25, 34, 0, 18, 25, 27, 41],
    [31, 30, 35, 0, 36, 37, 38],
    [23, 21, 23, 23, 0, 22, 27],
    [31, 33, 34, 33, 37, 0, 39],
    [30, 34, 37, 24, 40, 50, 0]
]

# Llamamos a la función y mostramos los resultados
ruta, distancia = tsp_dynamic_programming(distancia_matriz)
ruta = np.array(ruta)  # Convertimos la ruta en un array de NumPy
print("La ruta más corta es:", ruta, "La distancia es:", distancia)
