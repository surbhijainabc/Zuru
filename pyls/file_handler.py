import json
from typing import Any, Dict


class FileHandler:
    """
    Class to handle file operations.
    """
    @staticmethod
    def read_json_file(file_path) -> Dict[str, Any]:
        """
        Read JSON data from a file.

        file_path: Path to the JSON file to read.
        """
        with open(file_path, 'r') as file:
            return json.load(file)
