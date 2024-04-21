declare = [1, 2, 3, "*", 5, 6, 7, "*", 1337, 1488]

result = []
temp = []

for i in declare:
    if i != "*":
        temp.append(i)
    else:
        result.append(temp[:])
        temp.clear()
        continue
result.append(temp)
    # if temp:
    #     result.append(temp)

print(result)

lst = []
print(bool(lst))