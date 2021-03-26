from CSTstore import Store


def main():
	"""
	Driver Method of the CST store program.
	"""
	new_store = Store()
	run = True
	while run:
		print("-" * 10, "Welcome to CST store", "-" * 10)
		print(f"What Do You Want To Do Today?\n"
			  f"	1 - Process Web Orders\n"
			  f"	2 - Check Inventory\n"
			  f"	3 - Exit")
		user_input = input("Please enter your option")
		if user_input == "1":
			file_path = input("Please enter your file name you want to proceed")
			new_store.receive_order(file_path)
			input("'Enter' to Continue\n")
			continue
		if user_input == "2":
			new_store.check_inventory()
			input("'Enter' to Continue\n")
			continue
		if user_input == "3":
			new_store.generate_daily_transaction_report()
			run = False
			continue


if __name__ == '__main__':
	main()
