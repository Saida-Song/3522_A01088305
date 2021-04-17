import enum


class ModeURLEnum(enum.Enum):
	"""
	Enum of endpoints urls.
	"""
	POKEMON = "https://pokeapi.co/api/v2/pokemon/{}/"
	ABILITY = "https://pokeapi.co/api/v2/ability/{}/"
	MOVE = "https://pokeapi.co/api/v2/move/{}/"
	STAT = "https://pokeapi.co/api/v2/stat/{}/"


class ModeEnum(enum.Enum):
	"""
	Enum of Pokedex modes.
	"""
	POKEMON = "pokemon"
	ABILITY = "ability"
	MOVE = "move"