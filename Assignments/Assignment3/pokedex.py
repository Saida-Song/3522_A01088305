from pokeretriever.poke_request import Request, setup_request_commandline
from pokeretriever.handlers import ModeHandler, InputHandler, ExpandHandler, ReadDataFromFileHandler, AbilityHandler, \
    MoveHandler, OutputHandler, PokemonHandler, PokemonExtendedHandler
from pokeretriever.pokedex_enums import ModeEnum


class PokeFacade:
    """
    Provide a simplified interface to the pokeretriever package.
    """
    def __init__(self):
        """
        Construct a new Facade.
        """
        self.pokemon_start_handler = None
        self.move_start_handler = None
        self.ability_start_handler = None

        self.mode_handler = ModeHandler()
        self.input_handler = None
        self.expand_handler = ExpandHandler()
        self.pokemon_handler = None
        self.ability_handler = AbilityHandler()
        self.move_handler = MoveHandler()
        self.output_handler = OutputHandler()

    def execute_request(self, request: Request):
        """
        Executed the coming request.
        :param request: Request
        """
        if self.pokemon_start_handler:
            if request.input_file:
                self.input_handler = ReadDataFromFileHandler()
            else:
                self.input_handler = InputHandler()

            self.pokemon_start_handler.set_handler(self.input_handler)
            self.input_handler.set_handler(self.expand_handler)
            # check if expanded needed or not
            if request.expanded:
                self.pokemon_handler = PokemonExtendedHandler()
            else:
                self.pokemon_handler = PokemonHandler()

            self.expand_handler.set_handler(self.pokemon_handler)

            if request.output:
                self.pokemon_handler.set_handler(self.output_handler)

            self.pokemon_start_handler.handle_request(request)

        elif self.ability_start_handler:
            if request.input_file:
                self.input_handler = ReadDataFromFileHandler()
            else:
                self.input_handler = InputHandler()

            self.ability_start_handler.set_handler(self.input_handler)
            self.input_handler.set_handler(self.expand_handler)
            if request.output:
                self.ability_handler.set_handler(self.output_handler)

            self.expand_handler.set_handler(self.ability_handler)
            self.ability_start_handler.handle_request(request)

        elif self.move_start_handler:
            if request.input_file:
                self.input_handler = ReadDataFromFileHandler()
            else:
                self.input_handler = InputHandler()

            self.move_start_handler.set_handler(self.input_handler)
            self.input_handler.set_handler(self.expand_handler)
            if request.output:
                self.move_handler.set_handler(self.output_handler)
            self.expand_handler.set_handler(self.move_handler)

            self.move_start_handler.handle_request(request)


def main(my_request: Request):
    """
    Drives the program.
    """
    if request.mode == ModeEnum.POKEMON.value:
        pokeFacade = PokeFacade()
        pokeFacade.pokemon_start_handler = ModeHandler()
        pokeFacade.execute_request(my_request)
    elif request.mode == ModeEnum.MOVE.value:
        pokeFacade = PokeFacade()
        pokeFacade.move_start_handler = ModeHandler()
        pokeFacade.execute_request(my_request)
    elif request.mode == ModeEnum.ABILITY.value:
        pokeFacade = PokeFacade()
        pokeFacade.ability_start_handler = ModeHandler()
        pokeFacade.execute_request(my_request)


if __name__ == '__main__':
    request = setup_request_commandline()
    main(request)
