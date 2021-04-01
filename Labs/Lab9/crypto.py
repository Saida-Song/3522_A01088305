import des
import argparse
import abc
import enum
import ast


class CryptoMode(enum.Enum):
    """
    Lists the various modes that the Crypto application can run in.
    """
    # Encryption mode
    EN = "en"
    # Decryption Mode
    DE = "de"


class Request:
    """
    The request object represents a request to either encrypt or decrypt
    certain data. The request object comes with certain accompanying
    configuration options as well as a field that holds the result. The
    attributes are:
        - encryption_state: 'en' for encrypt, 'de' for decrypt
        - data_input: This is the string data that needs to be encrypted or
        decrypted. This is None if the data is coming in from a file.
        - input_file: The text file that contains the string to be encrypted or
        decrypted. This is None if the data is not coming from a file and is
        provided directly.
        - output: This is the method of output that is requested. At this
        moment the program supports printing to the console or writing to
        another text file.
        - key: The Key value to use for encryption or decryption.
        - result: Placeholder value to hold the result of the encryption or
        decryption. This does not usually come in with the request.

    """
    def __init__(self):
        self.encryption_state = None
        self.data_input = None
        self.input_file = None
        self.output = None
        self.key = None
        self.result = None

    def __str__(self):
        return f"Request: State: {self.encryption_state}, Data: {self.data_input}" \
               f", Input file: {self.input_file}, Output: {self.output}, " \
               f"Key: {self.key}"


def setup_request_commandline() -> Request:
    """
    Implements the argparse module to accept arguments via the command
    line. This function specifies what these arguments are and parses it
    into an object of type Request. If something goes wrong with
    provided arguments then the function prints an error message and
    exits the application.
    :return: The object of type Request with all the arguments provided
    in it.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("key", help="The key to use when encrypting or "
                                    "decrypting. This needs to be of "
                                    "length 8, 16 or 24")
    parser.add_argument("-s", "--string", help="The string that needs to be "
                                               "encrypted or decrypted")
    parser.add_argument("-f", "--file", help="The text file that needs to be"
                                             "encrypted or decrypted")
    parser.add_argument("-o", "--output", default="print",
                        help="The output of the program. This is 'print' by "
                             "default, but can be set to a file name as well.")
    parser.add_argument("-m", "--mode", default="en",
                        help="The mode to run the program in. If 'en' (default)"
                             " then the program will encrypt, 'de' will cause "
                             "the program to decrypt")
    try:
        args = parser.parse_args()
        request = Request()
        request.encryption_state = CryptoMode(args.mode)
        request.data_input = args.string
        request.input_file = args.file
        request.output = args.output
        request.key = args.key
        print(request)
        return request
    except Exception as e:
        print(f"Error! Could not read arguments.\n{e}")
        quit()


class Crypto:
    """
    The class represents the crypto class that will encrypt or decrypt based on the given command line
    argument.
    """

    def __init__(self):
        self.start_handler = None

    def execute_request(self, given_request: Request):
        """
        Execute the handlers to deal with the request.
        :param given_request: a Request
        :return: True if successfully encrypted or decrypted.
        """
        last_handler = None
        if given_request.output != "print":
            last_handler = WriteToFileHandler()
        if given_request.encryption_state == CryptoMode.EN:
            self.start_handler = EncryptDataHandler()
        elif given_request.encryption_state == CryptoMode.DE:
            self.start_handler = DecryptDataHandler()
        else:
            print("Wrong Crypto Mode")
            return False
        self.start_handler.next_handler = last_handler
        if given_request.input_file:
            buffer_handler = self.start_handler
            self.start_handler = ReadDataFromFileHandler()
            self.start_handler.next_handler = buffer_handler
        return self.start_handler.handle_request(given_request)


class BaseRequestHandler(abc.ABC):
    """
    Parent class of all Handlers.
    """

    def __init__(self):
        self.next_handler = None

    @abc.abstractmethod
    def handle_request(self, given_request: Request):
        """
        Handle the request.
        :param given_request: a Request
        """
        pass

    def set_handler(self, handler):
        """
        Set the next handler.
        :param handler: a Handler
        """
        self.next_handler = handler


class ReadDataFromFileHandler(BaseRequestHandler):
    """
    A handler that read data from a given file.
    """
    def handle_request(self, given_request: Request):
        """
        Read data from a given file and hand it over to next handler.
        :param given_request: a Request
        :return: false if Exception occurs
        """
        try:
            with open(given_request.input_file, mode='r', encoding='utf-8') as file:
                content = ''.join(file)
                if not self.next_handler:
                    print(content)
                    return True
                given_request.result = content
                return self.next_handler.handle_request(given_request)
        except FileNotFoundError as e:
            print(e)
            return False


class EncryptDataHandler(BaseRequestHandler):
    """
    A handler that encrypt the given message to byte string.
    """
    def handle_request(self, given_request: Request):
        """
        Encrypt the message of the request to a byte string.
        :param given_request: a Request
        """
        key = des.DesKey(given_request.key.encode('utf-8'))
        if not request.data_input:
            en_message = key.encrypt(given_request.result.encode('utf-8'), padding=True)
        else:
            en_message = key.encrypt(given_request.data_input.encode('utf-8'), padding=True)
        if not self.next_handler:
            print(en_message)
            return True
        given_request.result = en_message
        return self.next_handler.handle_request(given_request)


class DecryptDataHandler(BaseRequestHandler):
    """
    A handler that decrypt the given message to a string
    """
    def handle_request(self, given_request: Request):
        """
        Decrypt the message of given request to a string.
        :param given_request: a Request
        """
        key = des.DesKey(request.key.encode('utf-8'))
        if not request.data_input:
            de_message = key.decrypt(ast.literal_eval(given_request.result), padding=True)
        else:
            de_message = key.decrypt(ast.literal_eval(given_request.data_input), padding=True)
        original_message = de_message.decode('utf-8')
        if not self.next_handler:
            print(original_message)
            return True
        given_request.result = original_message
        return self.next_handler.handle_request(given_request)


class WriteToFileHandler(BaseRequestHandler):
    """
    A handler that write the encrypted or decrypted message to a file
    """
    def handle_request(self, given_request: Request):
        """
        Write the encrypted or decrypted message to a file.
        :param given_request: a Request
        """
        with open(request.output, mode="w", encoding='utf-8') as file:
            file.write(request.result)
            return True


def main(given_request: Request):
    crypto = Crypto()
    crypto.execute_request(given_request)


if __name__ == '__main__':
    request = setup_request_commandline()
    main(request)
