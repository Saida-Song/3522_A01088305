from .api_request import APIHandlers
from .pokedex_enums import ModeURLEnum
import asyncio
from .poke_object import *


class ObjectProducer(abc.ABC):
    """
	A class can produce objects from a given api response.
	"""

    @staticmethod
    @abc.abstractmethod
    def handle_response(response: dict) -> list:
        """
		Produce Objects from the given response.

		:param response: a dictionary
		:return: a list
		"""
        pass


class HandleRequestAPIInterface(abc.ABC):
    """
	Interface that need to handle api requests.
	"""

    @staticmethod
    @abc.abstractmethod
    def handle_api(id_: list):
        """
		Produce a list of objects from requested response with a list of id.

		:param id_: a list
		:return: a list of objects
		"""
        pass


class StatProducer(ObjectProducer):

    @staticmethod
    def handle_response(response: dict):
        """
		Produce a list of Tuples from the given response.

		:param response: a dictionary
		:return: a list
		"""
        return [(stat['stat']['name'], stat['base_stat']) for stat in response.get('stats')]


class StatExtendedProducer(ObjectProducer):

    @staticmethod
    def handle_response(response: dict):
        """
		Produce a list of Stat objects from the given response.

		:param response: a dictionary
		:return: a list
		"""
        loop = asyncio.get_event_loop()
        stat_list = StatProducer.handle_response(response)
        stat_name_list = [stat[0] for stat in stat_list]
        res = loop.run_until_complete(APIHandlers.process_requests(stat_name_list, ModeURLEnum.STAT.value))
        stat_expanded_list = []
        for (stat, details) in zip(stat_list, res):
            name = stat[0]

            if details["move_damage_class"]:
                move_damage_class = details["move_damage_class"]["name"]
            else:
                move_damage_class = "N/A"
            identity = details['id']
            battle_only = details['is_battle_only']
            stat_expanded_list.append(Stat(name, identity, battle_only, move_damage_class))
        return stat_expanded_list


class AbilityProducer(ObjectProducer):

    @staticmethod
    def handle_response(response: dict):
        """
		Produce a list of ability names from the given response.

		:param response: a dictionary
		:return: a list
		"""
        return [ability['ability']['name'] for ability in response.get('abilities')]


class AbilityExtendedProducer(ObjectProducer, HandleRequestAPIInterface):

    @staticmethod
    def handle_response(response: dict):
        """
		Produce a list of Ability objects from the given response.

		:param response: a dictionary
		:return: a list
		"""
        ability_name_list = AbilityProducer.handle_response(response)
        return AbilityExtendedProducer.handle_api(ability_name_list)

    @staticmethod
    def handle_api(id_: list):
        """
		Produce a list of Ability objects from requested response with a list of id.

		:param id_: a list
		:return: a list
		"""
        loop = asyncio.get_event_loop()
        abilities = loop.run_until_complete(APIHandlers.process_requests(id_, ModeURLEnum.ABILITY.value))
        ability_list = []
        for ability in abilities:
            if ability is None:
                ability_list.append(None)
                continue
            name = ability['name']
            identity = ability['id']
            generation = ability['generation']['name']
            effects = [effect['effect'] for effect in ability['effect_entries'] if effect['language']['name'] == 'en']
            effect_short = [effect['short_effect'] for effect in ability['effect_entries'] if
                            effect['language']['name'] == 'en']
            pokemons = [pokemon['pokemon']['name'] for pokemon in ability['pokemon']]
            ability_list.append(Ability(name, identity, generation, effects, effect_short, pokemons))
        return ability_list


class MoveProducer(ObjectProducer):

    @staticmethod
    def handle_response(response: dict):
        """
		Produce a list of Tuples objects from the given response.

		:param response: a dictionary
		:return: a list
		"""
        return [(move['move']['name'], move['version_group_details'][0]['level_learned_at'])
                for move in response.get('moves')]


class MoveExtendedProducer(ObjectProducer, HandleRequestAPIInterface):

    @staticmethod
    def handle_response(response: dict):
        """
		Produce a list of Move objects from the given response.

        :param id_:
		:param response: a dictionary
		:return: a list
		"""
        move_name_list = [move[0] for move in MoveProducer.handle_response(response)]
        return MoveExtendedProducer.handle_api(move_name_list)

    @staticmethod
    def handle_api(id_: list):
        """
		Produce a list of Move objects from requested response with a list of id.

		:param id_: a list
		:return: a list of objects
		"""
        loop = asyncio.get_event_loop()
        moves = loop.run_until_complete(APIHandlers.process_requests(id_, ModeURLEnum.MOVE.value))
        move_list = []
        for move in moves:
            if move is None:
                move_list.append(None)
                continue
            name = move['name']
            identity = move['id']
            generation = move['generation']['name']
            accuracy = move['accuracy']
            pp = move['pp']
            power = move['power']
            move_type = move['type']['name']
            damage_class = move['damage_class']['name']
            effects = [effect['short_effect'] for effect in move['effect_entries']
                       if effect['language']['name'] == 'en']
            move_list.append(Move(name, identity, generation, accuracy, pp,
                                  power, move_type, damage_class, effects))
        return move_list


class PokemonProducer(ObjectProducer):

    @staticmethod
    def handle_response(id_: list):
        """
        Produce a list of Pokemon objects from the given id.

        :param id_: a list
        :return: a list
        """
        loop = asyncio.get_event_loop()
        pokemons = loop.run_until_complete(APIHandlers.process_requests(id_, ModeURLEnum.POKEMON.value))
        pokemons_list = []

        for pokemon in pokemons:
            name = pokemon['name']
            identity = pokemon['id']
            height = pokemon['height']
            weight = pokemon['weight']
            types = []
            for t in pokemon["types"]:
                types.append(t["type"]["name"])

            stats = StatProducer.handle_response(pokemon)
            abilities = AbilityProducer.handle_response(pokemon)
            moves = MoveProducer.handle_response(pokemon)
            pokemons_list.append(Pokemon(name, identity, height, weight, stats, types, abilities, moves))
        return pokemons_list


class PokemonExtendedProducer(ObjectProducer):

    @staticmethod
    def handle_response(id_):
        """
		Produce a list of Pokemon objects from the given response.

		:param id_: a dictionary
		:return: a list
		"""

        loop = asyncio.get_event_loop()
        pokemons = loop.run_until_complete(APIHandlers.process_requests(id_, ModeURLEnum.POKEMON.value))
        pokemons_list = []

        for pokemon in pokemons:
            if pokemon is None:
                pokemons_list.append(None)
                continue
            name = pokemon['name']
            identity = pokemon['id']
            height = pokemon['height']
            weight = pokemon['weight']
            types = []
            for t in pokemon["types"]:
                types.append(t["type"]["name"])

            stats = StatExtendedProducer.handle_response(pokemon)
            abilities = AbilityExtendedProducer.handle_response(pokemon)
            moves = MoveExtendedProducer.handle_response(pokemon)

            pokemons_list.append(Pokemon(name, identity, height, weight, stats, types, abilities, moves))
        return pokemons_list

#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     pokemon = MoveExtendedProducer.handle_api([4])[0]
#     print(pokemon)
