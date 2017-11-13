import matplotlib.pyplot as plt
import numpy as np
import math


def love6():
    t = np.linspace(0, math.pi * 2, 1000)
    x = 16 * np.power(np.sin(t), 3)
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    plt.plot(x, y, color='red', linewidth=2)
    plt.title('LOVE')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    love6()

