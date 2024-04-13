# n = int(input("n = "))
s = 1
k = int(input())
i = 2
while s <= k:
    s += 1/i
    i += 1
    if s >= k:
        break

print(i)

