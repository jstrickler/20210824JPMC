# don't care:
#  bool  complex

# do care:
#  int float

# int  unlimited precision
# float long double (15-16 digits of precision)

i1 = 1000
i2 = 0b1000
i3 = 0x1000
i4 = 0o1000

# 0523 invalid!
print(i1, i2, i3, i4)
i5 = 283502936720938620396820396820369820968203968209862098602986
i6 = 23_435_930
# i6 = 23435930
i7 = 12_34_77_30930902_92
print()

a = 19
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)  # floored div -- round *down* to nearest whole number
print(a ** b)  # raise to power
print(a % b)   # remainder (modulo)

# invalid:
#  x++ ++x x-- --x

x = 0
x = x + 1
x += 1    # same as previous
# += -= *= /= //= **= %=
#  P E M D A S
#  ()
print(a, b, divmod(a, b))

# convert anything
# str(x)  bool(x)

# convert number OR string that *looks like* number to number
# int(x) float(x)

j = "123"
k = 456
print(int(j) + k)
print(j + str(k))

# str() -> human friendly
# repr() -> how to create object




