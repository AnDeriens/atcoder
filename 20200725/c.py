# -*- coding: utf-8 -*-

n,k = list(map(int, list(input().split())))
scores = list(map(int, list(input().split())))

for i in range(k + 1, n + 1):
    remove = scores[i - k - 1]
    add    = scores[i - 1]

    if remove < add:
        print('Yes')
    else:
        print('No')
