class User:

	def __init__(self, name, age):
		self._name = name
		self._age = age

	@property
	def name(self):
		return self._name

	@property
	def age(self):
		return self._age

	def __repr__(self):
		return f"Name: {self._name}, Age: {self._age}"
