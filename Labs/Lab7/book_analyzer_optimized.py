"""
This module is responsible for holding a badly written (but not so bad
that you won't find this in the workplace) BookAnalyzer class that needs
to be profiled and optimized.
"""

import re


class BookAnalyzer:
	"""
    This class provides the ability to load the words in a text file in
    memory and provide the ability to filter out the words that appear
    only once.
    """

	# a constant to help filter out common punctuation.
	COMMON_PUNCTUATION = ",*;.:([])"

	def __init__(self):
		self.text = None

	def read_data(self, src="House of Usher.txt"):
		"""
		Reads through a text file and loads in all the words. This
		function also processes the words such that all whitespace and
		common punctuation is removed.
		:param src: the name of the file, a string
		"""
		with open(src, mode='r', encoding='utf-8') as book_file:
			content = ''.join(book_file)
			table = str.maketrans('', '', self.COMMON_PUNCTUATION)
			content_no_pun = content.translate(table)
			self.text = {word for word in content_no_pun.lower().split()}

	def find_unique_words(self):
		return self.text


def main():
	book_analyzer = BookAnalyzer()
	book_analyzer.read_data()
	unique_words = book_analyzer.find_unique_words()
	print("-" * 50)
	print(f"List of unique words (Count: {len(unique_words)})")
	print("-" * 50)
	for word in unique_words:
		print(word)
	print("-" * 50)


if __name__ == '__main__':
	main()
