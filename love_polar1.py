import numpy as np
import matplotlib.pyplot as plt


def love():
    theta = np.linspace(0, 2 * np.pi, 1000)

    plt.subplot(111, polar=True)
    a = 4
    r = a * (1 - np.sin(theta))
    plt.plot(theta, r, '--', lw=2)
    plt.grid(True)

    plt.show()


if __name__ == '__main__':
    love()

