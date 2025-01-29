from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
import math

sum = 0
h = (math.pi / 2) / 100

for i in range(100):
    sum += (sin(i * h) + sin((i + 1) * h))

print((h / 2) * sum)
