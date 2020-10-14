# -*- coding: utf-8 -*-

n = int(input())

ls = list(map(int, input().split()))

ans = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            a = ls[i]
            b = ls[j]
            c = ls[k]

            nums = [a,b,c]
            nums.sort()

            maxi = nums[2]
            mid = nums[1]
            mini = nums[0]

            if maxi < mid + mini and maxi != mid and mid != mini:
                ans += 1

print(ans)

