a = 123
wizard_percentage = 47.23902903
person = "Gandalf"

SEP = " "
END = "\n"
print(a, wizard_percentage, person)
print(str(a) + SEP + str(wizard_percentage) + SEP + str(person) + END)

print(a)
print(str(a) + END)

print()
print(END)

print(a, wizard_percentage, person, sep='/')
print(a, wizard_percentage, person, sep=" and ")
print(a, wizard_percentage, person, sep='')

print(a)
print(wizard_percentage)
print()
print(a, end=' ')
# if ...
print(wizard_percentage)

print(person, "is", wizard_percentage, "% wizard")
print(person, " is ", wizard_percentage, "% wizard", sep="")

print("{} is {}% wizard".format(person, wizard_percentage))
print("{} is {:.2f}% wizard".format(person, wizard_percentage))
print(f"{person} is {wizard_percentage:.2f}% wizard")

