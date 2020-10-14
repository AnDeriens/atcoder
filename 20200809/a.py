# -*- coding: utf-8 -*-

n = int(input())

ans = 0

nums = [''] * n
noInt = 0
noFloat = 0
for i in range(n):
    a = input()
    p_index = a.rfind('\.')
    print(a, p_index)
    if p_index == -1:
        noInt += 1
        nums[i] = a
    elif p_index < 5:
        noFloat += 1
        nums[i] = a
    elif a[p_index:].count('0') == len(a[p_index:]):
        noInt += 1
        nums[i] = a

ints = [''] * noInt
floats = [''] * noFloat

# 整数同士の組み合わせ
ans += len(ints) * (len(ints) + 1) / 2

print(noInt, noFloat)
