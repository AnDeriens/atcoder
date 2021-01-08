n = int(input())
b = [0] + list(map(int, input().split()))

ans = b[1]
for i in range(2, n):
    ans += min(b[i - 1], b[i])    

ans += b[n - 1]

print(ans)
