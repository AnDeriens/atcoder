n, k = list(map(int, input().split()))

h = list(map(int, input().split()))

ans = 0
for _h in h:
    if _h >= k:
        ans += 1

print(ans)
