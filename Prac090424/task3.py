def gen(n, x):
    a = x
    yield a
    for k in range(1, n+1):
        a = -x ** 2 / (2 * k * (2 * k + 1)) * a
        yield a


N = int(input("N = "))
x = float(input("x = "))

# for a in gen(N, x):
#     print(a, end = ' ')