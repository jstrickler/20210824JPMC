def get_message():
    return "Hello, JPMC world"

m = get_message()
print(m)
print(get_message())
print(get_message)

def mom():
    print("Hi, Mom!")

mom()
mom()
print(mom())

def greet(whom):
    print("Hello,", whom)

greet('world')
greet('Sailor')
greet('Sinbad')

person = "Bill Gates"
greet(person)

def find_word(word, *filenames):
    lines = []
    for filename in filenames:
        with open(filename) as file_in:
            for line in file_in:
                if word in line:
                    lines.append(line.rstrip())
    return lines

print(find_word('pig', 'DATA/alice.txt'))
print(find_word('bird', 'DATA/parrot.txt'))
search_term = 'Lizard'
file_name = 'DATA/alice.txt'
lines = find_word(search_term, file_name)
print(lines)
lines = find_word('bird', 'DATA/alice.txt', 'DATA/parrot.txt',
                  'DATA/words.txt')

print(lines)


