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
airports['IAH'] = "George Bush International"

counts = {}
counts['a'] = 0
counts['a'] += 1
counts['a'] += 1
print(counts, counts['a'])

for code in 'IAH', 'RDU', 'LAX', 'LON', 'LUT', 'EWR':
    # if code in airports:
    #     print(airports[code])
    # else:
    #     print("NOT FOUND")
    print(airports.get(code, "NOT FOUND"))

print(airports)
print()
print(airports.setdefault('ELM', 'Elmira-Corning'))
print(airports)

print(airports.items(), '\n')
for code, airport in sorted(airports.items()):
    print(code, airport)
print()

def by_value(element):
    return element[1], element[0]

for code, airport in sorted(airports.items(), key=by_value):
    print(code, airport)

