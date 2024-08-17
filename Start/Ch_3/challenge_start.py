# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
import csv
import datetime


# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# Create a CSV file with the following information:
# 40 most significant seismic events, ordered by most recent
# Header row: Magnitude, Place, Felt Reports, Date, and Google Map link
# Date should be in the format of YYYY-MM-DD
header = ['Magnitude', 'Place', 'Felt Reports', 'Date', 'Link']
rows = []

def significance(q):
    sig = q['properties']['sig']
    # if sig is not None:
    #     return sig
    # return 0
    return 0 if sig is None else sig

data['features'].sort(key=significance, reverse=True)
significant = data['features'][:40]

# def time(q):
#     time = q['properties']['time']
#     return 0 if time is None else time
# 
# significant.sort(key=time, reverse=True)
# or use a lambda function
significant.sort(key=lambda t: t['properties']['time'], reverse=True)

for quake in significant:
    thedate = datetime.date.fromtimestamp(
        int(quake['properties']['time']/1000)
    )

    # https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php
    # geometry > coordinates > [long, lat, depth]
    lat = quake['geometry']['coordinates'][1]
    long = quake['geometry']['coordinates'][0]
    # https://developers.google.com/maps/documentation/urls/get-started#search-action
    gmap_link = (
        f"https://maps.google.com/maps/search/?api=1&query={lat},{long}"
    )

    rows.append([
        quake['properties']['mag'],
        quake['properties']['place'],
        (
            0 if quake['properties']['felt'] is None
            else quake['properties']['felt']
        ),
        thedate,
        gmap_link,
    ])

with open('significant_events.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(header)
    writer.writerows(rows)