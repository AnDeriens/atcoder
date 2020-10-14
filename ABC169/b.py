# -*- coding: utf-8 -*-

n = int(input())

nums = sorted(list(map(int, input().split())))

ans = 1
for i in range(n):
    ans *= nums[i]

    if ans == 0:
        print(0)
        exit()

    if ans > 10 ** 18:
        print(-1)
        exit()

print(ans)
