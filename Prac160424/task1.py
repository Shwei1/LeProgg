import math

x = math.pi / 6


def sin(x):
    S = x
    a = x
    n = 0
    while True:
        n += 1
        a = - a * x ** 2 / (2 * n * (2*n + 1))
        S = S+a
        if abs(a) < 0.0000000000001:
            break

    return S

print(f"math.sin: {math.sin(x)}")
print(f"my.sin: {sin(x)}")







