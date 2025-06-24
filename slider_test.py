import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('TkAgg')
from matplotlib.widgets import Slider

# Datos iniciales
x = np.linspace(0, 10, 1000)
a0 = 1
y = a0 * np.sin(x)

# Crear figura y eje
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)  # Espacio para el slider
l, = plt.plot(x, y)

# Posición y características del slider
ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03])
slider = Slider(ax_slider, 'Amplitud', 0.1, 10.0, valinit=a0)

# Función que actualiza la gráfica
def update(val):
    amp = slider.val
    l.set_ydata(amp * np.sin(x))
    fig.canvas.draw_idle()

slider.on_changed(update)

plt.show()
