from Polynomial import Poly


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


def main():
    Poly_test()


if __name__ == '__main__':
    main()
