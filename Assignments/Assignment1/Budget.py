class Budget:
	"""
	A class that represents a Budget of a category.
	"""

	def __init__(self, category, limit, spent):
		self._category = category
		self._limit = limit
		self._spent = spent
		self._locked = False
		self._transaction = []

	def add_to_category(self, transaction):
		"""
		Add a Transaction to the category.
		:param transaction: a Transaction
		"""
		if not self._locked:
			self._transaction.append(transaction)
			self.spent = transaction.amount
			return True
		print(f"Category {self._category} is locked")
		return False

	@property
	def category(self):
		"""
		Category getter.
		:return: a String
		"""
		return self._category

	@property
	def limit(self):
		"""
		Limit getter.
		:return: A float
		"""
		return self._limit

	@limit.setter
	def limit(self, amount):
		"""
		Set the limit.
		:param amount: a float
		"""
		if amount > 0:
			self._limit = amount
			return
		raise ValueError("Amount Less Than 0")

	@property
	def spent(self):
		"""
		Spent amount getter.
		:return: a float
		"""
		return self._spent

	@spent.setter
	def spent(self, amount):
		"""
		Set the spent amount of the budget.
		:param amount: a float
		"""
		self._spent += amount

	@property
	def locked(self):
		"""
		Locked property getter.
		:return: a boolean
		"""
		return self._locked

	@locked.setter
	def locked(self, status):
		"""
		Set the budget to lock or not.
		:param status: a boolean
		"""
		self._locked = status

	@property
	def transaction(self):
		"""
		transactions getter.
		:return: a list
		"""
		return self._transaction

	def __repr__(self):
		"""
		String method of the class.
		:return: a String
		"""
		return f"Category: {self._category}, locked: {self._locked}, Limit: {self._limit}" \
			   f", Spent: {self._spent}, Amount Left: {self._limit - self._spent}"
