import argparse


class ArgumentParser:
    """
    ArgumentParser for pyls utility.
    """

    def __init__(self) -> None:
        """
        Initialize the ArgumentParser.
        """
        self.parser = argparse.ArgumentParser(description="pyls - List directory contents")
        self.add_arguments()

    def add_arguments(self) -> None:
        """
        Add arguments to the parser.
        """
        self.parser.add_argument('-A', action='store_true', help="Include entries which start with .")
        self.parser.add_argument('-l', action='store_true', help="Use a long listing format")
        self.parser.add_argument('-r', action='store_true', help="Reverse order while sorting")
        self.parser.add_argument('-t', action='store_true', help="Sort by time modified")
        self.parser.add_argument('--filter', help="Filter results to show only files or directories")
        self.parser.add_argument('path', nargs='?', default=None,
                                 help="Path to the directory or file within the JSON structure")

    def parse_args(self) -> argparse.Namespace:
        """
        Parse command line arguments.
        """
        return self.parser.parse_args()
