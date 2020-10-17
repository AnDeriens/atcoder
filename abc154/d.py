n , k = list(map(int, input().split()))
p = [0] + list(map(int, input().split()))

s = [0] * (n + 1)

for i in range(1, n + 1):
    s[i] = s[i - 1] + (p[i] + 1) / 2

ans = 0

for j in range(1, n - k + 2): # 開始地点
    x = s[j + k - 1] - s[j - 1]
    ans = max(x, ans)

print(ans)
