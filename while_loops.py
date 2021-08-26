
i = 0
while i < 3:
    print(i)
    i += 1
print()

while True:
    user_name = input("What is your name? ")
    if user_name == 'q':
        break  # exit loop
    if user_name == '':
        continue   # go back to top
    print("Welcome,", user_name)

