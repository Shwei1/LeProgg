import math

def pi_gregori():
    S = 0
    n = 0
    a = 0
    e = 1/10 ** 8
    while True:
        n += 1
        a = (-1)**(n+1)/(2*n-1)
        S += a
        if abs(a) < e:
            break
    return 4 * S, n


def pi_wallice():
    P = 2
    n = 0
    e = 1 / 10 ** 8
    while True:
        n += 1
        a = (n+3)*2/(n+4)*2
        P = P * a
        if abs(a) < e:
            break
    return P

print(pi_wallice())



print(pi_gregori())



