# -*- coding: utf-8 -*-

n = int(input())

lengths = list(map(int, input().split()))

l_max = max(lengths)
i_l_max = lengths.index(l_max)

ans = 0
_max = lengths[0]

for i in range(len(lengths)):
    if i < i_l_max:
        if _max > lengths[i]:
            ans += _max - lengths[i]
        else:
            _max = lengths[i]
    else:
        ans += l_max - lengths[i]

print(ans)
