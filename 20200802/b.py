# -*- coding: utf-8 -*-
import math

n, d = map(int, list(input().split()))

ans = 0

for i in range(n):
    x, y = map(int, list(input().split()))
    z = math.sqrt(x ** 2 + y ** 2)
    if z <= d:
        ans += 1
print(ans)
