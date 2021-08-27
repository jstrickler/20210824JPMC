letters1 = ['m', 'a', 'c', 'b', 'e', 't', 'h']
letters2 = ['h', 'a', 'm', 'l', 'e', 't']

s1 = set(letters1)   # set('macbeth')
s2 = set(letters2)    # set('hamlet')

print("Common:", s1 & s2)  # intersection
print("Not common:", s1 ^ s2)  # xor
print("All:", s1 | s2)  # union

s3 = set("mississippi")
print(s3)

s4 = set()
s4.add('beef')
s4.add('tofu')
s4.add('beef')
s4.add('lamb')
s4.add('seitan')
s4.add('tofu')
print(s4)

print("s1 only:", s1 - s2)
print("s2 only:", s2 - s1)


