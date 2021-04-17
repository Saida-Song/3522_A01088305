import abc


class PokeObject(abc.ABC):
    """
    The abstract class for all the objects used for Pokedex.
    """

    def __init__(self, name, object_id=None):
        self._name = name
        self._id = object_id

    @property
    def id(self):
        """
        Get id of a pokemon.
        :return: str
        """
        return self._id

    @property
    def name(self):
        """
        Get name of a pokemon.
        :return: str
        """
        return self._name

    def __str__(self):
        """
        Get str representation of a pokemon object.
        :return: str
        """
        return f"Name {self._name}" if not self._id else f"Name: {self._name}\nID: {self._id}\n"


class Ability(PokeObject):
    """
    Class Ability.
    """

    def __init__(self, name, object_id=None, generation=None, effect=None, effect_short=None, pokemon=None):
        """
        Initiate a new Ability.

        :param name: str
        :param object_id: int
        :param generation: str
        :param effect: str
        :param effect_short: str
        :param pokemon: List of str
        """
        super().__init__(name, object_id)
        self._generation = generation
        self._effect = effect
        self._effect_short = effect_short
        self._pokemon = pokemon

    def __str__(self):
        pokemon_list = ', '.join(pokemon for pokemon in self._pokemon)
        return f"{super().__str__()}" \
               f"Generation: {self._generation}\n" \
               f"Effect: {self._effect}\n" \
               f"Effect(short): {self._effect_short}\n" \
               f"Pokemon:\n{pokemon_list}\n\n"


class Stat(PokeObject):
    """
    Class Stat.
    """

    def __init__(self, name, object_id=None, is_battle_only=None, base_value=None):
        """
        Initiate a new Stat Object.

        :param name: str
        :param object_id: str
        :param is_battle_only: boolean
        :param base_value: str
        """
        super().__init__(name, object_id)
        self._is_battle_only = is_battle_only
        self._damage_class = base_value

    def __str__(self):
        return f"{super().__str__()}" \
               f"Battle only: {self._is_battle_only}\n" \
               f"Move Damage Class: {self._damage_class}\n\n"


class Move(PokeObject):
    """
    Class Move.
    """

    def __init__(self, name, object_id=None,
                 generation=None,
                 accuracy=None,
                 pp=None,
                 power=None,
                 type_=None,
                 damage=None,
                 effect=None):
        """
        Construct a new Move class.

        :param name: str
        :param object_id: int
        :param generation: str
        :param accuracy: int
        :param pp: int
        :param power: int
        :param type_: str
        :param damage: str
        :param effect: str

        """
        super().__init__(name, object_id)
        self._generation = generation
        self._accuracy = accuracy
        self._pp = pp
        self._power = power
        self._type = type_
        self._damage = damage
        self._effect = effect

    def __str__(self):
        return f"{super().__str__()}" \
               f"Generation: {self._generation}\n" \
               f"Accuracy: {self._accuracy}\n" \
               f"PP: {self._pp}\n" \
               f"Power: {self._power}\n" \
               f"Type: {self._type}\n" \
               f"Damage class: {self._damage}\n" \
               f"Effect(short): {self._effect}\n\n"


class Pokemon(PokeObject):
    """
    Class Pokemon.
    """

    def __init__(self, name, object_id, height, weight, stats, types, abilities, moves):
        """
        Construct a new Pokemon.

        :param name: str
        :param object_id: int
        :param height: int
        :param weight: int
        :param stats: list of Stat
        :param types: list of Str
        :param abilities: List of Ability
        :param moves: list of Move
        """
        super().__init__(name, object_id)
        self._height = height
        self._weight = weight
        self._stats = stats
        self._types = types
        self._abilities = abilities
        self._moves = moves

    @property
    def height(self):
        """
        Get height of a polemon.
        :return: int
        """
        return self._height

    @property
    def weight(self):
        """
        Get weight of a pokemon.
        :return: int
        """
        return self._weight

    def __str__(self):
        """
        Formatting the str representation of a pokemon.
        :return: str
        """
        type_formatter = ""
        for type in self._types:
            type_formatter += (type + " ")

        stat_formatter = ""
        for stat in self._stats:
            stat_formatter += (str(stat) + "\n")

        ability_formatter = ""
        for ability in self._abilities:
            ability_formatter += (str(ability) + "\n")

        move_formatter = ""
        for move in self._moves:
            move_formatter += (str(move) + "\n")

        return (f"Name: {self.name}\n"
                f"ID: {self.id}\n"
                f"Height: {self._height}\n"
                f"Weight: {self._weight}\n"
                f"Types: {type_formatter}\n"
                f"\nStats:\n------\n{stat_formatter}"
                f"\nAbilities:\n------\n{ability_formatter}"
                f"nMoves:\n------\n{move_formatter}")


def main():
    pass


if __name__ == '__main__':
    main()
