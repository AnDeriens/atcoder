n = int(input())

dots = [[0, 0] for _ in range(n)]

for a in range(n):
    x, y = list(map(int, input().split()))
    dots[a][0] = x
    dots[a][1] = y

ans = 0
for i in range(n):
    for j in range(i, n):
        if dots[j][0] - dots[i][0] == 0:
            continue

        t = (dots[j][1] - dots[i][1]) / (dots[j][0] - dots[i][0])
        if t >= -1 and t <= 1:
            ans += 1

print(ans)
