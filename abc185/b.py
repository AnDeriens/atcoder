n, m, t = list(map(int, input().split()))

max_n = n
s = 0
for _ in range(m):
    a, b = list(map(int, input().split()))

    n -= a - s
    if n < 1:
        print('No')
        exit()

    n += b - a
    n = min(max_n, n)
    s = b

n -= t - s
if n < 1:
    print('No')
    exit()

print('Yes')
