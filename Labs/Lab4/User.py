class User:
	"""
	A class that represents a user.
	"""

	def __init__(self, name, age):
		self._name = name
		self._age = age

	@property
	def name(self):
		"""
		Name getter.
		:return: a String
		"""
		return self._name

	@property
	def age(self):
		"""
		Age getter.
		:return: an integer
		"""
		return self._age

	def __repr__(self):
		"""
		String method of the class.
		:return: a string
		"""
		return f"Name: {self._name}, Age: {self._age}"
