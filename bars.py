import json
import os
import sys
FILE_DATA = 'data-2897-2016-11-23.json'


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r', encoding='cp1251') as file_handler:
        return json.load(file_handler)


def get_biggest_bar(data):
    return max(data, key=lambda bar: bar['SeatsCount'])


def get_smallest_bar(data):
    return min(data, key=lambda bar: bar['SeatsCount'])


def get_distance_to_bar(bar, longitude, latitude):
    longitude_bar = bar['geoData']['coordinates'][0]
    latitude_bar = bar['geoData']['coordinates'][1]
    return ((longitude_bar-longitude)**2 + (latitude_bar-latitude)**2)**0.5


def get_closest_bar(data, longitude, latitude):
    closest_bar = data[0]
    min_distance = get_distance_to_bar(data[0], longitude, latitude)
    for bar in data[1:]:
        distance = get_distance_to_bar(bar, longitude, latitude)
        if distance < min_distance:
            closest_bar = bar
            min_distance = distance
    return closest_bar


if __name__ == '__main__':
    data = load_data(FILE_DATA)
    try:
        longitude = float(input('Input your longitude: '))
        latitude = float(input('Input your latitude: '))
    except ValueError:
        print('Please input correct data')
        sys.exit(2)
    print(get_biggest_bar(data))
    print(get_smallest_bar(data))
    print(get_closest_bar(data, longitude, latitude))
