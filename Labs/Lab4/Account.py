from Budget import Budget


class Account:

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

	def add_to_budget(self, transaction):
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
		for budget in self._budgets:
			if category == budget.category:
				return budget

	@property
	def bank(self):
		return self._bank

	@property
	def user(self):
		return self._user

	@property
	def budgets(self):
		return self._budgets

	@property
	def account_num(self):
		return self._account_num

	@staticmethod
	def id_generator():
		identification = Account.account_id + 1
		Account.account_id += 1
		return identification

	def __repr__(self):
		return f"Account Number: {self._account_num:05d}, {self._bank}, {self._user}.\n"
