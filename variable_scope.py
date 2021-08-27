search_term = 'drink'  # global variable

def find_word(word, *filenames):
    lines = []  # local variable -- only visible in function
    for filename in filenames:
        with open(filename) as file_in:
            for line in file_in:
                if word in line:
                    lines.append(line.rstrip())
    return lines

lines = find_word(search_term, 'DATA/alice.txt')
print(lines)
