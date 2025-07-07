from collections import deque

class Grafo:
    def __init__(self, grafo):
        self.grafo = grafo
        self.N = len(grafo)
        self.padre = [-1] * self.N

    def bfs(self, s, t):
        visitado = [False] * self.N
        cola = deque([s])
        visitado[s] = True

        while cola:
            u = cola.popleft()
            for v, capacidad in enumerate(self.grafo[u]):
                if not visitado[v] and capacidad > 0:
                    cola.append(v)
                    visitado[v] = True
                    self.padre[v] = u
        return visitado[t]

    def ford_fulkerson(self, origen, destino):
        flujo_maximo = 0

        while self.bfs(origen, destino):
            camino_flujo = float('inf')
            v = destino
            while v != origen:
                u = self.padre[v]
                camino_flujo = min(camino_flujo, self.grafo[u][v])
                v = self.padre[v]

            # Actualizar capacidades residuales
            v = destino
            while v != origen:
                u = self.padre[v]
                self.grafo[u][v] -= camino_flujo
                self.grafo[v][u] += camino_flujo
                v = self.padre[v]

            flujo_maximo += camino_flujo

        return flujo_maximo

# Grafo: nodos 0 (1), 1 (2), 2 (3), 3 (4)
grafo = [
    [0, 10, 5, 0],   # nodo 1
    [0, 0, 15, 10],  # nodo 2
    [0, 0, 0, 10],   # nodo 3
    [0, 0, 0, 0]     # nodo 4
]

g = Grafo(grafo)
flujo_max = g.ford_fulkerson(0, 3)
print("El flujo máximo desde el nodo 1 al nodo 4 es:", flujo_max)
