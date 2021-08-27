#!/usr/bin/env python

counts = {}  # <1>
with open("../DATA/breakfast.txt") as breakfast_in:
    for line in breakfast_in:
        breakfast_item = line.rstrip('\n\r')
        counts[breakfast_item] = counts.get(breakfast_item, 0) + 1   # <3>

for item, count in counts.items():
    print(item, count)
