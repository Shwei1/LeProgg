k = int(input())
s = 0 # harmonic sequence
for i in range(1, k+1):
    s = s + 1/i
    print(f"S_{i} = {s}")


