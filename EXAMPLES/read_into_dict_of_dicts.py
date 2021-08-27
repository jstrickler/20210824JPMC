#!/usr/bin/env python
from pprint import pprint
knight_info = {}

with open("../DATA/knights.txt") as knights_in:
    for line in knights_in:
        name, title, color, quest, comment = line.rstrip('\n\r').split(":")
        knight_info[name] = {
            'title': title,
            'color': color,
            'quest': quest,
            'comment': comment,
        }

for name, info in knight_info.items():
    print("{} {}".format(info['title'], name))
print()

pprint(knight_info)
