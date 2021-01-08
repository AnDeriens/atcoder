a, b, c = list(map(int, input().split()))

ans = 0
s = a + b + c

for i in range(100 - max(a,b,c), 300 - (a + b + c + 1)):
    ans += a / s + b / s + c / s
    s += 1

    print(i, ans)

print(ans)
