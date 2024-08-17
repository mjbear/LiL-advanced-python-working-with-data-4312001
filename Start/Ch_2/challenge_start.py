# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
from collections import defaultdict


# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

    # categorize each event and count each one
    type_count = defaultdict(int)
    for event in data['features']:
        type_count[event['properties']['type']] += 1

    # return the result
    print(type_count)
    print()
    print(dict(type_count))

    print()
    for k, v in type_count.items():
        print(f'{k:15}: {v}')