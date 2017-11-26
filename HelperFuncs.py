def horner(term, coeffs, value):
	"""Blueprint for calculating value of a Polynomial recursively"""
	# speeds up calculation by reducing the number of multiplication calls to the degree of the polynomial
	if term == 0:
		init_val = coeffs[0] * value + coeffs[1]
		return init_val
	else:
		next_val = horner(term - 1, coeffs, value) * value + coeffs[term + 1]
		return next_val


# Support functions for Poly.__str__ method

def mathformat(term, coeffs):
	"""Returns formatted term of Polynomial according to coefficient's parity and input"""
	# Booleans used for control flow to exhaust all cases
	isLeadingTerm = (term == 0)
	isConstTerm = (term == len(coeffs) - 1)

	# Handles case where polynomial is constant
	if isLeadingTerm and isConstTerm: return str(coeffs[0])

	c = float(coeffs[term])

	# Handles formatting the highest order term's coefficient
	if c == 1:
		leadingstr = ''
	elif c == -1:
		leadingstr = '-'
	else:
		leadingstr = f'{c:.03}'

	# Formats coefficient accordingly; superscripts degree unless it's the linear term
	coeff = leadingstr if isLeadingTerm else formatcoeff(term, coeffs)
	degree = f'{superscript(len(coeffs) - 1 - term)}'
	formattedterm = f'{coeff}x' + degree * (degree != '¹')

	polyformat = formatcoeff(term, coeffs) if (isConstTerm or c == 0) else formattedterm

	return polyformat


def formatcoeff(term, coeffs):
	"""Transforms coefficient into appropriate str"""
	c = float(coeffs[term])

	isConstTerm = (term == len(coeffs) - 1)
	isUnitary = (abs(c) == 1)  # checks if c = 1 or -1

	coeff = '' if (isUnitary and not isConstTerm) else abs(c)

	if c > 0:
		formatted = f' + {coeff:.03}'
	elif c < 0:
		formatted = f' - {coeff:.03}'
	else:
		formatted = ''

	return formatted


def superscript(value, reverse=False):
	"""
	Returns a str with any numbers superscripted: H2SO4 -> H²SO⁴
	Change reverse param to 'True' to subscript: H2SO4 -> H₂SO₄
	"""
	digits = ('⁰¹²³⁴⁵⁶⁷⁸⁹', '₀₁₂₃₄₅₆₇₈₉')[reverse]
	transtable = str.maketrans("0123456789", digits)
	formatted = str(value).translate(transtable)

	return formatted
