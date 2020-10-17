x, y, a, b = list(map(int, input().split()))

ans = 0

while(x * a <= x + b and x * a < y):
    x *= a
    ans += 1

ans += (y - x - 1) // b

print(ans)
