from FormattingFuncs import mathformat


class Poly:
	"""
	Polynomial(*coeffs) -> Polynomial

	Supports:
	- Computing real-valued polynomials for any given float/int
	- Field operations: can add, subtract, & scalar multiply polynomials
	- Calculus opeartions: can differentatiate & integrate polynomials
	"""

	def __init__(self, *coeffs):
		"""
		Creates a new Polynomial object by passing in floats/ints
		Passed in args correspond to coefficients in decreasing degree order
		"""
		try:
			if coeffs[0] == 0 and len(coeffs) > 1:
				raise ValueError('First argument of non-constant Polynomial must be non-zero')

			self.coeffs = coeffs
			# self.coeffs = {degree: coeff for degree, coeff in enumerate(reversed(coeffs))}
			self.degree = len(coeffs) - 1
			self.isConst = (len(coeffs) == 1)  # P(x) = c
			self.isLinear = (len(coeffs) == 2)  # P(x) = ax + b

		except IndexError:
			raise IndexError(f'Oops! {type(self).__name__} requires atleast 1 float/int arg')

	def value(self, x):
		"""Computes P(x=float/int)"""
		# Makes finding y-intercept a constant time process, since y-int := P(0) = const term
		if x == 0:
			val = self.coeffs[-1]
		else:
			val = sum(self.coeffs[i] * (x ** (self.degree - i)) for i in range(self.degree + 1))

		return val

	def differentiate(self):
		"""Computes differentiated Polynomial object: dP/dx"""
		if self.isConst:
			coeffs = (0,)
		else:
			coeffs = (self.coeffs[i] * (self.degree - i) for i in range(self.degree))

		return Poly(*coeffs)

	def integrate(self, const=0):
		"""Computes integrated Polynomial object given some integrating constant: ∫P(x)dx + c"""
		coeffs = [self.coeffs[i] / (self.degree + 1 - i) for i in range(self.degree + 1)]
		coeffs.append(const)

		return Poly(*coeffs)

	def __add__(self, other):
		"""
		Polynomial(*coeffs1) + Polynomial(*coeffs2) -> Polynomial(*coeffs3)
		Polynomial(*coeffs4) + float/int -> Polynomial(*coeffs5)
		"""
		try:
			# Prepends smaller degree polynomial with leading 0's
			diff = self.degree - other.degree
			leadingZeros = tuple(0 for _ in range(abs(diff)))

			if diff > 0:
				p1coeffs = self.coeffs
				p2coeffs = leadingZeros + other.coeffs
			else:
				p1coeffs = leadingZeros + self.coeffs
				p2coeffs = other.coeffs

			sumcoeffs = [sum(c) for c in zip(p1coeffs, p2coeffs)]

			# Finds index of first non-zero term
			leadingindex = -1
			for c in sumcoeffs:
				leadingindex += 1
				if c is not 0: break

			sumcoeffs = sumcoeffs[leadingindex:]

			return Poly(*sumcoeffs)

		# Handles case when adding a scalar -> shifts polynomial vertically
		except AttributeError:
			coeffs = list(self.coeffs)
			coeffs[-1] += other

			return Poly(*coeffs)

	def __radd__(self, other):
		"""
		Polynomial(*coeffs1) + Polynomial(*coeffs2) -> Polynomial(*coeffs3)
		float/int + Polynomial(*coeffs4) -> Polynomial(*coeffs5)
		"""
		return self + other

	def __mul__(self, scalar):
		"""Polynomial(coeffs=tuple) * float/int -> Polynomial(coeffs=tuple2)"""
		if not isinstance(scalar, (float, int)):
			raise TypeError(f"'{type(scalar).__name__}' object cannot be multiplied"
			                f" - only supports scalar (float/int) multiplication")
		elif scalar == 0:
			coeffs = (0,)
		else:
			coeffs = (coeff * scalar for coeff in self.coeffs)

		return Poly(*coeffs)

	def __rmul__(self, other):
		"""float/int * Polynomial(coeffs=tuple) -> Polynomial(coeffs=tuple2)"""
		return self * other

	def __sub__(self, other):
		"""
		Polynomial(*coeffs1) - Polynomial(*coeffs2) -> Polynomial(*coeffs3)
		Polynomial(*coeffs4) - float/int -> Polynomial(*coeffs5)
		"""
		return self + (-1 * other)

	def __rsub__(self, other):
		"""
		Polynomial(*coeffs1) - Polynomial(*coeffs2) -> Polynomial(*coeffs3)
		float/int - Polynomial(*coeffs4) -> Polynomial(*coeffs5)
		"""
		return other + (-1 * self)

	def __repr__(self):
		return f'{type(self).__name__}{self.coeffs}'

	def __str__(self):
		"""
		Displays 'mathematical' representation of polynomial:
		i.e. Polynomial(-1, 0, 0, 0, -2, 0, 1) ->  -x⁶ - 2x² + 1
		"""
		poly = ''.join(mathformat(k, self.coeffs) for k in range(self.degree + 1))

		return poly
