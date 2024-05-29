import time
from typing import Dict, Any, Tuple, Optional
from utilities import human_readable_size


class DirectoryHandler:
    """
    Class to handle directory operations.
    """

    @staticmethod
    def format_time(epoch_time: float) -> str:
        """
        Format epoch time into human-readable time string.

        epoch_time: The epoch time to be formatted.
        """
        return time.strftime("%b %d %H:%M", time.localtime(epoch_time))

    @staticmethod
    def list_directory(data: Dict[str, Any], show_all: bool, long_format: bool, reverse: bool,
                       sort_time: bool, filter_type: str, is_single_file: bool = False) -> None:
        """
        List directory contents with various formatting options.

        data: Directory data containing contents information.
        show_all: Flag to show hidden files/directories.
        long_format: Flag to show detailed information.
        reverse: Flag to reverse the sorting order.
        sort_time: Flag to sort by time modified.
        filter_type: Type of content to filter (file/directory).
        is_single_file: Flag to indicate single file mode. Defaults to False.
        """
        contents = data.get('contents', [])

        if is_single_file:
            contents = [data]
        elif not show_all:
            contents = [item for item in contents if not item['name'].startswith('.')]

        if filter_type:
            if filter_type == 'file':
                contents = [item for item in contents if 'contents' not in item]
            elif filter_type == 'dir':
                contents = [item for item in contents if 'contents' in item]

        if sort_time:
            contents.sort(key=lambda x: x['time_modified'], reverse=reverse)
        elif reverse:
            contents.reverse()

        for item in contents:
            if long_format:
                size = human_readable_size(item['size'])
                print(f"{item['permissions']} {size} "
                      f"{DirectoryHandler.format_time(item['time_modified'])} {item['name']}")
            else:
                print(item['name'])

    @staticmethod
    def find_path(data: Dict[str, Any], path: str) -> Tuple[Optional[Dict[str, Any]], bool]:
        """
        Find a path within the directory structure.

        data: Directory data to search within.
        path: Path to search for.
        """
        if not path or path == ".":
            return data, False
        parts = path.split('/')
        for part in parts:
            found = False
            for item in data.get('contents', []):
                if item['name'] == part:
                    data = item
                    found = True
                    break
            if not found:
                return None, False
        return data, 'contents' not in data
