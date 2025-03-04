import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parámetros de la esfera
R = 5  # Radio de la esfera

# Crear la figura y el objeto 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Crear la rejilla en coordenadas esféricas
phi = np.linspace(0, np.pi, 100)
theta = np.linspace(0, 2 * np.pi, 100)
Phi, Theta = np.meshgrid(phi, theta)

# Convertir a coordenadas cartesianas
X = R * np.sin(Phi) * np.cos(Theta)
Y = R * np.sin(Phi) * np.sin(Theta)
Z = R * np.cos(Phi)

# Graficar la superficie de la esfera
ax.plot_surface(X, Y, Z, color='b', alpha=0.5)

# Configurar los límites y etiquetas
ax.set_xlim([-R, R])
ax.set_ylim([-R, R])
ax.set_zlim([-R, R])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('Región de Integración: Esfera de Radio R')

plt.show()
