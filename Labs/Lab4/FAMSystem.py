from Account import Account
from Bank import Bank
from User import User
from Transaction import Transaction


class FAMSystem:
	"""
	A class that simulates a Family Appointed Moderator system.
	"""

	def __init__(self):
		self._accounts = []
		self.load_test_user()

	def view_budgets(self, account_num):
		"""
		View budgets of a given account number.
		:param account_num: an integer
		"""
		for acc in self._accounts:
			if account_num == acc.account_num:
				for budget in acc.budgets:
					print(budget)
					return

	def add_to_budget(self, acc_num, transaction):
		"""
		Add a Transaction to a budget of an account.
		:param acc_num: an integer
		:param transaction: a Transaction
		"""
		for account in self._accounts:
			if acc_num == account.account_num:
				account.add_to_budget(transaction)
				return

	def load_test_user(self):
		"""
		Test function that auto-generate accounts and appended to the account list.
		"""
		bank = Bank("RBC", 5000)
		bank2 = Bank("RBC", 5000)
		bank3 = Bank("RBC", 5000)
		user1 = User("Saida", 20)
		user2 = User("Andrew", 20)
		user3 = User("Scott", 20)
		self._accounts.append(Account(bank3, user3))
		self._accounts.append(Account(bank2, user2))
		self._accounts.append(Account(bank, user1))

	@property
	def accounts(self):
		"""
		Account list getter.
		:return: a list
		"""
		return self._accounts


def main():
	"""
	Main function of the FAM system.
	"""
	new_fam = FAMSystem()
	working = True
	while working:
		print(f"-------- Welcome to FAM System --------\n"
			  f"Here are the account numbers\n"
			  f"{new_fam.accounts}\n")
		user_input = input("Please enter the account number that you want to add a transaction to ('q' to quit): ")
		if user_input == "q":
			working = False
			continue
		acc_num = int(user_input)
		category_list = ["Games and Entertainment", "Clothing and Accessories", "Eating out", "Miscellaneous"]
		print(f"	1. Games and Entertainment\n	2. Clothing and Accessories\n	3. Eating out\n    4. Miscellaneous")
		category_input = int(input("please choose which category you want to store the transaction (enter the number)"))
		category = category_list[category_input - 1]
		amount = float(input("Please enter the amount of the transaction"))
		place = input("please enter the location the transaction happened")
		new_fam.add_to_budget(acc_num, Transaction(amount, category, place))


if __name__ == '__main__':
	main()
