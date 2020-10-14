# -*- coding: utf-8 -*-

n = int(input())
scores = list(map(int, list(input().split())))

amount = 1000

def exec(amount, scores):
    # その時の所持金を、scoresのセットの中で最大にする
    return amount

_i = 0
_s = scores[0]
for i in range(n):
    s = scores[i]
    if _s < s:
        _i = i
        score_set = scores[_i: i - _i + 1]
        amount = exec(amount)

print(amount)
