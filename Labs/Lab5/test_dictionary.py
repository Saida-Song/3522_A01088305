from unittest import TestCase
from dictionary import Dictionary
from io import StringIO
from unittest.mock import patch
import json
import ast


class TestDictionary(TestCase):

	def test_load_dictionary_without_loading(self):
		dictionary = Dictionary()
		expected = 0
		self.assertEqual(len(dictionary), expected)

	def test_load_dictionary_not_existing_filepath(self):
		dictionary = Dictionary()
		expected = """!!! The file does not exist.
-- loading dictionary finished.
"""
		with patch('sys.stdout', new=StringIO()) as mock:
			dictionary.load_dictionary("notExist.txt")
			self.assertEqual(mock.getvalue(), expected)

	def test_load_dictionary_with_loading_json_file(self):
		dictionary = Dictionary()
		dictionary.load_dictionary("data.json")
		expected = 49537
		self.assertEqual(len(dictionary), expected)

	def test_load_dictionary_with_loading_txt_file_dictionary(self):
		with open("data.json", mode='r', encoding='utf-8') as file:
			data_txt = str(json.load(file))
			with open("data.txt", mode='w', encoding='utf-8') as txt_file:
				txt_file.write(data_txt)

		dictionary = Dictionary()
		dictionary.load_dictionary("data.txt")
		expected = 49537
		self.assertEqual(len(dictionary), expected)

	def test_load_dictionary_with_loading_saved_user_query_file(self):
		open("saved_queries.txt", mode='w').close()
		dictionary = Dictionary()
		dictionary.load_dictionary("data.txt")
		dictionary.query_definition("rain")
		dictionary.load_dictionary("saved_queries.txt")
		expected = 1
		self.assertEqual(len(dictionary), expected)

	def test_query_definition_query_a_word(self):
		dictionary = Dictionary()
		dictionary.load_dictionary("data.json")
		actual = dictionary.query_definition("abandoned industrial site")
		expected = ["Site that cannot be used for any purpose, being contaminated by pollutants."]
		self.assertEqual(actual, expected)

	def test_query_definition_query_an_upper_case_word(self):
		dictionary = Dictionary()
		dictionary.load_dictionary("data.json")
		actual = dictionary.query_definition("RAIN")
		expected = ["Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.",
					"To fall from the clouds in drops of water."]
		self.assertEqual(actual, expected)

	def test_query_definition_query_a_close_match_word(self):
		dictionary = Dictionary()
		dictionary.load_dictionary("data.json")
		actual = dictionary.query_definition("raain")
		expected = ["Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.",
					"To fall from the clouds in drops of water."]
		self.assertEqual(actual, expected)

	def test_query_definition_query_an_empty_string(self):
		dictionary = Dictionary()
		dictionary.load_dictionary("data.json")
		actual = dictionary.query_definition("")
		expected = None
		self.assertEqual(actual, expected)

	def test_query_definition_query_without_matching_word(self):
		dictionary = Dictionary()
		dictionary.load_dictionary("data.json")
		actual = dictionary.query_definition("alskjdlkfjlas")
		expected = None
		self.assertEqual(actual, expected)

	def test_query_definition_writing_to_a_txt_file(self):
		dictionary = Dictionary()
		dictionary.load_dictionary("data.json")
		dictionary.query_definition("abandoned industrial site")
		with open("saved_queries.txt", mode='r', encoding='utf-8') as file:
			data = ast.literal_eval("{" + file.read() + "}")
		actual = data["abandoned industrial site"]
		open("saved_queries.txt", mode='w').close()
		expected = ['Site that cannot be used for any purpose, being contaminated by pollutants.']
		self.assertEqual(actual, expected)


