# https://docs.python.org/3/reference/datamodel.html 
class Polynomial:
	def __init__(self, *coeffs):
		self.coeffs = coeffs
	def __repr__(self):
		return 'Polynomial(*{!r})'.format(self.coeffs)
	def __add__(self, other):
		z = (x + y for x, y in zip(self.coeffs, other.coeffs))

        #here * means unzip 
		return Polynomial(*z)

	def __len__(self):
		return len(self.coeffs)

p1 = Polynomial(1,2,3)
p2 = Polynomial(3,4,5)

p3=p1+p2

