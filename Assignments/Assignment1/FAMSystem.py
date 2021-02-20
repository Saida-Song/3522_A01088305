from AngelAccount import AngelAccount
from TroubleMaker import TroubleMaker
from RebelAccount import RebelAccount
from Transaction import Transaction
from Bank import Bank
from User import User


class FAMSystem:
	"""
	A class that simulates a Family Appointed Moderator system.
	"""

	def __init__(self):
		"""
		Stats of the FAMSystem.
		"""
		self._accounts = []
		self.load_test_user()

	def print_accounts(self):
		"""
		Print all accounts in the System.
		"""
		for acc in self._accounts:
			print(acc)

	def add_account(self, account):
		"""
		Append an account to the system.
		:param account: an Account
		"""
		self._accounts.append(account)

	def register_menu(self):
		"""
		Register an Account.
		:raise ValueError: if enter wrong input
		:precondition: the user follows the instruction
		:return: an Account
		"""
		try:
			print("--Please Choose An Account Type You Want To Create:")
			user_type = input("	1. Angel\n	2. TroubleMaker\n	3. Rebel\nType: ")
			user_name = input("Name Of The User: ")
			user_age = input("Age Of The User: ")
			bank_name = input("Bank Name Of The Account: ")
			balance = int(input("Please Set Up The Initial Balance Of The Account: "))
			new_account = self.register_an_account(user_type, user_name, user_age, bank_name, balance)
			self.budget_initial_setting_menu(new_account)
		except ValueError:
			print("-- Please Enter Correct Information")
		else:
			print("-- Succeed. New Account is:", new_account)
			return new_account

	def manage_account_menu(self, account):
		"""
		Manages an account with an interface.
		:param account: an Account
		"""
		run_menu = True
		while run_menu:
			print(f"\n-- Managing The Account:\n{account}")
			print("\n    1. View Budgets\n	2. Record a Transaction\n    3. View Transactions by Budget")
			print("    4. View Bank Account Details\n    5. Exit The Menu")
			manage_input = input("Please Choose An Operation: ")
			if manage_input == "1":
				account.view_budgets()
			if manage_input == "2":
				self.transaction_record_menu(account)
			if manage_input == "3":
				category_list = ["Games and Entertainment", "Clothing and Accessories", "Eating out", "Miscellaneous"]
				print(f"	1. Games and Entertainment\n	2. Clothing and Accessories")
				print(f"	3. Eating out\n    4. Miscellaneous")
				category_input = int(input("Please Enter The Number: ").strip()) - 1
				account.view_by_budget(category_list[category_input])
			if manage_input == "4":
				print(account)
				for budget in account.budgets:
					print("--", budget)
					account.view_by_budget(budget.category)
			if manage_input == "5":
				return
			input("Press Enter To Continue")

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
		self._accounts.append(AngelAccount(bank3, user3))
		self._accounts.append(TroubleMaker(bank2, user2))
		self._accounts.append(RebelAccount(bank, user1))

	@property
	def accounts(self):
		"""
		Account list getter.
		:return: a list
		"""
		return self._accounts

	@staticmethod
	def register_an_account(user_type, name, age, bank_name, balance):
		"""
		Register an account.
		:param user_type: a String
		:param name: a String
		:param age: a String
		:param bank_name: a String
		:param balance: a float
		:return: an Account
		"""
		bank = Bank(bank_name, balance)
		user = User(name, age)
		if user_type == "1":
			return AngelAccount(bank, user)
		if user_type == "2":
			return TroubleMaker(bank, user)
		if user_type == "3":
			return RebelAccount(bank, user)
		raise ValueError

	@staticmethod
	def budget_initial_setting_menu(account):
		"""
		Set the initial limit of the budgets.
		:param account: an Account
		"""
		for budget in account.budgets:
			initial_limit = int(input(f"Please Set The Limit For Category {budget.category}: "))
			budget.limit = initial_limit

	@staticmethod
	def transaction_record_menu(account):
		"""
		Interface of recording a Transaction.
		:param account: an Account
		"""
		try:
			category_list = ["Games and Entertainment", "Clothing and Accessories", "Eating out", "Miscellaneous"]
			print(f"	1. Games and Entertainment\n	2. Clothing and Accessories\n	3. Eating out\n    4. Miscellaneous")
			category_input = int(input("please choose which category you want to store the transaction (enter the number)"))
			category = category_list[category_input - 1]
			amount = float(input("Please enter the amount of the transaction"))
			place = input("please enter the location the transaction happened")
			account.record_a_transaction(Transaction(amount, category, place))
		except IndexError:
			print("-- Please Enter Correct Information")


def main():
	"""
	Main function of the FAM system.
	"""
	new_fam = FAMSystem()
	running = True
	while running:
		print("\n-------- Welcome to FAM System --------\n")
		print("-- Hi, Dear Customer, What do you want to do today?")
		print("    1. View Accounts\n    2. Register An Account\n    3. Manage An Account\n")
		main_menu_input = input("Please Enter The Number (\"exit\" to exit the program): ").strip()
		if main_menu_input == "1":
			new_fam.print_accounts()
		if main_menu_input == "2":
			new_account = new_fam.register_menu()
			new_fam.add_account(new_account)
		if main_menu_input == "3":
			acc_num = int(input("Please Enter The Account Number You Want To Manage: "))
			for acc in new_fam.accounts:
				if acc_num == acc.account_num:
					new_fam.manage_account_menu(acc)
			continue
		if main_menu_input.lower() == "exit":
			print("-- Thanks For Using FAMSystem, Have A Good Day")
			return
		input("Press Enter To Continue")


if __name__ == '__main__':
	main()
