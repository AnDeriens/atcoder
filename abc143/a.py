a, b = list(map(int, input().split()))

ans = a - 2 * b
if ans < 0:
    print(0)
else:
    print(ans)
