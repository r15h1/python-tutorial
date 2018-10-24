# Math Module Part I

import math

# Constants
print(math.pi)
print(math.e)

print(math.nan)
print(math.inf)
print(-math.inf)

# Trigonometry
obst_direction = math.cos(math.pi / 4)
print(obst_direction)
print(math.sin(math.pi / 4))

# Ceiling and Floor
cookies = 10.3
candy = 7
print(math.ceil(cookies))
print(math.ceil(candy))

age = 47.9
otherAge = 47
print(math.floor(age))
print(math.floor(otherAge))

# Factorial & Square Root
print(math.factorial(3))
print(math.sqrt(64))

# Greatest Common Denominator GCD
print(math.gcd(52, 8))
print(math.gcd(8, 52))

print(8/52)
print(2/13)

# Degrees and Radians
print(math.radians(360))
print(math.pi * 2)
print(math.degrees(math.pi * 2))