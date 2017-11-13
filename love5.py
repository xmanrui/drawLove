import matplotlib.pyplot as plt
import numpy as np


def love5():

    x = np.linspace(0, 2, 1000)
    g = -1 * np.sqrt(1 - 1.65 * np.arctan(x) * np.arctan(x))
    f = np.sqrt(1 - np.power(np.power(np.abs(x), np.abs(x)), 2))

    plt.plot(x, g, color='red', linewidth=2)
    plt.plot(-x, g, color='red', linewidth=2)
    plt.plot(x, f, color='red', linewidth=2)
    plt.plot(-x, f, color='red', linewidth=2)

    plt.ylim(-2, 2)
    plt.xlim(-2, 2)
    plt.title('LOVE')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    love5()
