# grafica_csv.py
import csv
import matplotlib.pyplot as plt

nombres = []
valores = []

with open('datos.csv', newline='') as archivo:
    lector = csv.reader(archivo)
    next(lector)  # saltar encabezado
    for fila in lector:
        nombres.append(fila[0])
        valores.append(float(fila[1]))

plt.bar(nombres, valores, color='skyblue')
plt.title('Valores desde archivo CSV')
plt.xlabel('Categorías')
plt.ylabel('Valores')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
