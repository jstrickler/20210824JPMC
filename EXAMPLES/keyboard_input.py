#!/usr/bin/env python

name = input("What is your name: ")
quest = input("What is your quest? ")
print(name, "seeks", quest)

raw_num = input("Enter number: ")  # <1>
num = int(raw_num)  # <2>

print("2 times", num, "is ", 2 * num)

raw_input = input("Enter something: ")
print(f"input was >{raw_input}<")
#  print("input was >{}<".format(raw_input))