# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json


# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

    # TotalEvents = len(data['features'])
    TotalEvents = data['metadata']['count']
    print(f'Total Events: {TotalEvents}')

    def felt_greater_than_100(q):
        f = q['properties']['felt']
        return f is not None and f >= 100

    # TotalFelt = sum(
    #     quake['properties']['felt'] is not None and
    #     quake['properties']['felt'] >= 100
    #         for quake in data['features']
    # )
    TotalFelt = len(
        list(filter(
            felt_greater_than_100,
            data['features']
        ))
    )
    print(f'Total Felt: {TotalFelt}')
    
    def most_felt_event(q):
        felt_ct = q['properties']['felt']
        if felt_ct is not None:
            return felt_ct
        return 0

    MostFeltEvent = max(
        data['features'], key=most_felt_event
    )['properties']['title']
    print(f'Most Felt Event Name: {MostFeltEvent}')

    MostFeltCount = max(
        data['features'], key=most_felt_event
    )['properties']['felt']
    print(f'Most Felt Event Count: {MostFeltCount}')
    
    
    # apparently there was an extra exercise that isn't included in the challenge
    #   (seems to be this way since CoderPad appears to limit the amount of output)
    def signficance(q):
        sig = q['properties']['sig']
        if sig is not None:
            return sig
        return 0
    
    sorted_by_significance = sorted(
        data['features'],
        key=signficance,
        reverse=True
    )
    
    print(f'Top Ten Significant Events:')
    # TopTenSignificant = sorted_by_significance[:10]
    # print(f'There are {len(TopTenSignificant)} Significant events')
    # print(TopTenSignificant)
    # import pprint
    # pprint.pp(TopTenSignificant)
    for i in range(0, 10):
        print(
            f"Event: {sorted_by_significance[i]['properties']['title']} ; "
            f"Significance: {sorted_by_significance[i]['properties']['sig']}"
        )