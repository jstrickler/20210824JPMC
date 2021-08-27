d1 = dict()  # empty dict
d2 = {'a': 5, 'm': 18, 'b': 27, 'e': 99}
d3 = {}  # empty dict
print(d1)
print(d2)
print(d2['a'], d2['e'])
print(d3)

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}
print(airports['IAD'], airports['RDU'])
print(len(airports))

airports['IAH'] = "Houston International"
airports['HOU'] = "Houston Hobby"
print(airports)


