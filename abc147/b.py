s = input()

ans = 0
i = 0
n = len(s)

while(i < n // 2):
    if s[i] != s[n - i - 1]:
        ans += 1
    i += 1

print(ans)
