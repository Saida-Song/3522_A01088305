import argparse


class Request:
    """
    Represent a Request generated from the command line argument.
    """

    def __init__(self):
        """
        Represent a new request.
        """
        self.mode = None
        self.input_file = None
        self.input_data = None
        self.expanded = None
        self.output = None
        self.result = None

    def __str__(self):
        """
        A str representation of a request.
        :return: str
        """
        return f"Request: Mode: {self.mode}, Input file: {self.input_file}" \
               f", Input data: {self.input_data}, Expanded: {self.expanded}" \
               f", Output: {self.output}"


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
    parser.add_argument("mode", help="A positional argument. "
                                     "Choose one of pokemon | ability | move ")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--inputfile",
                       help="A group of mutually exclusive argument. "
                            "This takes a file name (only .txt is accepted)")
    group.add_argument("--inputdata",
                       help="A group of mutually exclusive argument "
                            "This takes a name(string) or an id(int)")
    parser.add_argument("--expanded", action='store_true',
                        help="An optional flag. This supports only pokemon queries. "
                             "This provides more information "
                             "(stats | abilities | moves)")
    parser.add_argument("--output",
                        help="The output of the program. This is 'print' by "
                             "default, but can be set to a file name as well.")

    try:
        args = parser.parse_args()
        req = Request()
        req.mode = args.mode.lower()
        req.input_file = args.inputfile
        req.input_data = args.inputdata
        req.expanded = args.expanded
        req.output = args.output
        print(req)
        return req
    except Exception as e:
        print(f"Error! Could not read arguments.\n{e}")
        quit()