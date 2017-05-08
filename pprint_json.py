import json
import sys
import os


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def pretty_print_json(data):
    print(json.dumps(data, sort_keys=True, indent=4))


if __name__ == '__main__':
    try:
        file_name = sys.argv[1]
    except IndexError:
        print('Usage: python pprint_json.py <path to file>')
        sys.exit(2)
    pretty_print_json(load_data(file_name))
