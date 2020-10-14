# -*- coding: utf-8 -*-

n = int(input())
x = int(input(), 2)

def popcount(n):
    return bin(n).count('1')

def replace(n):
    return n % popcount(n)

def f(n):
    i = 0
    while n > 0:
        i += 1
        n = replace(n)

    return i

def reverse(num, n):
    return num ^ (1 << n)

for i in range(1, n + 1):
    print(f(reverse(x, i)))

