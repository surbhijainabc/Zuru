from argument_parser import ArgumentParser
from file_handler import FileHandler
from directory_handler import DirectoryHandler


def main() -> None:
    arg_parser = ArgumentParser()
    args = arg_parser.parse_args()

    data = FileHandler.read_json_file('../structure.json')

    if args.filter and args.filter not in ['file', 'dir']:
        print(f"error: '{args.filter}' is not a valid filter criteria. Available filters are 'file' and 'dir'")
        return

    if args.path:
        target_data, is_single_file = DirectoryHandler.find_path(data, args.path)
        if target_data is None:
            print(f"error: cannot access '{args.path}': No such file or directory")
            return
    else:
        target_data, is_single_file = data, False

    if target_data:
        DirectoryHandler.list_directory(target_data, args.A, args.l, args.r, args.t, args.filter, is_single_file)


if __name__ == "__main__":
    main()
