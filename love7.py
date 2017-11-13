import matplotlib.pyplot as plt
import numpy as np
import math


def love7():
    x = np.linspace(-2, 2, 1000)
    f = np.sqrt(2 * np.sqrt(x * x) - x * x)
    g = -1 * 2.14 * np.sqrt(math.sqrt(2) - np.sqrt(np.abs(x)))
    plt.plot(x, f, color='red', linewidth=2)
    plt.plot(x, g, color='red', linewidth=2)

    plt.title('LOVE')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    love7()

