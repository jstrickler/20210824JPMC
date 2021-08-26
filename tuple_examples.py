
person = 'Bill', 'Gates', 'Microsoft', '1955-10-24'

print(type(person), person, '\n')

x = 'Fred', 'Smith', 24, 89.7, 'Idaho'

print(person[0], person[1])

#  v1, v2, v3, ... = I   (iterable)
#  v1 = I[0]
#  v2 = I[1]
# ...
first_name, last_name, product, dob = person
print(first_name, last_name)
print()

a, b, c, _ = person
print(a, b, c)
a, b, *c = person
print(a, b, c)

a, *b, c = person
print(a, b, c)

*a, b, c = person
print(a, b, c)

# next up: unpack in loop


people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]
m = people[0]
first_name, last_name, product, dob = people[0]
print(first_name)

for first_name, last_name, *_ in people: #  product, dob in people:
    # first_name, last_name, product, dob = <next element of people>
    print(first_name, last_name)
print()

a = 23
b = 6
r = divmod(a, b)
print(r)
quotient, remainder = divmod(a, b)

days_old = 23093
years, days = divmod(days_old, 365)
print(years, days)









