from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
import math

sum = 0
a = 0
b = math.pi / 2
n = 100
h = (b - a) / n

for i in range(n):
    sum += (sin(a + i * h) + sin(a + (i + 1) * h))

print((h / 2) * sum)
