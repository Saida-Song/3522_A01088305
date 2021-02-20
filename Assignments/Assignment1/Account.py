from Budget import Budget
import abc


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

		self._budgets = [
			Budget("Games and Entertainment", 500, 0),
			Budget("Clothing and Accessories", 500, 0),
			Budget("Eating out", 500, 0),
			Budget("Miscellaneous", 500, 0)
		]

	def view_budgets(self):
		"""
		View budgets status of the account.
		"""
		for budget in self._budgets:
			print(budget)

	def record_a_transaction(self, transaction):
		"""
		Add a Transaction to the budget.
		:param transaction: a Transaction
		"""
		for budget in self._budgets:
			if transaction.category == budget.category:
				if self._bank.balance - transaction.amount < 0:
					print("\n-- No Enough Balance\n")
					return
				result = budget.add_to_category(transaction)
				if result:
					self.check_if_warn(budget)
					self._bank.balance = transaction.amount
					print("\n-- Transaction Succeed")
					print(transaction)
					return
				print(f"-- Transaction Failed")

	def view_by_budget(self, category):
		"""
		Check transactions by category name.
		:param category: a String
		:return: a list
		"""
		for budget in self._budgets:
			if category == budget.category:
				for transaction in budget.transaction:
					print("    -", transaction)

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

	@abc.abstractmethod
	def check_if_warn(self, budget):
		pass

	@abc.abstractmethod
	def lock_out(self, budget):
		pass

	@abc.abstractmethod
	def __repr__(self):
		pass
