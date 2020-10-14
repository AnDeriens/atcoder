# -*- coding: utf-8 -*-

n, m = map(int, input().split(' '))
c = [map(int, list(input().split(' '))) for _ in range(m)]

r = [[0] * n for _ in [0] * n]
for i in c:
    x, y = i
    r[x - 1][y - 1] = 1

def dfs(x,y,i):
    if not(0 <= x < n) or not(0 <= y < n) or r[x][y] == 0:
        return i
    else:
         i += 1

    r[x][y] = 1
    i = dfs(x+1, y, i)
    i = dfs(x-1, y, i)
    i = dfs(x, y+1, i)
    i = dfs(x, y-1, i)

_max = 0
for _x in range(n):
    _max = max(dfs(_x, 0, 0), _max)

print(_max)
