import math

x = 2


def sqrt(x):
    xn = x / 2
    n = 1
    while True:
        n += 1
        yn = xn
        xn = 0.5 * (xn + x / xn)
        if abs(xn - yn) < 0.000000000001:
            break
    return xn


print(math.sqrt(x))
print(sqrt(x))
