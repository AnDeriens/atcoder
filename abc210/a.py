n, a, x, y = list(map(int, input().split()))

if n > a:
    print(a * x + y * (n - a))
else:
    print(x * n)
