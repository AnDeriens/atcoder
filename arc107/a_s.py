a, b, c = list(map(int, input().split()))

x = 0

for _a in range(1, a + 1):
    for _b in range(1, b + 1):
        for _c in range(1, c + 1):
            x += _a * _b * _c

print(x)
