import matplotlib.pyplot as plt
import numpy as np


def draw_love():
    x = np.linspace(-2, 2, 1000)
    f = (np.power(x, 2/3) + np.sqrt(np.power(x, 4/3)
        - 4 * np.power(x, 2) + 4)) / 2
    g = (np.power(x, 2/3) - np.sqrt(np.power(x, 4/3)
        - 4 * np.power(x, 2) + 4)) / 2

    plt.plot(x, f, color='red', linewidth=2)
    plt.plot(-x, f, color='red', linewidth=2)
    plt.plot(x, g, color='red', linewidth=2)
    plt.plot(-x, g, color='red', linewidth=2)

    plt.ylim(-2, 2)
    plt.xlim(-2, 2)
    plt.title('LOVE')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    draw_love()
