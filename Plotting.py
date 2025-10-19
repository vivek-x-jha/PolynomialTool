from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np
import matplotlib.pyplot as plt
from HelperFuncs import superscript

if TYPE_CHECKING:
    from Polynomial import Poly


def polyplot(*polys: 'Poly', xaxis_range: float = 3, yaxis_range: float = 10, titleString: str = '') -> None:
    """
    Plots single graph of any number of polynomials using matplotlib.pyplot
    Change axes_range keyword args accordingly
    Can pass in custom title
    """
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, facecolor='grey')

    # Creates title above graph
    if titleString != '':
        ttl = plt.gca().title
        ttl.set_position([0.5, 1.05])
        plt.title(titleString)

    # spine placement data centered
    ax.spines['left'].set_position(('data', 0.0))
    ax.spines['bottom'].set_position(('data', 0.0))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # Helper funcs to uniformly space axis tick markers
    uniform_xinterval = lambda num=50: np.linspace(-1 * xaxis_range, xaxis_range, num)
    uniform_yinterval = lambda num=50: np.linspace(-1 * yaxis_range, yaxis_range, num)

    # Sets axes tick markers accordingly and hides marker value at origin
    ax.set_xticks([x for x in uniform_xinterval(7) if x != 0])
    ax.set_yticks([y for y in uniform_yinterval(6) if y != 0])
    ax.set_ylim([-1 * (yaxis_range + 1), yaxis_range + 1])
    plt.grid(True, linestyle='dotted')

    lineColors = ['cyan', 'yellow', 'blue', 'red', 'magenta', 'green', 'white', 'black']

    # Creates graph of all passed in polynomial objects
    for i, poly in enumerate(polys):
        domain = uniform_xinterval(10**4)
        f = np.vectorize(poly.value)
        codomain = f(domain)

        try:
            plt.plot(domain, codomain, label=f'P{superscript(i + 1, reverse=True)}(x) = {poly}', color=lineColors[i])
        except IndexError:
            plt.plot(domain, codomain, label=f'P{superscript(i + 1, reverse=True)}(x) = {poly}')

    plt.legend(loc='lower right')
    plt.show()
