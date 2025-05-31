import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Parámetros
r = 5  # radio del círculo
theta_inicio = 90  # ángulo inicial en grados
n_pasos = 360  # número de pasos para completar el ciclo

# Convertir ángulo inicial a radianes
theta_inicio_rad = np.deg2rad(theta_inicio)

# Crear figura y axis
fig, ax = plt.subplots()

# Dibujar círculo
circle = plt.Circle((0, 0), r, fill=False)
ax.add_artist(circle)

# Configurar axis
ax.set_xlim(-r-1, r+1)
ax.set_ylim(-r-1, r+1)
ax.set_aspect('equal')

# Inicializar líneas
line_blue, = ax.plot([], [], 'b-')
line_red, = ax.plot([], [], 'r-')

# Función de inicialización para la animación
def init():
    line_blue.set_data([], [])
    line_red.set_data([], [])
    return line_blue, line_red

# Función de actualización para la animación
def update(i):
    theta_blue = theta_inicio_rad + i * 2 * np.pi / n_pasos
    theta_red = theta_inicio_rad - i * 2 * np.pi / n_pasos
    
    x_blue = r * np.cos(theta_blue)
    y_blue = r * np.sin(theta_blue)
    x_red = r * np.cos(theta_red)
    y_red = r * np.sin(theta_red)
    
    line_blue.set_data([0, x_blue], [0, y_blue])
    line_red.set_data([0, x_red], [0, y_red])
    
    return line_blue, line_red

# Crear animación
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, n_pasos), init_func=init, blit=True, interval=20, repeat=True)

# Mostrar gráfica
plt.show()
