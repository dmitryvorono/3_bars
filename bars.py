import json
import os
import sys
import pprint


def load_data(filepath):
    if not os.path.exists(filepath):
        sys.exit('File does not exists: {0}'.format(filepath))
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


def print_bar_information(feature, bar):
    print(feature)
    pprint.pprint(bar, indent=4)


if __name__ == '__main__':
    try:
        file_path = sys.argv[1]
        bars = load_data(file_path)
        longitude = float(input('Input your longitude: '))
        latitude = float(input('Input your latitude: '))
    except IndexError:
        sys.exit('Usage: python pprint_json.py <path to file>')
    except ValueError:
        sys.exit('Please input correct longitude and latitude')
    print_bar_information('Самый большой бар:', get_biggest_bar(bars))
    print_bar_information('Самый маленький бар:', get_smallest_bar(bars))
    print_bar_information('Ближайший бар:', get_closest_bar(bars, longitude, latitude))
