# -*- coding: utf-8 -*-

d,g = map(int, list(input().split(' ')))

score_list = [0] * d

for i in range(d):
    p, c = map(int, list(input().split(' ')))
    score_list[i] = {
        "index": i + 1,
        "number": p,
        'bornus': c,
        'score': 100 * (i + 1),
        'total_score': 100 * (i + 1) * p + c
    }

score_list.sort(key=lambda x: x["total_score"], reverse=True)

ans = 0
for item in score_list:

    if g >= item['total_score']:
        ans += item['number'] 
        g -= item['total_score']
    else:
        _num = g // item['score']
        ans += _num
        break

print(ans)
