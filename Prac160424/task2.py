import math


def cos(x):
    S = 1
    a = 1
    epsilon = 1 / 10 ** 10
    n = 0
    while True:
        n += 1
        a = a * (- x ** 2 / (2 * n * (2 * n - 1)))
        S += a
        if abs(a) < epsilon:
            break
    return S


x = math.pi / 3
print(cos(x))
print(math.cos(x))