from .poke_request import Request
from .poke_object_producer import *
from datetime import datetime


class BaseRequestHandler(abc.ABC):
    """
    The Super class of all handlers.
    """

    def __init__(self):
        """
        stats of the class.
        """
        self.next_handler = None

    @abc.abstractmethod
    def handle_request(self, request: Request):
        """
        handle the given request.
        :param request: a Request
        """
        pass

    def set_handler(self, handler):
        """
        Set the next handler.
        :param handler: a Handler object.
        """
        self.next_handler = handler


class ModeHandler(BaseRequestHandler):

    def handle_request(self, request: Request):
        """
        handle the given request.
        :param request: a Request
        """
        print("===Verifying mode")
        if request.mode is not None:
            if request.mode in ["pokemon", "ability", "move"]:
                if not self.next_handler:
                    return True
                else:
                    return self.next_handler.handle_request(request)
            else:
                print(f"Invalid query! {request.mode} is unsupported, please choose from the supported mode : "
                      f"pokemon | Ability | move")
        else:
            print("Invalid query! You have to enter a mode from pokemon | Ability | move")
            return False


class InputHandler(BaseRequestHandler):

    def handle_request(self, request: Request):
        print("===Verifying input")

        if request.input_file is not None:
            if request.input_file.lower().endswith('.txt'):
                if not self.next_handler:
                    return True
                else:
                    return self.next_handler.handle_request(request)
        elif request.input_data is not None:
            if not self.next_handler:
                return True
            request.result = [request.input_data]
            return self.next_handler.handle_request(request)
        else:
            print("Invalid query! The input file or input data is missing, please check ur query!")
            return False


class ExpandHandler(BaseRequestHandler):

    def handle_request(self, request: Request):
        print("===Verifying expand")

        if request.expanded is True:
            if request.mode == "pokemon":
                if not self.next_handler:
                    return True
                else:
                    return self.next_handler.handle_request(request)
            else:
                print("Invalid query! Expand is only supported by pokemon mode!")
                return False
        else:
            if not self.next_handler:
                return True
            return self.next_handler.handle_request(request)


class ReadDataFromFileHandler(BaseRequestHandler):

    def handle_request(self, request: Request):
        """
        handle the given request.
        :param request: a Request
        """
        print("===Verifying input file")

        try:
            with open(request.input_file, mode='r', encoding='utf-8') as file:
                content = ''.join(file).split()
                if not self.next_handler:
                    print(content)
                    return True
                request.result = content
                return self.next_handler.handle_request(request)
        except FileNotFoundError as e:
            print(e)
            return False


class PokemonHandler(BaseRequestHandler):
    """
    Produce a list of unexpanded Pokemon objects and send it to next handler
    or print it to the console.
    """

    def handle_request(self, request: Request):
        """
        handle the given request.
        :param request: a Request
        """
        print("===Verifying pokemon")
        pokemon = PokemonProducer.handle_response(request.result)
        if self.next_handler is None:
            for i in pokemon:
                print(i)
        else:
            request.result = pokemon
            self.next_handler.handle_request(request)


class PokemonExtendedHandler(BaseRequestHandler):
    """
    Produce a list of expanded Pokemon objects and send it to next handler
    or print it to the console.
    """

    def handle_request(self, request: Request):
        """
        handle the given request.
        :param request: a Request
        """
        print("===Verifying pokemon expand")

        pokemon = PokemonExtendedProducer.handle_response(request.result)
        if self.next_handler is None:
            for i in pokemon:
                print(i)
        else:
            request.result = pokemon
            self.next_handler.handle_request(request)


class AbilityHandler(BaseRequestHandler):
    """
    Produce a list of Ability objects and send it to next handler
    or print it to the console.
    """

    def handle_request(self, request: Request):
        """
        handle the given request.
        :param request: a Request
        """
        print("===Verifying ability")

        abilities = AbilityExtendedProducer.handle_api(request.result)
        if self.next_handler is None:
            for i in abilities:
                print(i)
        else:
            request.result = abilities
            self.next_handler.handle_request(request)


class MoveHandler(BaseRequestHandler):
    """
    Produce a list of Move objects and send it to next handler
    or print it to the console.
    """

    def handle_request(self, request: Request):
        """
        handle the given request.
        :param request: a Request
        """
        print("===Verifying Move")

        moves = MoveExtendedProducer.handle_api(request.result)
        if self.next_handler is None:
            for i in moves:
                print(i)
        else:
            request.result = moves
            self.next_handler.handle_request(request)


class OutputHandler(BaseRequestHandler):
    """
    A handler that print the result to a specified text file.
    """

    def handle_request(self, request: Request):
        """
        handle the given request.
        :param request: a Request
        """
        print("===Verifying output")
        with open(request.output, mode='w', encoding='utf-8') as file:
            file.write(f"Timestamp: {datetime.now().strftime('%d-%m-%Y %H:%M')}\n"
                       f"Number of requests: {len(request.result)}\n")
            for output in request.result:
                if output is None:
                    file.write("An error occurred. Skipping this request.\n\n")
                    continue
                # print(type(output).__name__)
                file.write(str(output))

            print("Your file has been generated.")
