import matplotlib.pyplot as plt
import numpy as np


def love8():
    t = np.linspace(-1, 1, 1000)
    x = np.sin(t) * np.cos(t) * np.log(np.abs(t))
    y = np.sqrt(np.abs(t)) * np.cos(t)
    plt.plot(x, y, color='red', linewidth=2)

    plt.title('LOVE')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    love8()

