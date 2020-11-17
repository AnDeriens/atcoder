a, b = list(map(int, input().split()))

for x in range(1, 1300):
    if int(x * 0.08) == a and int(x * 0.1) == b:
        print(x)
        exit()

print(-1)
