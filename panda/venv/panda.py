from __future__ import print_function

from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

import matplotlib.pyplot as plt
import numpy as np


@interact(lg_z=(-0.5, 4.0, 0.1))
def f(lg_z=1.0):
    z = 10 ** lg_z
    x_min = 1.5 - 6 / z
    x_max = 1.5 + 6 / z
    l_min = 1.5 - 4 / z
    l_max = 1.5 + 4 / z
    xstep = (x_max - x_min) / 100
    lstep = (l_max - l_min) / 100

    x = np.arange(x_min, x_max, xstep)

    plt.plot(x, np.sin(x), '-b')

    plt.plot((l_min, l_max), (np.sin(l_min), np.sin(l_max)), '-r')
    plt.plot((l_min, l_max), (np.sin(l_min), np.sin(l_min)), '-r')
    plt.plot((l_max, l_max), (np.sin(l_min), np.sin(l_max)), '-r')

    yax = plt.ylim()

    plt.text(l_max + 0.1 / z, (np.sin(l_min) + np.sin(l_max)) / 2, "$\Delta y$")
    plt.text((l_min + l_max) / 2, np.sin(l_min) - (yax[1] - yax[0]) / 20, "$\Delta x$")

    plt.show()

    print('slope =', (np.sin(l_max) - np.sin(l_min)) / (l_max - l_min))