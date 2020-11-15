n = int(input())
a = list(map(int, input().split()))
k = max(a)

ans = 0
max_gcd = 0

for _k in range(2, k + 1):
    gcd = 0
    for i in a:
        if i % _k == 0:
            gcd += 1

    if max_gcd <= gcd:
        ans = _k
        max_gcd = gcd

print(ans)
