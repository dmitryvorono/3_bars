import json
import os
import sys
from pprint_json import pretty_print_json


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='cp1251') as file_handler:
        return json.load(file_handler)


def get_biggest_bar(bars):
    return max(bars, key=lambda bar: bar['SeatsCount'])


def get_smallest_bar(bars):
    return min(bars, key=lambda bar: bar['SeatsCount'])


def get_closest_bar(bars, longitude, latitude):
    def get_distance_to_bar(bar):
        longitude_bar = bar['geoData']['coordinates'][0]
        latitude_bar = bar['geoData']['coordinates'][1]
        return ((longitude_bar-longitude)**2 + (latitude_bar-latitude)**2)**0.5
    return min(bars, key=get_distance_to_bar)


if __name__ == '__main__':
    try:
        file_path = sys.argv[1]
        bars = load_data(file_path)
        if not bars:
            raise Exception('File not found: {0}'.format(file_path))
        longitude = float(input('Input your longitude: '))
        latitude = float(input('Input your latitude: '))
    except IndexError:
        print('Usage: python pprint_json.py <path to file>')
        sys.exit(2)
    except ValueError:
        print('Please input correct longitude and latitude')
        sys.exit(2)
    except Exception as e:
        print(e)
        sys.exit(2)
    pretty_print_json(get_biggest_bar(bars))
    pretty_print_json(get_smallest_bar(bars))
    pretty_print_json(get_closest_bar(bars, longitude, latitude))
