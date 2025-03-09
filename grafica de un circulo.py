import numpy as np
import matplotlib.pyplot as plt

# Parámetros del círculo
centro_x, centro_y = 1, 0  # Centro en (1, 0)
radio = 1  # Radio del círculo

# Generar los puntos del círculo
theta = np.linspace(0, 2 * np.pi, 100)  # Ángulo en radianes
x = centro_x + radio * np.cos(theta)  # Coordenada x
y = centro_y + radio * np.sin(theta)  # Coordenada y

# Graficar el círculo
plt.figure(figsize=(6,6))
plt.plot(x, y, label=r'$(x-1)^2 + y^2 = 1$', color='blue')
plt.scatter(centro_x, centro_y, color='red', label='Centro (1, 0)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfica de $(x-1)^2 + y^2 = 1$')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.axis('equal')  # Escala igual en ambos ejes
plt.show()
