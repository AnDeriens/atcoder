a, b, n = list(map(int, input().split()))

lim = min(b - 1, n)

x = int(a * lim / b)

print(x)
