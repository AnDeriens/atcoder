def gcd(n, m):
    if n < m:
        n, m = m, n
    i = 1
    while n % m != 0:
        n, m = m, n % m
        print(i, n, m)
        i += 1

    return m

ans = gcd(200, 144)

print(ans)
