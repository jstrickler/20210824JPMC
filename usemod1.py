from john.math import geometry
import sys

print(geometry.circle_area(10))
print(geometry.rectangle_area(8, 9))
print(geometry.square_area(14))

# 1. current folder
# 2. folders in PYTHONPATH
# 3. builtin folders (sys.prefix)
print(sys.prefix)
print()
for path in sys.path:
    print(path)

