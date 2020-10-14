# -*- coding: utf-8 -*-

s = input().split(' ')

h = int(s[0])
w = int(s[1])
k = int(s[2])

r = [list(input()) for i in range(h)]

def ex(values, x, y, k):
    cnt = 0
    for i, vs in enumerate(values):
        for j, v in enumerate(vs):
            if i != x and j != y and v == '#':
                cnt += 1
    if cnt == k:
        return True
    else:
        return False

result = 0
for i in range(h + 1):
    for j in range(w + 1):
        if ex(r, i, j, k):
            result += 1

print(result)
