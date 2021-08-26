
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