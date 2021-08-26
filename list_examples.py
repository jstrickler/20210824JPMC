list1 = list()
list2 = ['a', 'b', 'c']
list3 = []
print(list1, list2, list3)
print(len(list1), len(list2), len(list3))

cities = ['Plano', 'Columbus', 'Durham']
print(cities)
cities.append('Houston')
print(cities)
cities.insert(0, 'Wilmington')
print(cities)
cities.insert(3, 'Albany')
print(cities)
more_cities = ['Bournemouth', 'Chicago', 'NYC']
cities.extend(more_cities)
print(cities)

#  cities.append(obj)
#  cities.insert(pos, obj)
#  cities.extend(iterable)
cities[0] = "Wilmington DE"
print(cities)

del cities[3]
print(cities)

cities.remove('Chicago')
print(cities)

city = cities.pop()
print(city, cities)

city = cities.pop(2)
print(city, cities)

#  del L[pos]
#  L.pop(pos)
#  L.remove(value)

print(cities.index('Durham'))
# print(cities.index('Hoboken'))

print(cities)
print(cities[0])
print(cities[3])
print(cities[-1])  # cities[len(cities) - 1]
print(cities[-2])

#  LIST[START:STOP]
print(cities[0:3])
print(cities[2:4])

actor = "Chris Hemsworth"
print(actor[:5])
print(actor[3:5])
print(actor[-5:])

print(cities)
print()
for city in cities:
    # city = <next element of cities>
    print(city)

print("printing x")
x = []
for value in x:
    print(value)
