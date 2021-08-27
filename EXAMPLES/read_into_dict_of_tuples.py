#!/usr/bin/env python
from pprint import pprint

knight_info = {}  # <1>

with open("../DATA/knights.txt") as knights_in:
    first_line = next(knights_in)  # read first line
    num_fields = len(first_line.split(':'))
    print("num_fields:", num_fields)
    knights_in.seek(0)  # rewind file
    for i, line in enumerate(knights_in):
        name, title, color, quest, comment = line.rstrip('\n\r').split(":")
        knight_info[i] = name, title, color, quest, comment  # <2>

pprint(knight_info)
print()

for num, info in knight_info.items():
    print(info[1], info[0])

print()
# print(knight_info['Robin'][2])
