fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear"]

print(len(fruits), min(fruits), max(fruits))
print(sorted(fruits))
print()

nums = [800,80,1000,32,255,400,5,5000]
print(sum(nums))






r = reversed(fruits)
print(fruits)
print(r)
print()
fruits.insert(0, "durian")

for fruit in r:
    print("fruit:", fruit)
print()
# print(len(r))

colors = ['red', 'blue', 'ecru', 'mauve', 'puce',
          'green', 'yellow', 'purple', 'black',
          'grey', 'white', 'pink']

combos = zip(fruits, colors)
print(combos)
print(len(fruits), len(colors))
for combo in combos:
    print(combo)
print()

for fruit, color in zip(fruits, colors):
    print(fruit, color)
print()

for i, fruit in enumerate(fruits):
    print(f"{i}. {fruit}")
print()

# S + S
# S * i

# range(stop) range(start, stop) range(start, stop, step)

r = range(10)
print(r)
for i in r:
    print(i)
print()

for i in range(1, 11):
    print(i, end=' ')
print()

for i in range(5, 101, 5):
    print(i, end=', ')
print()

REPEAT = 4
for i in range(REPEAT):
    print("Python rocks!")

nums = list(range(1, 26))
print(nums)
import random
nums = list(range(1, 101))
random.shuffle(nums)
print(nums)


