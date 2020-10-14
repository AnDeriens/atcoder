n, a, b = list(map(int, input().split()))

ans = 0

ans += a * (n // (a + b))

if n % (a + b) >= a:
    ans += a
else:
    ans += n % (a + b)

print(ans)
