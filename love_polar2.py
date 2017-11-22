import numpy as np
import matplotlib.pyplot as plt


def love():
    t1 = np.linspace(np.pi/2, np.pi, 100)
    t2 = np.linspace(np.pi/2, 0, 100)  # -t1 + np.pi
    r = 5 * np.power(np.sin(t1), 7) * np.power(np.e, np.abs(2*t1))

    plt.subplot(111, polar=True)

    plt.plot(t1, r, '--', lw=2)
    plt.plot(t2, r, '--', lw=2)

    plt.grid(True)

    plt.show()


if __name__ == '__main__':
    love()

