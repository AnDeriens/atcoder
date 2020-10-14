n,m,x = list(map(int, input().split()))

c = [0] * (n + 1)
a = [[]] * (n + 1)

for i in range(n):
    l = list(map(int, input().split()))

    c[i + 1] = l.pop(0)
    a[i + 1] = l

al = [0] * (n + 1)
for i in range(1, n + 1):
    for j in range(m):
        al[j + 1] += a[i][j]


