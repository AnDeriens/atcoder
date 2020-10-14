# -*- coding: utf-8 -*-

n = int(input())

r = ''

def to_moji(x: int):
    if x == 0:
        x = 26
    return chr(96 + x)

def devide(x, moji):
    a = x // 26
    b = x % 26

    if b == 0:
        a -= 1

    if a < 1:
        moji = to_moji(b) + moji
        return moji
    elif 1 <= a and a <= 26:
        moji = to_moji(b) + moji
        moji = to_moji(a) + moji
        return moji
    else:
        moji = to_moji(b) + moji
        return devide(a, moji)

print(devide(n, r))
