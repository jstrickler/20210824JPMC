import sqlite3
import sys

file_name = "wombats.txt"

try:
    with open(file_name) as file_in:
        for line in file_in:
            print(line.rstrip())
except FileNotFoundError as err:
    print(err)

with open('DATA/breakfast.txt') as breakfast_in:
    foods = breakfast_in.read().splitlines()
try:
    print(foods[99])
except (IndexError, KeyError) as err:
    print(err)

number = 23
values = 5, 0, 14, 9, 7, "15"

for value in values:
    try:
        result = number / value
    except ZeroDivisionError as err:
        print(err)
    except TypeError as err:
        print(err)
    except Exception as err:
        print(err)
    else:
        print(result)

conn = None
try:
    conn = sqlite3('mydatabase.db')
except Exception as err:
    print(err)
    sys.exit()  # exit script
else:
    cur = conn.cursor()
    cur.execute('select spam from ham')
finally:
    if conn is not None:
        conn.close()
