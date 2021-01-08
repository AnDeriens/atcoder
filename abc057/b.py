n, m = list(map(int, input().split()))

gakusei = [[0, 0] for _ in range(n)]
checkpoint = [[0, 0] for _ in range(m)]

for i in range(n):
    gakusei[i] = list(map(int, input().split()))

for j in range(m):
    checkpoint[j] = list(map(int, input().split()))

for g in gakusei:
    goal = -1
    minkyori = (10 ** 8) * 4 + 10
    for k in range(m):
        p = checkpoint[k]
        kyori = abs(g[0] - p[0]) + abs(g[1] - p[1])
        if kyori < minkyori:
            goal = k + 1
            minkyori = kyori

    print(goal)

