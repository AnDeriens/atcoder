n = int(input())
d = [0] + list(map(int, input().split()))

s = [0] * (n + 1)

for i in range(1, n + 1):
    s[i] = d[i] + s[i - 1]

ans = 0

for j in range(1, n):
    ans += d[j] * (s[n] - s[j])

print(ans)
