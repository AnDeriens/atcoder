# -*- coding: utf-8 -*-

import collections
import copy

n = int(input())
r = list(map(int, input().split(' ')))
r.sort(reverse=True)
counter = collections.Counter(r)

r2 = list(set(copy.copy(r)))
r2.sort(reverse=True)


result = 0
for i, v in enumerate(r2):
    if i == 0 and counter[v] > 1:
        result += v * (counter[v] - 1)
    elif i != 0:
        result += r2[i - 1] * (counter[v] - 1)

    print(result)




print(result)
