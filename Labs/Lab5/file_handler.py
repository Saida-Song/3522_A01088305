import json
import ast
from FileExtensions import FileExtensions


class FileHandler:
	"""
	A class that represents a handler for writing to or reading from a file.
	"""

	@staticmethod
	def write_lines(path, lines):
		"""
		Write lines to a file
		:param path: a string
		:param lines: a string
		:return:
		"""
		with open(path, mode='a', encoding='utf-8') as saving_file:
			saving_file.write(lines + ",\n")

	@staticmethod
	def load_data(path, file_extension):
		"""
		Returns a dictionary
		:param path: a string
		:param file_extension: a string
		:return:
		"""
		if file_extension == FileExtensions.JSON.value:
			return FileHandler._read_json_file(path)
		if file_extension == FileExtensions.TXT.value:
			return FileHandler._read_txt_file(path)
		raise InvalidFileTypeError("!!! The file extension must be .json or .txt")

	@staticmethod
	def _read_json_file(path):
		"""
		Returns a dictionary from a json file.
		:param path: a string
		:return: a dictionary
		"""
		with open(path, mode='r', encoding='utf-8') as file:
			data = json.load(file)
			return data

	@staticmethod
	def _read_txt_file(path):
		"""
		Returns a dictionary from a txt file.
		:param path: a string
		:return: a dictionary
		"""
		with open(path, mode='r', encoding='utf-8') as file:
			data = file.read()
			try:
				output_dict = ast.literal_eval(data)
				return output_dict
			except SyntaxError:
				output_dict = ast.literal_eval("{" + data + "}")
				return output_dict
			except Exception:
				print("---   Something went wrong when loading the file, please try again")


class InvalidFileTypeError (Exception):
	"""
	An exception when the file extension is not .json or .txt.
	"""

	def __init__(self, invalid_file_type):
		super().__init__("The file must be a json or a txt file")
		self.invalid_file_type = invalid_file_type
