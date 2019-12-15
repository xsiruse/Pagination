import csv
from pprint import pprint

from app import settings


def get_data(file):
    with open(file, encoding='cp1251', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
    dict_list = []
    for line in reader:
        dict_list.append(line)

    print(dict_list)
    return dict_list



get_data(settings.BUS_STATION_CSV)
