n, k, m = list(map(int, input().split()))
a = list(map(int, input().split()))

s = sum(a)

x = n * m - s

if x > k:
    print(-1)
elif x < 0:
    print(0)
else:
    print(x)
