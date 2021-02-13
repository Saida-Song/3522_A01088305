from file_handler import InvalidFileTypeError
from file_handler import FileHandler
import difflib


class Dictionary:
	"""
	A class that represents a dictionary.
	"""

	def __init__(self):
		"""
		The stats of a Dictionary.
		"""
		self._dictionary = {}

	def load_dictionary(self, filepath):
		"""
		Load a dictionary data to the dictionary.
		:param filepath: a string
		:raise FileNotFoundError: if user entered the wrong path
		:raise InvalidFileTypeError: if entered file is not a json or a txt file
		:precondition: must be an existing json or a txt file
		:postcondition: successfully loaded dictionary
		"""
		try:
			extension = "." + filepath.split(".")[1]
			self._dictionary = FileHandler.load_data(filepath, extension)
		except FileNotFoundError:
			print("!!! The file does not exist.")
		except InvalidFileTypeError as e:
			print(e)
		except Exception as e:
			print(e)
		else:
			print("-- A dictionary successfully loaded.")
		finally:
			print("-- loading dictionary finished.")

	def query_definition(self, word):
		"""
		Explore a word's definition from the dictionary.
		:param word: a string
		:return: a list that contains the definition about the word
		:raise KeyError: if no exact word in the dictionary
		:raise IndexError: if no close match word found
		:raise AttributeError: if the parameter is not a string
		:precondition: must be a string
		:postcondition: a list of definition about the word
		"""
		try:
			definitions = self.write_and_return_definitions_to_file(word.lower())
			self._print_definitions(word, definitions)
			return definitions
		except KeyError:
			try:
				match_word = difflib.get_close_matches(word.lower(), self._dictionary, n=1)[0]
				definitions = self.write_and_return_definitions_to_file(match_word)
				self._print_definitions(match_word, definitions)
				return definitions
			except IndexError:
				print("!!! No such a word or any close matches")
		except AttributeError:
			print("!!! It must be a string")
		finally:
			print(f"These are the most relevant results about \"{word}\".")

	def write_and_return_definitions_to_file(self, word):
		"""
		Return the definitions of the word in the dictionary
		:param word: a string
		:return: a list of string
		"""
		definitions = self._dictionary[word]
		written_line = f"\"{word}\": {definitions}"
		FileHandler.write_lines("saved_queries.txt", written_line)
		return definitions

	@staticmethod
	def _print_definitions(word, definitions):
		"""
		Print the word and definitions
		:param word: a string
		:param definitions: a list of string
		:precondition: must be a string and a list of string
		:postcondition: print the word and the definitions
		"""
		print(word, ":")
		for definition in definitions:
			print("--- " + definition)

	def __len__(self):
		return len(self._dictionary)


def main():
	dictionary = Dictionary()
	dictionary.load_dictionary("data.json")
	run_program = True
	while run_program:
		print("\n-------    Welcome To The Dictionary Program    ------")
		user_input = input("\nPlease enter the word you want to query (enter \"exitprogram\" to exit the program): ")
		if user_input == "exitprogram":
			run_program = False
			print("\n------    Program Ended    ------")
			continue
		dictionary.query_definition(user_input)


if __name__ == '__main__':
	main()
