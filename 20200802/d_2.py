# -*- coding: utf-8 -*-

n = int(input())
cs = input()

c_sliced = cs[0:cs.rfind('R') + 1]
c_list = list(c_sliced)

_s = c_list[0]
r = _s
for i in range(len(c_list)):
    if _s != c_list[i]:
        r += c_list[i]
        _s = c_list[i]

print(r)
