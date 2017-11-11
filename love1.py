import matplotlib.pyplot as plt
import numpy as np
import math


def draw_love():
    t = np.linspace(0, math.pi, 1000)
    a = 2
    x = a * (2 * np.cos(t) - np.cos(2 * t))
    y = a * (2 * np.sin(t) - np.sin(2 * t))

    plt.plot(x, y, color='red', linewidth=2)
    plt.plot(x, -y, color='red', linewidth=2)

    plt.ylim(-6, 6)
    plt.xlim(-8, 4)
    plt.title('LOVE')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    draw_love()
