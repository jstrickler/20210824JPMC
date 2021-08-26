fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear"]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0:", f0, '\n')

#    [expr for var in iterable]
f1 = [f.upper() for f in fruits]
print("f1:", f1, '\n')

f2 = [f[:3].title() for f in fruits]
print("f2:", f2, '\n')

f3 = [f.upper() for f in fruits if f.startswith('p')]
print("f3:", f3, '\n')

f4 = [f for f in fruits if f.startswith('p')]
print("f4:", f4, '\n')

nums = [800,80,1000,32,255,400,5,5000]
n1 = [float(n * 2) for n in nums if n > 300]
print("n1:", n1, '\n')

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
last_names = [p[1] for p in people]
print("last_names:", last_names, '\n')

youngsters = [p[1] for p in people if p[-1] > '1970']
print("youngsters:", youngsters, '\n')

info = [(p[1], p[-1]) for p in people if p[-1] > '1970']
print("info:", info, '\n')

g1 = (f.upper() for f in fruits)
print(g1)
for fruit in g1:
    print(fruit, end=' ')
print("\n")

g2 = (p[1] for p in people)
print(g2)
for last_name in g2:
    print(last_name, end=', ')
print()