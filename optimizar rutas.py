def ruta_minima(matriz):
    from functools import lru_cache
    filas, columnas = len(matriz), len(matriz[0])

    @lru_cache(maxsize=None)
    def dfs(i, j, ult_direccion):
        if i == filas - 1 and j == columnas - 1:
            return matriz[i][j]

        costo_actual = matriz[i][j]
        min_costo = float('inf')

        # Moverse a la derecha
        if j + 1 < columnas and ult_direccion != 'H':
            min_costo = min(min_costo, dfs(i, j + 1, 'H'))

        # Moverse hacia abajo
        if i + 1 < filas and ult_direccion != 'V':
            min_costo = min(min_costo, dfs(i + 1, j, 'V'))

        return costo_actual + min_costo

    return dfs(0, 0, None)

# Prueba
matriz = [
    [1, 3, 1],
    [6, 5, 2],
    [4, 2, 1]
]
print("Costo mínimo:", ruta_minima(matriz))
