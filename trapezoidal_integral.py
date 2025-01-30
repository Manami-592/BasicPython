from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------

import math
def function(f, a = 0, b = 1, n = 100):

    sum = 0
    h = (b - a) / n

    for i in range(n):
        sum += (f(a + i * h) + f(a + (i + 1) * h))

    return((h / 2) * sum)


def func2(x):
    return 4 / (1 + x**2)


def func3(x):
    return math.pi**0.5 * math.exp(-x**2)


print(function(sin, 0, math.pi / 2, 50))
print(function(func2, 0, 1, 500))
print(function(func3, -100, 100, 1000))
