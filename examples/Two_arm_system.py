import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

x0 = 0
y0 = 0
l1 = 1


def endpoint_x(q1):
    x1 = x0 + l1 * np.cos(q1)
    return x1


def endpoint_y(q1):
    y1 = y0 + l1 * np.sin(q1)
    return y1


fig, ax = plt.subplots()

line, = ax.plot([x0, endpoint_x(0)], [y0, endpoint_y(0)])
ax.set_xlim(-1,1)
ax.set_ylim(-1,1)
fig.subplots_adjust(bottom=0.25)

q_value = fig.add_axes([0.25, 0.1, 0.65, 0.03])
q_slider = Slider(
    ax=q_value,
    label='angle',
    valmin=0,
    valmax=360,
    valinit=0,
)


def update(val):
    line.set_xdata([x0, endpoint_x(np.deg2rad(q_slider.val))])
    line.set_ydata([y0, endpoint_y(np.deg2rad(q_slider.val))])
    fig.canvas.draw_idle()


q_slider.on_changed(update)
plt.show()
