# -*- coding: utf-8 -*-

n = int(input())
nums = list(map(int, input().split()))
x = 10 ** 9 + 7

ans = 0

sums = [0] * (n - 1)

for j in range(n - 1):
    if j == 0:
        sums[0] = nums[0] % x
    else:
        sums[j] = (sums[j - 1] + nums[j]) % x

for i in range(1, len(nums)):
    ans += sums[i - 1] * nums[i]
    ans = ans % x

print(ans)
