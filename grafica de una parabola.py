import matplotlib.pyplot as plt
import numpy as np



# Parámetros del movimiento parabólico
v0 = 10  # Velocidad inicial (m/s)
theta = 45  # Ángulo de lanzamiento (grados)
g = 9.81  # Aceleración debido a la gravedad (m/s²)

# Convertir el ángulo a radianes
theta_rad = np.radians(theta)

# Calcular las componentes de la velocidad inicial
vx = v0 * np.cos(theta_rad)
vy = v0 * np.sin(theta_rad)

# Tiempo de vuelo
t_flight = 2 * vy / g

# Crear el rango de tiempo para graficar
t = np.linspace(0, t_flight, 100)

# Ecuaciones del movimiento parabólico
x = vx * t
y = vy * t - 0.5 * g * t**2

# Graficar el movimiento parabólico
plt.plot(x, y)
plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plt.title('Tiro Parabólico')
plt.grid(True)
plt.show()
