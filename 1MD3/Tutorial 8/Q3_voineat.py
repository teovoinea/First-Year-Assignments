class Vector():
	def __init__(self, l):
		assert type(l) == type([])
		for i in l:
			assert type(i) == type(2) or type(i) == type(0.1)
		self.l = l
	def dim(self):
		return len(self.l)
	def __getitem__(self, i):
		assert i > 0 and i < len(self.l) + 1
		return self.l[i - 1]
	def __setitem__(self, i, x):
		assert i > 0 and i < len(self.l) + 1
		self.l[i - 1] = x
		return self.l
	def __str__(self):
		return "Vector: " + str(self.l)
	def __add__(self, other):
		assert type(other) == type(self) and other.dim() == self.dim()
		newL = []
		for i in range(len(other.l)):
			newL.append(other.l[i] + self.l[i])
		return Vector(newL)
	def __mul__(self, scalar):
		assert type(scalar) == type(2) or type(scalar) == type(0.1)
		newL = []
		for i in self.l:
			newL.append(i * scalar)
		return Vector(newL)
	def __mul__(self, other):
		assert type(other) == type(self) and other.dim() == self.dim() or type(other) == type(2) or type(other) == type(0.1)
		if type(other) == type(self):
			newL = []
			for i in range(len(other.l)):
				newL.append(other.l[i] * self.l[i])
			return sum(newL)
		else:
			newL = []
			for i in self.l:
				newL.append(i * other)
			return Vector(newL)
	def __rmul__(self, other):
		assert type(other) == type(self) and other.dim() == self.dim() or type(other) == type(2) or type(other) == type(0.1)
		if type(other) == type(self):
			newL = []
			for i in range(len(other.l)):
				newL.append(other.l[i] + self.l[i])
			return sum(newL)
		else:
			newL = []
			for i in self.l:
				newL.append(i * other)
			return Vector(newL)