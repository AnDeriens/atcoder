import math

n = int(input())

l = [0] * 1001

def cnt_factorialize(m):
    cnt = 0
    for i in range(1, math.ceil((m + 1) ** 0.5)):
        if m % i == 0:
            cnt += 1

    cnt *= 2

    if m / i == i:
        cnt -= 1

    return cnt

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3

    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2

    if n != 1:
        a.append(n)

    return a


for x in range(1, 1001):
    l[x] = cnt_factorialize(x)

ans = 0

for c in range(1, n):
    a = prime_factorize(c)
    cnt = 1

    for h in a:
        cnt *= l[h]

    ans += cnt

print(cnt)
