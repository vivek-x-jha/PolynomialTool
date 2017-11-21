from Polynomial import Poly
from Plotting import polyplot


def Poly_test():
    p1 = Poly(-1, 0, 0, 3, 4, -1, 0, 1)
    p2 = Poly(-1)
    p3 = p1 + p2
    p4 = 3 * p1
    dp = p1.differentiate()
    int_p = p1.integrate(1)
    polynomials = [p1, dp]

    for poly in polynomials:
        print(f'{"~" * 50}')
        print(f'P(x) = {poly}')
        print(f'\n{repr(poly)}')
        print(f'deg(P) = {poly.degree}')
        print(f'P(0) = {poly.value(1)}')


def graph_test():
    p = Poly(1, -1.5, -5, 5.5)
    q = p - 3

    polyplot(p, q)


Poly_test()
graph_test()

