import matplotlib.pyplot as plt
import numpy as np
import math


def draw_love():
    x = np.linspace(0, math.pi/3, 1000)
    f = -1 * np.tan(np.sqrt(1 - np.power(np.abs(x), 3/2))) + math.pi/2
    g = np.sqrt(1/4 - np.power(x - 1/2, 2)) + math.pi/2

    plt.plot(x, f, color='red', linewidth=2)
    plt.plot(-x, f, color='red', linewidth=2)
    plt.plot(x, g, color='red', linewidth=2)
    plt.plot(-x, g, color='red', linewidth=2)

    plt.ylim(-1, 3)
    plt.xlim(-2, 2)
    plt.title('LOVE')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    draw_love()
