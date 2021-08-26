FILE_PATH = "DATA/mary.txt"

file_obj = open(FILE_PATH)
file_obj.close()

mary_in = open(FILE_PATH)
mary_in.close()

#  mary_in = open(FILE_PATH)
with open(FILE_PATH) as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()  # trim \n or \r
        print(line)
print("-" * 60)

with open('DATA/alice.txt') as alice_in:
    for raw_line in alice_in:
        if 'Lizard' in raw_line:
            line = raw_line.rstrip()
            print(line)
print("-" * 60)

with open(FILE_PATH) as mary_in:
    contents = mary_in.read()
    print("raw:", repr(contents))
    print()
    print("normal:", contents)
print("-" * 60)

with open(FILE_PATH) as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)
print("-" * 60)

with open(FILE_PATH) as mary_in:
    all_lines_without_nl = mary_in.read().splitlines()
    print(all_lines_without_nl)
print("-" * 60)

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date"]

with open('fruits.txt', 'w') as fruits_out:
    for fruit in fruits:
        fruits_out.write(fruit + '\n')

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

with open('computer_people.txt', 'w') as cp_out:
    for person in people:
        record = '|'.join(person)
        cp_out.write(record + '\n')


with open('DATA/words.txt') as words_in:
    with open('zwords.txt', 'w') as zwords_out:
        for raw_line in words_in:
            line = raw_line.rstrip()
            if line.endswith('z'):
                zwords_out.write(raw_line)

