# -*- coding: utf-8 -*-

n = int(input())

strs = [''] * n

ans = 0

for i in range(n):
    strs[i] = input()

for i in range(n):
    for j in range(i + 1, n):
        a = strs[i]
        b = strs[j]

        if len(b) > len(a):
            a, b = b, a

        if len(b) == 1:
            if b in a:
                ans += 1
            continue
        else:
            b_1 = b[0:1]
            b_2 = b[1:]
            a_2 = a[-1 * len(b_2):]
            a_1 = a[:-1 * len(b_2)]

            if a_2 == b_2 and b_1 in a_1:
                ans += 1

print(ans)
