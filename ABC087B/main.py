# -*- coding: utf-8 -*-
a = int(input())
b = int(input())
c = int(input())
x = int(input())

list_a = [500 * int(i) for i in range(a + 1)]
list_b = [100 * int(i) for i in range(b + 1)]
list_c = [50 * int(i) for i in range(c + 1)]

r = 0

for y_a in list_a:
    for y_b in list_b:
        for y_c in list_c:
            if x == y_a + y_b + y_c:
                r += 1

print(r)
