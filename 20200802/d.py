# -*- coding: utf-8 -*-

n = int(input())
cs = input()

c_sliced = cs[0:cs.rfind('R') + 1]
c_list = list(c_sliced)

def replace(s_list):
    string = ''.join(s_list)
    index_r = string.rfind('R')
    index_w = string.find('W')
    s_list[index_r] = 'W'
    s_list[index_w] = 'R'
    return ''.join(s_list)

i = 0
while c_sliced.rfind('R') > c_sliced.find('W') and c_sliced.rfind('R') * c_sliced.find('W') >= 0:
    i += 1
    c_list = list(c_sliced)
    c_sliced = replace(c_list)
    c_sliced = cs[0:cs.rfind('R') + 1]

print(i)

