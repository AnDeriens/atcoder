h, w = list(map(int, input().split()))

ans = 0
x = [[0] * w] * h
a_min = 100
for _ in range(h):
    a = list(map(int, input().split()))
    a_min = min(a_min, min(a))
    x[_] = a

for i in range(h):
    for j in range(w):
        ans += x[i][j] - a_min

print(ans)
