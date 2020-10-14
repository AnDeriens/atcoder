n, k = list(map(int, input().split()))

ans = ''

for i in range(100):
    r = n % k
    ans = str(r) + ans

    if n < k:
        break

    n = int(n / k)


print(len(ans))
