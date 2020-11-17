n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

ans = 0

for i in range(n):
    diff = p[n - i - 1] - q[n - i - 1]
    print(diff)
    if diff > 0:
        ans += (n - 1) ** i * abs(diff)
    elif diff < 0:
        ans -= (n - 1) ** i * abs(diff)

print(abs(ans))
