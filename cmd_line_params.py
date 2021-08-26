import sys

print(sys.argv)
print(sys.argv[0])  # always script name
print(sys.argv[1])  # 1st "real" param
print(len(sys.argv))

if len(sys.argv) > 1:
    value = sys.argv[1]
else:
    print("Please put a value on the command line")
