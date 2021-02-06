from Budget import Budget


class Account:
	"""
	A class that represents a monitored bank account.
	"""

	# self incrementing id number
	account_id = 0

	def __init__(self, bank, user):
		self._account_num = Account.id_generator()
		self._bank = bank
		self._user = user

		# hard-coded categories
		self._budgets = [
			Budget("Games and Entertainment", 500, 0),
			Budget("Clothing and Accessories", 500, 0),
			Budget("Eating out", 500, 0),
			Budget("Miscellaneous", 500, 0)
		]

	def add_to_budget(self, transaction):
		"""
		Add a Transaction to the budget.
		:param transaction: a Transaction
		"""
		for budget in self._budgets:
			if transaction.category == budget.category:
				if self._bank.balance - transaction.amount < 0:
					print("\nNot Enough Balance\n")
					return
				budget.add_to_category(transaction)
				self._bank.balance = transaction.amount
				print("\nTransaction succeed")
				print(transaction)
				return

	def view_by_budget(self, category):
		"""
		Check transactions by category name.
		:param category: a String
		:return: a list
		"""
		for budget in self._budgets:
			if category == budget.category:
				return budget

	@property
	def bank(self):
		"""
		Bank getter.
		:return: a Bank
		"""
		return self._bank

	@property
	def user(self):
		"""
		User getter.
		:return: a User
		"""
		return self._user

	@property
	def budgets(self):
		"""
		List of budgets getter.
		:return: a list
		"""
		return self._budgets

	@property
	def account_num(self):
		"""
		Account number getter.
		:return: an integer
		"""
		return self._account_num

	@staticmethod
	def id_generator():
		"""
		Self-incrementing id number generator.
		:return: an integer
		"""
		identification = Account.account_id + 1
		Account.account_id += 1
		return identification

	def __repr__(self):
		"""
		String method of the class.
		:return: a String
		"""
		return f"Account Number: {self._account_num:05d}, {self._bank}, {self._user}.\n"
