import matplotlib.pyplot as plt
import numpy as np
import math


def love9():
    x = np.linspace(-2, 2, 1000)
    f = np.sqrt(2 * np.sqrt(np.power(x, 2)) - np.power(x, 2))
    g = np.arcsin(np.abs(x) - 1) - math.pi/2
    plt.plot(x, f, color='red', linewidth=2)
    plt.plot(x, g, color='red', linewidth=2)

    plt.title('LOVE')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    love9()

