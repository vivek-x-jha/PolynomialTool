from unittest import TestCase
from Polynomial import Poly
import numpy as np


class PolyTest(TestCase):
    def test_value(self):
        degree = 15
        precision = 3
        randHigh = np.random.randint(degree)
        randLow = -1 * randHigh
        randSize = np.random.randint(1, degree)
        coeffs = np.random.uniform(low=randLow, high=randHigh, size=randSize)
        randPositiveValue = round(degree * (1 - np.random.random()), precision)
        randNegativeValue = round(degree * (1 - np.random.random()), precision)

        try:
            p = Poly(*coeffs)

        except ValueError:
            # ensures first coefficient is non-zero for non-constant Polynomial (but honestly the probability of an Exception is soooo small)
            coeffs[0] = degree * (1 - np.random.random())
            p = Poly(*coeffs)

        polyValue = lambda x: round(p.value(x), precision)
        testValue = lambda x: round(sum(coeffs[i] * (x ** (p.degree - i)) for i in range(p.degree + 1)), precision)

        self.assertEqual(polyValue(0), round(coeffs[-1], precision))
        self.assertEqual(polyValue(1), round(sum(coeffs), precision))
        self.assertEqual(polyValue(randPositiveValue), testValue(randPositiveValue))
        self.assertEqual(polyValue(randNegativeValue), testValue(randNegativeValue))

    # def test_differentiate(self):
    # 	pass
    #
    # def test_integrate(self):
    # 	pass
    #
    # pass
    # def test_tangent(self):
    # 	pass
    #
    # def test_integrate(self):
    # 	pass
    #
    # def __add__(self, other):
    # 	pass
    #
    # def __radd__(self, other):
    # 	pass
    #
    # def __mul__(self, scalar):
    # 	pass
    #
    # def __rmul__(self, other):
    # 	pass
    #
    # def __sub__(self, other):
    # 	pass
    #
    # def __rsub__(self, other):
    # 	pass
    #
    # def __repr__(self):
    # 	pass
    #
    # def __str__(self):
    # 	pass
