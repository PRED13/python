import numpy as np
# Función para crear la tabla de costos
def crear_tabla():
    # Pedir número de orígenes y destinos
    num_origenes = int(input("Ingrese el número de orígenes: "))
    num_destinos = int(input("Ingrese el número de destinos: "))
    
    # Inicializar matrices de oferta, demanda y costos
    oferta = []
    demanda = []
    print("\n--- Ingrese la oferta de cada origen ---")
    for i in range(num_origenes):
        oferta.append(int(input(f"Oferta del origen {i+1}: ")))
    
    print("\n--- Ingrese la demanda de cada destino ---")
    for j in range(num_destinos):
        demanda.append(int(input(f"Demanda del destino {j+1}: ")))
    
    costos = np.zeros((num_origenes, num_destinos), dtype=int)
    print("\n--- Ingrese la matriz de costos ---")
    for i in range(num_origenes):
        for j in range(num_destinos):
            costos[i, j] = int(input(f"Costo de enviar desde el origen {i+1} al destino {j+1}: "))
    
    return oferta, demanda, costos

# Función para aplicar el método de la esquina noroeste y encontrar la solución inicial
def metodo_esquina_noroeste(oferta, demanda, costos):
    num_origenes = len(oferta)
    num_destinos = len(demanda)
    
    # Crear tabla de solución inicial
    solucion = np.zeros((num_origenes, num_destinos), dtype=int)
    
    i, j = 0, 0
    while i < num_origenes and j < num_destinos:
        cantidad = min(oferta[i], demanda[j])
        solucion[i, j] = cantidad
        oferta[i] -= cantidad
        demanda[j] -= cantidad
        
        if oferta[i] == 0:
            i += 1
        elif demanda[j] == 0:
            j += 1
    
    return solucion

# Función para calcular el costo total dado una solución
def calcular_costo_total(solucion, costos):
    return np.sum(solucion * costos)

# Implementación del método MODI
def metodo_modi(solucion, costos):
    num_origenes, num_destinos = solucion.shape
    u = [None] * num_origenes
    v = [None] * num_destinos
    
    u[0] = 0  # Inicializamos U1 como 0 para empezar
    
    # Calcular las Ui y Vj
    while None in u or None in v:
        for i in range(num_origenes):
            for j in range(num_destinos):
                if solucion[i, j] > 0:  # Solo para las celdas no vacías
                    if u[i] is not None and v[j] is None:
                        v[j] = costos[i, j] - u[i]
                    elif u[i] is None and v[j] is not None:
                        u[i] = costos[i, j] - v[j]
    
    # Calcular costos reducidos
    costos_reducidos = np.zeros((num_origenes, num_destinos), dtype=int)
    for i in range(num_origenes):
        for j in range(num_destinos):
            if solucion[i, j] == 0:
                costos_reducidos[i, j] = costos[i, j] - (u[i] + v[j])
    
    return costos_reducidos

# Función principal para resolver el problema
def resolver_problema():
    oferta, demanda, costos = crear_tabla()
    solucion_inicial = metodo_esquina_noroeste(oferta, demanda, costos)
    print("\n--- Solución inicial (Esquina Noroeste) ---")
    print(solucion_inicial)
    
    costo_inicial = calcular_costo_total(solucion_inicial, costos)
    print(f"\nCosto inicial: {costo_inicial}")
    
    # Aplicamos el método MODI para optimizar
    costos_reducidos = metodo_modi(solucion_inicial, costos)
    print("\n--- Costos reducidos ---")
    print(costos_reducidos)
    
    # Evaluamos si es óptima la solución o si requiere ajustes (costos reducidos negativos)
    if np.all(costos_reducidos >= 0):
        print("\nLa solución es óptima.")
    else:
        print("\nLa solución no es óptima, se requieren ajustes.")

# Ejecutar el programa
resolver_problema()
