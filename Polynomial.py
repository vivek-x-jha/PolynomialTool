import argparse
from typing import Tuple, cast

from HelperFuncs import horner, mathformat

Number = float | int


class Poly:
    """
    Blueprint for creating a Polynomial object

    Var-positional parameter: *coeffs

    Supports:
    - Computing real-valued polynomials for any given float/int
    - Field operations: can add, subtract, & scalar multiply polynomials
    - Calculus opeartions: can differentatiate, create tangent line, & integrate polynomials
    """

    def __init__(self, *coeffs: Number) -> None:
        """
        Initializes a new Polynomial object by passing in numerial values
        Passed in args represent coefficients in decreasing degree order
        """

        try:
            if coeffs[0] == 0 and len(coeffs) > 1:
                raise ValueError('First argument of non-constant Polynomial must be non-zero')

            self.coeffs: Tuple[Number, ...] = coeffs
            self.degree: int = len(coeffs) - 1

        except IndexError:
            raise IndexError(f'Oops! {type(self).__name__} requires atleast 1 float/int arg')

    def value(self, x: Number) -> float:
        """Computes P(x=float/int) by implementing horner's method"""

        try:
            return horner(self.degree - 1, self.coeffs, x)

        except RecursionError:
            # Handles case where Polynomial is constan
            return self.coeffs[0]

    def differentiate(self) -> 'Poly':
        """Computes differentiated Polynomial object: dP/dx"""
        if self.degree == 1:
            coeffs = (0,)
        else:
            coeffs = (self.coeffs[i] * (self.degree - i) for i in range(self.degree))

        return Poly(*coeffs)

    def integrate(self, const: Number = 0) -> 'Poly':
        """Computes integrated Polynomial object given some integrating constant: ∫P(x)dx + c"""

        coeffs = [self.coeffs[i] / (self.degree + 1 - i) for i in range(self.degree + 1)]
        coeffs.append(const)

        return Poly(*coeffs)

    def tangent(self, x: Number) -> 'Poly':
        """Computes tangent line of a Polynomial at a given point x"""

        try:
            dp = self.differentiate()
            slope = dp.value(x)
            intercept = self.value(x) - slope * x
            tline = Poly(slope, intercept)

            return tline

        except ValueError:
            # Handles case where Polynomial is constant
            return self

    def __add__(self, other: 'Poly' | Number) -> 'Poly':
        """
        Polynomial(*coeffs1) + Polynomial(*coeffs2) -> Polynomial(*coeffs3)
        Polynomial(*coeffs4) + float/int -> Polynomial(*coeffs5)
        """

        try:
            # Prepends smaller degree polynomial with leading 0's
            other_poly = cast('Poly', other)
            diff = self.degree - other_poly.degree
            leadingZeros = tuple(0 for _ in range(abs(diff)))

            if diff > 0:
                p1coeffs: Tuple[Number, ...] = self.coeffs
                p2coeffs: Tuple[Number, ...] = leadingZeros + other_poly.coeffs
            else:
                p1coeffs = leadingZeros + self.coeffs
                p2coeffs = other_poly.coeffs

            sumcoeffs = [sum(c) for c in zip(p1coeffs, p2coeffs)]

            # Finds index of first non-zero term
            leadingindex = -1
            for c in sumcoeffs:
                leadingindex += 1
                if c != 0:
                    break

            sumcoeffs = sumcoeffs[leadingindex:]

            return Poly(*sumcoeffs)

        except AttributeError:
            try:
                # Handles case when adding a scalar -> shifts polynomial vertically
                coeffs = list(self.coeffs)
                coeffs[-1] += other

                return Poly(*coeffs)

            except TypeError:
                raise TypeError(
                    f"Cannot perform field operation using '{type(other).__name__}' - please use another Poly object or scalar (float/int)"
                )

    def __radd__(self, other: Number | 'Poly') -> 'Poly':
        """
        Polynomial(*coeffs1) + Polynomial(*coeffs2) -> Polynomial(*coeffs3)
        float/int + Polynomial(*coeffs4) -> Polynomial(*coeffs5)
        """

        return self + other

    def __mul__(self, scalar: Number) -> 'Poly':
        """Polynomial(coeffs=tuple) * float/int -> Polynomial(coeffs=tuple2)"""

        if not isinstance(scalar, (float, int)):
            raise TypeError(f"'{type(scalar).__name__}' object cannot be multiplied - only supports scalar (float/int) multiplication")
        elif scalar == 0:
            coeffs = (0,)
        else:
            coeffs = (coeff * scalar for coeff in self.coeffs)

        return Poly(*coeffs)

    def __rmul__(self, other: Number | 'Poly') -> 'Poly':
        """float/int * Polynomial(coeffs=tuple) -> Polynomial(coeffs=tuple2)"""

        return self * other

    def __sub__(self, other: 'Poly' | Number) -> 'Poly':
        """
        Polynomial(*coeffs1) - Polynomial(*coeffs2) -> Polynomial(*coeffs3)
        Polynomial(*coeffs4) - float/int -> Polynomial(*coeffs5)
        """

        return self + (-1 * other)

    def __rsub__(self, other: Number | 'Poly') -> 'Poly':
        """
        Polynomial(*coeffs1) - Polynomial(*coeffs2) -> Polynomial(*coeffs3)
        float/int - Polynomial(*coeffs4) -> Polynomial(*coeffs5)
        """

        return other + (-1 * self)

    def __repr__(self) -> str:
        return f'{type(self).__name__}{self.coeffs}'

    def __str__(self) -> str:
        """
        Displays 'mathematical' representation of polynomial:
        i.e. Polynomial(-1, 0, 0, 0, -2, 0, 1) ->  -x⁶ - 2x² + 1
        """

        poly = ''.join(mathformat(k, self.coeffs) for k in range(self.degree + 1))
        return poly


def main() -> None:
    desc = 'Prints string formatted Polynomial instance using variable-length coeffs'

    parser = argparse.ArgumentParser(description=desc)
    parser_config = {
        'type': float,
        'nargs': '+',
        'metavar': '',
        'help': 'Numerical coefficients in descending order',
    }
    parser.add_argument('-c', '--coeffs', **parser_configs)
    args = parser.parse_args()

    p = Poly(*args.coeffs)

    formattedPolynomial = f'P(x) = {p}'
    print(formattedPolynomial)


if __name__ == '__main__':
    main()
